# models

from otree.api import *
from settings import DEBUG
from settings import num_participant

class C(BaseConstants):
    NAME_IN_URL = 'phase1'
    PLAYERS_PER_GROUP = 4 if DEBUG else int(num_participant) # wait for all 12 participants
    NUM_ROUNDS = 1 if DEBUG else 3
    Correct_Prediction = ["A", "B", "Tie"] # predefined correct predictions (may be randomized)
    Prediction_Reward = cu(50)

    midterm_examples = {
            1: "明天有期中考，而我目前還有兩個章節沒讀。如果現在睡覺，明天早上很可能來不及複習。雖然熬夜很累，但至少能把重點看完，所以我決定先讀完再睡。",
            2: "明天有期中考，而我目前還有兩個章節沒讀。雖然熬夜很累，但至少能把重點看完，所以我決定先讀完再睡。",
            3: "明天有期中考，而我目前還有兩個章節沒讀。如果現在睡覺，明天早上很可能來不及複習，所以我決定先讀完再睡。",
            4: "明天有期中考，我覺得現在還需要再準備一下。雖然熬夜很累，但至少能把重點看完，所以我決定先讀完再睡。",
            5: "我剛看窗外的天色整片變得很暗，就跟牛排不小心烤太焦的時候差不多黑，而且雲層厚到不行，讓我想到我早上吃的厚切吐司，吃起來非常軟，只可惜這麼厚的雲層不會讓我有想要吃他的慾望。而且我看氣象預報也說今天降雨機率有80%，順帶一提播報的主播長得很好看。我猜等一下出門一定會下大雨，大概是大到外國人來會說raining cats and dogs的程度，怕被淋得濕答答的，可能會變成落湯雞，有狗又有雞只差猴子就能打鬼了。為了避免這種情況，所以決定還是帶一下傘比較保險。",
            6: "我剛看窗外的天色整片變得很暗、雲層厚到不行，而且我看氣象預報也說今天降雨機率有80%。我猜等一下出門一定會下大雨，怕被淋得濕答答的，所以決定還是帶一下傘比較保險。",
            7: "我剛看窗外的天色整片變得很暗、雲層厚到不行。我猜等一下出門一定會下大雨，怕被淋得濕答答的，所以決定還是帶一下傘比較保險。"
        }

    round_reasonings = {
            1: (midterm_examples.get(1), midterm_examples.get(2)),
            2: (midterm_examples.get(4), midterm_examples.get(1)),
            3: (midterm_examples.get(1), midterm_examples.get(5))
        }

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

def calculate_results(self):
    correct_answer = C.Correct_Prediction[self.round_number - 1]

    for p in self.get_players():
        p.is_correct = (p.prediction == correct_answer)
        p.payoff = C.Prediction_Reward if p.is_correct else cu(0)
    
class Player(BasePlayer):  
    prediction = models.StringField(
        choices = ["A", "Tie", "B"],
    )
    is_correct = models.BooleanField()


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
        reason_a, reason_b = C.round_reasonings.get(player.round_number)

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
        reason_a, reason_b = C.round_reasonings.get(player.round_number)
        result_text = "正確" if player.is_correct else "錯誤"

        correct_answer = C.Correct_Prediction[player.round_number - 1]
        if correct_answer == "A":
            answer_text = "理由A"
        elif correct_answer == "B":
            answer_text = "理由B"
        elif correct_answer == "Tie":
            answer_text = "兩者平手"

        return {
            "reason_a": reason_a,
            "reason_b": reason_b,
            "result_text": result_text,
            "answer_text": answer_text
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
