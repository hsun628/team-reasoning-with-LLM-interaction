from otree.api import *
from openai import OpenAI
import random
from settings import debug

my_api_key = "API_KEY"
model_used = "gpt-5"

client = OpenAI(api_key = my_api_key)

class C(BaseConstants):
    NAME_IN_URL = 'phase_AI'
    PLAYERS_PER_GROUP = 2 if debug else 6
    NUM_ROUNDS = 3 if debug else 10
    Pass_Reward = 100 # the payoff for players who pass the reason assessment
    reasoning_rounds = [1, 3, 5] if debug else [1, 5, 10]

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    gpt_reason = models.LongStringField() 
    winner_type = models.StringField() 

def gpt_generate(participant_decision):
    generate_prompt = "prompt"

    response = client.chat.completions.create(
        model = model_used,
        messages = [
            {"role": "system", "content": generate_prompt},
            {"role": "user", "content": f"請針對以下受試者決策數字和實驗說明生成一個做出此決策的理由：{participant_decision}"}]
    )
    return response.choices[0].message.content

def gpt_judge(reason_a, reason_b):
    reasons = [("A", reason_a), ("B", reason_b)]
    random.shuffle(reasons)
    
    judge_prompt = f"""
    以下有兩個決策理由，請忽略其來源，僅針對『邏輯清晰度』與『說服力』進行評分。
    理由 1: {reasons[0][1]}
    理由 2: {reasons[1][1]}
    請僅回答『理由 1』或『理由 2』。
    """
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": judge_prompt},
                  {"role": "user", "content": "請選擇你認為較清楚地說明決策思考過程的理由。請僅回答『理由 1』或『理由 2』。"}]
    )
    result = response.choices[0].message.content
    
    if "理由 1" in result:
        return "Human" if reasons[0][0] == "A" else "AI"
    else:
        return "AI" if reasons[0][0] == "A" else "Human"

def set_payoffs(group: Group):
    if group.round_number in C.reasoning_rounds:
        for p in group.get_players():
            human_reason = p.participant.vars.get(f'reason_{p.round_number}')
            human_decision = p.participant.vars.get(f'decision_{p.round_number}')
            phase2_payoff = p.participant.vars.get(f'payoff_{p.round_number}', cu(0))
           
            if human_reason and human_decision:
                p.gpt_reason = gpt_generate(human_decision)
                p.winner_type = gpt_judge(human_reason, p.gpt_reason)

            if p.winner_type == "Human":
                p.payoff = cu(C.Pass_Reward) - phase2_payoff # payoff in oTree is cumulative
            else:
                p.payoff = - phase2_payoff
    else:
        for p in group.get_players():
            p.payoff = cu(0)

class Player(BasePlayer):
    gpt_reason = models.LongStringField() 
    winner_type = models.StringField()

##################################################################

# pages

class Results(Page):
    @staticmethod
    def vars_for_template(player):
        player_history = player.in_all_rounds()
        extra_data = []

        for p in player_history:
            if p.round_number in C.reasoning_rounds:
                is_luckywinner = p.participant.vars.get(f'is_luckywinner_{p.round_number}', cu(0)) > 0
            
            extra_data.append({
                'round': p.round_number,
                'is_luckywinner': "是" if is_luckywinner else "否",
                'assessment': "你的理由較清楚" if p.winner_type == "Human" else "生成的理由較清楚",
            })
            
        return {
            'extra_data': extra_data
        }

class payoff_WaitPage(WaitPage):
    title_text = "請等待其他受試者確認此階段實驗報酬"

    wait_for_all_groups = True

    after_all_players_arrive = 'set_payoffs'

page_sequence = [
    Results,
    payoff_WaitPage
    ]

 