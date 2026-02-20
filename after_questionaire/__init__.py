# models

from otree.api import *
from settings import DEBUG
from settings import num_participant


class C(BaseConstants):
    NAME_IN_URL = 'after_questionaire'
    PLAYERS_PER_GROUP = 4 if DEBUG else int(num_participant) # wait for all 12 participants
    NUM_ROUNDS = 3 if DEBUG else 10
    Prediction_Reward = 50
    reasoning_rounds = [1, 3] if DEBUG else [1, 5, 10]
    exchange_rate = 0.5   # exchange rate for NTD
    participation_fee = 150

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

def calculate_results(group:Group):
    for p in group.get_players():
        all_players = p.subsession.get_players()
        target_p = [tp for tp in all_players if tp.id_in_subsession == p.target_participant_id][0]

        history = target_p.participant.vars.get("reason_history", [])

        current_entry = None
        for entry in history:
            if entry.get("round") == p.round_number:
                current_entry = entry
                break
        
        if current_entry:
            real_winner_type = current_entry.get("winner_type")
            is_correct = False

            if p.prediction == "Tie":
                is_correct = (real_winner_type == "Tie")
            else:
                if not p.is_flipped:
                    if (p.prediction == "A" and real_winner_type == "Human") or \
                       (p.prediction == "B" and real_winner_type == "AI"):
                        is_correct = True
                else:
                    if (p.prediction == "A" and real_winner_type == "AI") or \
                       (p.prediction == "B" and real_winner_type == "Human"):
                        is_correct = True

            p.payoff = cu(C.Prediction_Reward) if is_correct else cu(0)
    
class Player(BasePlayer):  
    prediction = models.StringField(
        choices = ["A", "Tie", "B"],
        widget = widgets.RadioSelectHorizontal,
    )

    target_participant_id = models.IntegerField()
    is_flipped = models.BooleanField()


#############################################################################

# pages

from otree.api import *
import random

class InstructionPage(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class questionaireStartWaitPage(WaitPage):
    title_text = "請等待其他受試者完成準備"

    wait_for_all_groups = True

class Prediction(Page):
    form_model = 'player'
    form_fields = ['prediction']

    @staticmethod
    def is_displayed(player):
        return player.round_number in C.reasoning_rounds

    @staticmethod
    def vars_for_template(player):
        all_players = player.subsession.get_players()
        other_players = [p for p in all_players if p.id_in_subsession != player.id_in_subsession]
        target_player = random.choice(other_players)   # your own reasoning may be drawn

        player.target_participant_id = target_player.id_in_subsession

        history = target_player.participant.vars.get("reason_history",[])

        current_entry = None
        for entry in history:
            if entry.get("round") == player.round_number:
                current_entry = entry
                break
        if not current_entry:
            current_entry = {
                "human_reason": "NaN",
                "gpt_reason": "NaN",
                "winner_type": "NaN"
            }

        target_decision = target_player.participant.vars.get(f'decision_{player.round_number}')

        player.is_flipped = random.choice([True, False])

        if player.is_flipped:
            reason_a = current_entry.get("gpt_reason")
            reason_b = current_entry.get("human_reason")
        else:
            reason_a = current_entry.get("human_reason")
            reason_b = current_entry.get("gpt_reason")

        reasoning_round_num = C.reasoning_rounds.index(player.round_number) + 1

        return {
            "round_number": player.round_number,
            "target_id": player.target_participant_id,
            "target_decision": target_decision,
            "reason_a": reason_a,
            "reason_b": reason_b,
            "round_number": player.round_number,
            "reason_history": current_entry,
            "reasoning_round_num": reasoning_round_num
        }

class PredictionWaitPage(WaitPage):
    title_text = "請等待其他受試者完成預測"
    
    @staticmethod
    def is_displayed(player):
        return player.round_number in C.reasoning_rounds

    after_all_players_arrive = 'calculate_results'


class Results(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number in C.reasoning_rounds
    
    @staticmethod
    def vars_for_template(player):
        target_id = player.target_participant_id
        all_players = player.subsession.get_players()

        target_player = [p for p in all_players if p.id_in_subsession == target_id]

        if target_player:
            target_player = target_player[0]
            history = target_player.participant.vars.get("reason_history", [])

            current_entry = None
            for entry in history:
                if entry.get("round") == player.round_number:
                    current_entry = entry
                    break

            if current_entry:
                if player.is_flipped:
                    reason_a = current_entry.get("gpt_reason")
                    reason_b = current_entry.get("human_reason")
                else:
                    reason_a = current_entry.get("human_reason")
                    reason_b = current_entry.get("gpt_reason")

                reason_a = reason_a.strip()
                reason_b = reason_b.strip()
                real_winner = current_entry.get("winner_type")
            else:
                reason_a = "NaN"    
                reason_b = "NaN"
                real_winner = "NaN"
        else:
            reason_a = "NaN"
            reason_b = "NaN"
            real_winner = "NaN"

        is_correct = False
        if player.prediction == "Tie":
            is_correct = (real_winner == "Tie")
        elif player.prediction == "A":
            if not player.is_flipped:
                is_correct = (real_winner == "Human")
            else:
                is_correct = (real_winner == "AI")

        elif player.prediction == "B":   
            if not player.is_flipped:
                is_correct = (real_winner == "AI")
            else:
                is_correct = (real_winner == "Human")   

        result_text = "正確" if is_correct else "錯誤" 

        reasoning_round_num = C.reasoning_rounds.index(player.round_number) + 1 
        
        return {
            "reason_a": reason_a,
            "reason_b": reason_b,
            "real_winner": real_winner,
            "is_correct": is_correct,
            "result_text": result_text,
            "reasoning_round_num": reasoning_round_num
        }

class Payoff(Page):
    title_text = "感謝您參加本實驗，請確認您的報酬金額。"

    @staticmethod
    def vars_for_template(player):
        total_payoff_no_participation_fee = player.participant.payoff
        if player.round_number == C.NUM_ROUNDS:
            if not player.participant.vars.get("fee_added"):
                player.participant.payoff = player.participant.payoff*C.exchange_rate + cu(C.participation_fee)
                player.participant.vars["fee_added"] = True

        return {
            "total_payoff_no_participation_fee": total_payoff_no_participation_fee,
            "total_NTD_payoff": player.participant.payoff
        }
    
    def is_displayed(player):
        return player.round_number == C.NUM_ROUNDS
    
class redirect_to_form(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == C.NUM_ROUNDS


page_sequence = [
    InstructionPage,
    questionaireStartWaitPage,
    Prediction,
    PredictionWaitPage,
    Results,
    Payoff,
    redirect_to_form
]
