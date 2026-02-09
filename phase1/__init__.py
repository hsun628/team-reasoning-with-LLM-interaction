# models

from otree.api import *
from settings import DEBUG
from settings import num_participant

class C(BaseConstants):
    NAME_IN_URL = 'phase1'
    PLAYERS_PER_GROUP = 4 if DEBUG else int(num_participant) # wait for all 12 participants
    NUM_ROUNDS = 1 if DEBUG else 3
    Correct_Prediction = ["A", "B", "Tie"] # predefined correct predictions (may be randomized)
    Prediction_Reward = 50

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

class welcome(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1
    
class Phase1StartWaitPage(WaitPage):
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
        midterm_examples = {
            1: "明天有期中考，而我目前還有兩個章節沒讀。如果現在睡覺，明天早上很可能來不及複習。雖然熬夜很累，但至少能把重點看完，所以我決定先讀完再睡。",
            2: "明天有期中考，而我目前還有兩個章節沒讀。雖然熬夜很累，但至少能把重點看完，所以我決定先讀完再睡。",
            3: "明天有期中考，而我目前還有兩個章節沒讀。如果現在睡覺，明天早上很可能來不及複習，所以我決定先讀完再睡。",
            4: "明天有期中考，我覺得現在還需要再準備一下。雖然熬夜很累，但至少能把重點看完，所以我決定先讀完再睡。",
            5: "明天有期中考，而我目前還有兩個章節還沒讀完，進度其實有點落後。如果現在就直接去睡覺，明天早上能用來複習的時間應該會不夠，很可能來不及把這兩個章節的重點再看過一遍。雖然熬夜讀書一定會讓人覺得很累，精神也可能沒有那麼好，但至少還能把重要的內容先讀完、心裡比較有底。綜合考量時間與準備程度之後，我還是決定先把剩下的部分讀完，再去休息睡覺。"
        }

        round_reasonings = {
            1: (midterm_examples.get(1), midterm_examples.get(2)),
            2: (midterm_examples.get(4), midterm_examples.get(1)),
            3: (midterm_examples.get(1), midterm_examples.get(5))
        }

        reason_a, reason_b = round_reasonings.get(player.round_number)

        return {
            "reason_a": reason_a,
            "reason_b": reason_b
        }

class PredictionWaitPage(WaitPage):
    title_text = "請等待其他受試者完成預測"
    
    after_all_players_arrive = 'calculate_results'

class Results(Page):
    @staticmethod
    def vars_for_template(player):
        midterm_examples = {
            1: "明天有期中考，而我目前還有兩個章節沒讀。如果現在睡覺，明天早上很可能來不及複習。雖然熬夜很累，但至少能把重點看完，所以我決定先讀完再睡。",
            2: "明天有期中考，而我目前還有兩個章節沒讀。雖然熬夜很累，但至少能把重點看完，所以我決定先讀完再睡。",
            3: "明天有期中考，而我目前還有兩個章節沒讀。如果現在睡覺，明天早上很可能來不及複習，所以我決定先讀完再睡。",
            4: "明天有期中考，我覺得現在還需要再準備一下。雖然熬夜很累，但至少能把重點看完，所以我決定先讀完再睡。",
            5: "明天有期中考，而我目前還有兩個章節還沒讀完，進度其實有點落後。如果現在就直接去睡覺，明天早上能用來複習的時間應該會不夠，很可能來不及把這兩個章節的重點再看過一遍。雖然熬夜讀書一定會讓人覺得很累，精神也可能沒有那麼好，但至少還能把重要的內容先讀完、心裡比較有底。綜合考量時間與準備程度之後，我還是決定先把剩下的部分讀完，再去休息睡覺。"
        }

        round_reasonings = {
            1: (midterm_examples.get(1), midterm_examples.get(2)),
            2: (midterm_examples.get(4), midterm_examples.get(1)),
            3: (midterm_examples.get(1), midterm_examples.get(5))
        }

        reason_a, reason_b = round_reasonings.get(player.round_number)

        return {
            "reason_a": reason_a,
            "reason_b": reason_b
        }

class ResultsWaitPage(WaitPage):
    title_text = "請等待其他受試者確認結果"

page_sequence = [
    welcome,
    Phase1StartWaitPage,
    Prediction,
    PredictionWaitPage,
    Results,
    ResultsWaitPage
]
