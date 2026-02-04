# models

from otree.api import *
from settings import debug
from settings import num_participant


class C(BaseConstants):
    NAME_IN_URL = 'after_questionaire'
    PLAYERS_PER_GROUP = 4 if debug else num_participant # wait for all 12 participants
    NUM_ROUNDS = 1 if debug else 3
    Correct_Prediction = ["A", "B", "Tie"] # predefined correct predictions (may be randomized)
    Prediction_Reward = 50
    reasoning_rounds = [1, 3, 5] if debug else [1, 5, 10]

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

def calculate_results(self):
    correct_prediction = C.Correct_Prediction[self.round_number - 1]

    for p in self.get_players():
        if p.prediction == correct_prediction:
            p.payoff = cu(C.Prediction_Reward)
        else:
            p.payoff = cu(0)
    
class Player(BasePlayer):  
    prediction = models.StringField(
        choices = ["A", "Tie", "B"],
    )


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

class Prediction_2(Page):
    form_model = 'player'
    form_fields = ['prediction']

    @staticmethod
    def vars_for_template(player):
        all_players = player.subsession.get_players()

        other_player = random.choice(all_players)   # your own reasoning may be drawn

        history = other_player.participant.vars.get("reason_history",[])

        return {
            "target_id": other_player.id_in_subsession,
            "reason_history": history
        }

class PredictionWaitPage(WaitPage):
    title_text = "請等待其他受試者完成預測"
    
    after_all_players_arrive = 'calculate_results'

class Results(Page):
    title_text = "感謝您參加本實驗，請確認您的報酬金額。"


page_sequence = [
    InstructionPage,
    questionaireStartWaitPage,
    Prediction_2,
    PredictionWaitPage,
    Results,
]
