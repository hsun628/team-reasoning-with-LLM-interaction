# models

from otree.api import *
from settings import debug
from settings import num_participant


class C(BaseConstants):
    NAME_IN_URL = 'after_questionaire'
    PLAYERS_PER_GROUP = 4 if debug else num_participant # wait for all 12 participants
    NUM_ROUNDS = 1 if debug else 3
    Prediction_Reward = 50
    reasoning_rounds = [1, 3, 5] if debug else [1, 5, 10]

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

def calculate_results(group:Group):
    for p in group.get_players():
        all_players = p.subsession.get_players()
        target_p = [tp for tp in all_players if tp.id_in_subsession == p.target_participant_id][0]

        history = target_p.participant.vars.get("reason_history", [])

        if history:
            real_winner_type = history[p.round_number - 1].get("winner")
            is_correct = False

            if p.prediction == "Tie":
                if real_winner_type == "Tie":
                    is_correct = True
            else:
                if not p.is_flipped:
                    if (p.prediction == "A" and real_winner_type == "Human") or (p.prediction == "B" and real_winner_type == "AI"):
                        is_correct = True
                else:
                    if (p.prediction == "A" and real_winner_type == "AI") or (p.prediction == "B" and real_winner_type == "Human"):
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
    
    @staticmethod
    def vars_for_template(player):
        all_players = player.subsession.get_players()

        other_player = random.choice(all_players)   # your own reasoning may be drawn

        player.target_participant_id = other_player.id_in_subsession

        history = other_player.participant.vars.get("reason_history",[])

        return {
            "target_id": other_player.id_in_subsession,
            "reason_history": history
        }

class questionaireStartWaitPage(WaitPage):
    title_text = "請等待其他受試者完成準備"

    wait_for_all_groups = True

    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class Prediction(Page):
    form_model = 'player'
    form_fields = ['prediction']

    @staticmethod
    def vars_for_template(player):
        target_id = player.target_participant_id
        all_players = player.subsession.get_players()

        target_player = [p for p in all_players if p.id_in_subsession == target_id][0]

        history = target_player.participant.vars.get("reason_history",[])

        current_entry = history[player.round_number - 1]

        player.is_flipped = random.choice([True, False])

        if player.is_flipped:
            reason_a = current_entry.get("gpt_reason")
            reason_b = current_entry.get("human_reason")
        else:
            reason_a = current_entry.get("human_reason")
            reason_b = current_entry.get("gpt_reason")

        return {
            "reason_a": reason_a,
            "reason_b": reason_b,
            "round_number": player.round_number,
            "reason_history": current_entry
        }

class PredictionWaitPage(WaitPage):
    title_text = "請等待其他受試者完成預測"
    
    after_all_players_arrive = 'calculate_results'

class Results(Page):
    pass

class Payoff(Page):
    title_text = "感謝您參加本實驗，請確認您的報酬金額。"

    @staticmethod
    def vars_for_template(player):
        player.participant.payoff += cu(150)   # add participation fee
        return {
            "total_payoff": player.participant.payoff
        }
    
    def is_displayed(player):
        return player.round_number == C.NUM_ROUNDS


page_sequence = [
    InstructionPage,
    questionaireStartWaitPage,
    Prediction,
    PredictionWaitPage,
    Results,
    Payoff
]
