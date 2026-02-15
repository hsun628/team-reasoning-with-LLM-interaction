from otree.api import *
from openai import OpenAI
import os
from dotenv import load_dotenv

import random
import json
import re
import time

from settings import DEBUG
from settings import num_participant

load_dotenv()

my_api_key = os.getenv('api_key')   # DO NOT PASTE YOUR API_KEY HERE!
model_used = "gpt-5.2"

client = OpenAI(api_key = my_api_key)  # DO NOT PASTE YOUR API_KEY HERE!

class C(BaseConstants):
    NAME_IN_URL = 'phase_AI'
    PLAYERS_PER_GROUP = 2 if DEBUG else int(0.5*num_participant)
    NUM_ROUNDS = 3 if DEBUG else 10
    Pass_Reward = 100 # the payoff for players who pass the reason assessment
    reasoning_rounds = [1, 3] if DEBUG else [1, 5, 10]

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass 

class Player(BasePlayer):
    gpt_reason = models.LongStringField()
    gpt_analysis = models.LongStringField() 
    winner_type = models.StringField()

    def gpt_process(self):
        if "reason_history" not in self.participant.vars:
            self.participant.vars["reason_history"] = []

        history = []

        time.sleep((self.id_in_subsession - 1) * 0.5)

        for r in C.reasoning_rounds:
            human_reason = self.participant.vars.get(f"reason_{r}", "").strip()
            human_decision = self.participant.vars.get(f'decision_{r}')
            is_luckywinner = self.participant.vars.get(f"is_luckywinner_{r}")

            luckywinner_text = "是" if is_luckywinner else "否"

            print(f"=====當前處理回合 {r} - 受試者{self.id_in_subsession} =====")
            print(f"human_decision: {human_decision}")
            print(f"human_reason: '{human_reason}'")

            if human_reason and human_decision is not None:
                try:
                    print(f"受試者{self.id_in_subsession} 正在呼叫API")
                    
                    gpt_reason = gpt_generate(human_decision)
                    winner_type, gpt_analysis = gpt_judge(human_reason, gpt_reason)
                    self.winner_type = winner_type

                    target_player_in_round = self.in_round(r)

                    if winner_type in ["Human", "Tie"]:
                        target_player_in_round.payoff = cu(C.Pass_Reward)
                        result_text = "您的理由較好"
                    else:
                        target_player_in_round.payoff = cu(0)
                        result_text = "AI生成的理由較好"

                    history.append({
                        "round": r,
                        "human_reason": human_reason,
                        "gpt_reason": gpt_reason,
                        "winner_type": winner_type,
                        "luckywinner_text": luckywinner_text,
                        "result_text": result_text,
                        "final_payoff": target_player_in_round.payoff
                    })

                    print(f"API呼叫成功 - winner: {winner_type}")

                except Exception as e:
                    print(f"Round_{r} API呼叫失敗: {e}")

        all_rounds = self.in_all_rounds()
        total_phase2_payoff = sum([p.payoff for p in all_rounds])

        self.participant.vars["total_phase2_payoff"] = total_phase2_payoff
        self.participant.vars["reason_history"] = history


########################################################################################################################

def gpt_generate(participant_decision):

    generate_prompt = f"""

        ### Role: 
            You are a college student participating in an economics experiment. Your task is to write a reasoning for a specific decision.

        ### Task: 
            You will be presented with a participant's decision from the experiment described below. Based on that decision, write a reasoning (about 30 characters in Traditional Chinese) explaining the underlying thoughts and the information used for that choice. The reasoning should follow the requirements below:
            * **Requirements**:
                * Your reasoning should include the information and beliefs you observed or used, and demonstrate the process of how you derived the decision from said information and beliefs.
                * The reasoning should sound like a real participant, not like a game theory expert.
                * Do not mention Nash equilibrium, infinite iteration, dominance, or formal strategic terminologies.
                * You may think strategically, but do not fully formalize or optimize the reasoning.* Use natural, conversational language.
                * Some uncertainty is allowed (e.g., “I guess”, “maybe”, “probably”).
                * The reasoning should not look highly sophisticated or mathematically complete.

        ### Experimental Rules:
            * Part II consists of 10 rounds. At the beginning, the computer randomly divides all participants into two equal groups.
            * In each round, you must choose an integer between 0 and 100.
            * The average of all numbers chosen by participants in your group is called the "Average Number."
            * The person whose choice is closest to **0.7 times the Average Number** (called the "Target Number") is the winner of the round. In the event of a tie, the computer will randomly select one winner.
            * Before each round begins, the computer will display the past "Average Number" and "Target Number" for your group.

        ### Response Format:
            Please provide the participant's decision and the reasoning (in Traditional Chinese) you have written. Your response must strictly follow this JSON format:
            {{
                "decision": {participant_decision},
                "reasoning": "Your reasoning (about 30 characters in Traditional Chinese) explaining the underlying thoughts and the information used for that choice for the provided decision."
            }}
    """

    for attempt in range(3):
        try:
            response = client.chat.completions.create(
                model = model_used,
                messages = [
                    {"role": "system", "content": generate_prompt},
                    {"role": "user", "content": f"""Based on that decision: {participant_decision}, write a 25-45 word reasoning (in Traditional Chinese) explaining the underlying thoughts and the information used for that choice. Your response must strictly follow the specified JSON format.
                """}
                ],
                response_format = {"type" : "json_object"},
                temperature = 0.7,   # lower value gives more stable response (0-2)
                max_completion_tokens = 300  
            )

            generate_result = response.choices[0].message.content
            data_generate = json.loads(generate_result)

            return data_generate.get("reasoning")
    
        except Exception as e:
            if attempt < 2:
                time.sleep(2)
                continue

            print(f"JSON / API error: {e}")
            return "JSON / API error"
    
########################################################################################################################

def gpt_judge(reasoning_a, reasoning_b):
    reasons = [("A", reasoning_a), ("B", reasoning_b)]
    random.shuffle(reasons)
    
    judge_prompt = f"""

    ### Role:
        You are a professional judge. Your task is to evaluate the explanations provided by participants regarding their decision-making process.

    ### Judging Task:
        Compare the reasons provided by the following two participants. Determine which participant more specifically explains the "underlying thoughts" and the "information used" behind their decision.

    ### Evaluation Criteria (Strictly Adhere to the Following):

    * **Information & Belief:** Does the participant mention specific information they observed? Do they state their inferences or hypotheses about the current situation? Did they elaborate on how they arrive at these inferences and hypotheses?

    * **Logic & Strategy:** Does the participant demonstrate the derivation process from the aforementioned information and beliefs to their final decision?
        * **Is the logic consistent with the experimental rules? (Crucial):** Does the claimed causal relationship in the reasoning align with the experimental rules? If the reasoning fundamentally contradicts the rules or physical facts (e.g., claiming that a certain decision can achieve "Effect A," when the rules make it impossible for that decision to ever produce such an effect), the reasoning should be considered a "Logical Break." Such a reasoning must receive a lower evaluation than one that is logically self-consistent.

        * Does the final decision mentioned or implied in the reasoning match the actual decision one chose? (For example, if one chooses A but the reasoning explains the reason of choosing B, then the reasoning should receive a lower evaluation.)

    * **Level of Specificity:** Is the reason specific? (For example: prefer "Because I observed A, I expected B, and therefore adopted strategy C" over "I just picked one" or "I wanted to choose this"). You can further judge based on:
        - Whether the reason contains specific information related to the rules, rather than just a vague description.
        - Whether there are clear causal and logical relationships between sentences.

    ### Strict Prohibitions (Do NOT Consider):

    * **Do NOT judge based on the "quality" or "winning probability" of the decision:** Even if the participant's reasoning contains calculation errors or the decision itself has a very low probability of winning, as long as they clearly and logically explain their thought process, that reason should receive a higher evaluation. 

    * **Note:** Your mission is to evaluate "who more specifically explained their underlying thoughts and information used," NOT "how smart the decision was."

    * **Reasoning Length**: Do not judge the specificity or detail of a reason based on its word count. (For example: "Because I observed A, I expected B, and therefore adopted strategy C" and "Under my careful observation, I discovered A, so I expect others to do B; consequently, I decided to adopt strategy C to increase my winning probability" describe the same content. They should receive the same or very similar evaluation).

    * **Do NOT Favor "Self-Invented Jargon":** Participants may use self-invented professional-sounding terms (e.g., "Boundary Suppression Effect," "Group Deviation Law"). Do not award a higher evaluation simply because the reasoning contains these non-standard terms that appear neither in the experimental instruction nor in everyday language. 
        - Pay attention to whether the participant explicitly explains the meaning of these invented terms, or whether the terms carry concrete logical weight within their common-sense semantic context. 
        - If the reasoning becomes hollow or lacks substance once these terms are removed, the reasoning should receive a lower evaluation.

    ### Experimental instruction:
        * Part II consists of 10 rounds. At the beginning, the computer randomly divides all participants into two equal groups.
        * In each round, you must choose an integer between 0 and 100.
        * The average of all numbers chosen by participants in your group is called the "Average Number."
        * The person whose choice is closest to **0.7 times the Average Number** (called the "Target Number") is the winner of the round. In the event of a tie, the computer will randomly select one winner.
        * Before each round begins, the computer will display the past "Average Number" and "Target Number" for your group.

    ### Response Format:        
        The following are two reasonings for a decision. Please evaluate them based on the judge criterion and prohibition above.

            - reasoning_1: {reasons[0][1]}
            - reasoning_2: {reasons[1][1]}

        Please state (in the following specified JSON format) which reasoning more specifically explained the "underlying thoughts" and "information used," (If the two are extremely close, you may declare a tie) and briefly provide the reasons (in Traditional Chinese and the following specified JSON format) for your judgment.

        Your response must strictly follow this JSON format:
            {{
                "winner": "reasoning_1" or "reasoning_2" or "Tie",
                "analysis": "A brief reason for your judgement of the winner."
            }}
        
    """
    
    response = client.chat.completions.create(
        model = model_used,
        messages = [
            {"role": "system", "content": judge_prompt},
            {"role": "user", "content": f"""Please state (in the following specified JSON format) which reasoning more specifically explained the "underlying thoughts" and "information used." (If the two are extremely close, you may declare a tie). Your response must strictly follow the specified JSON format."""}],
        response_format = {"type" : "json_object"},
        temperature = 0,   # test
        max_completion_tokens = 500
    )

    judge_result = response.choices[0].message.content
    data_judge = json.loads(judge_result)
    winner = data_judge.get("winner", "")
    gpt_analysis = data_judge.get("analysis", "")


    if "reasoning_1" in winner:
        final_winner = "Human" if reasons[0][0] == "A" else "AI"
    elif "reasoning_2" in winner:
        final_winner = "AI" if reasons[0][0] == "A" else "Human"
    elif "Tie" in winner:
        final_winner = "Tie" 

    return final_winner, gpt_analysis

########################################################################################################################

#def set_payoffs(subsession: Subsession):
#    all_players = subsession.get_players()

#    for p in all_players:
#        human_reason = ""
#        human_decision = None
#        phase2_payoff = cu(0)

#        if subsession.round_number in C.reasoning_rounds:
#            p.winner_type = "Processing"
#            p.gpt_reason = "Processing"

#            raw_reason = p.participant.vars.get(f"reason_{p.round_number}")
#            human_reason = str(raw_reason).strip() if raw_reason else ""
#            human_decision = p.participant.vars.get(f'decision_{p.round_number}')
#            phase2_payoff = p.participant.vars.get(f'payoff_{p.round_number}', cu(0))

#            print(f"=====回合 {p.round_number} - 受試者{p.id_in_subsession} =====")
#            print(f"human_decision: {human_decision}")
#            print(f"human_reason: '{human_reason}'")
           
#            if human_reason and human_decision is not None:
#                wait_time = (p.id_in_subsession - 1)*0.5
#                time.sleep(wait_time)
#                print(f"受試者{p.id_in_subsession} 正在呼叫API")

#                try:
#                    generated_reason = gpt_generate(human_decision)
#                    p.gpt_reason = str(generated_reason).strip()

#                    time.sleep(1)

#                    p.winner_type, p.gpt_analysis = gpt_judge(human_reason, p.gpt_reason)

#                    if p.winner_type == "Human":
#                        p.payoff = cu(C.Pass_Reward) - phase2_payoff # payoff in oTree is cumulative
#                    else:
#                        p.payoff = - phase2_payoff
#                    print(f"API呼叫完成 - winner: {p.winner_type}")
#                except Exception as e:
#                    print(f"API呼叫失敗: {e}")
#                    p.gpt_reason = "API error"
#                    p.winner_type = "Error"
#                    p.payoff = phase2_payoff
#            else:
#                p.gpt_reason = "No data"
#                p.winner_type = "No data"
#                p.payoff = phase2_payoff
#        else:
#            print(f"-回合{p.round_number} 非額外說明回合")
#            p.winner_type = ""
#            p.gpt_reason = ""
#            p.payoff = cu(0)

#        if p.round_number == 1:
#            p.participant.vars["reason_history"] = []

#        if p.round_number in C.reasoning_rounds:
#            current_history = p.participant.vars.get("reason_history", [])

#            if not any(d.get("round") == p.round_number for d in current_history):
#                current_history.append({
#                    "round": p.round_number,
#                    "human_reason": human_reason,
#                    "gpt_reason": p.gpt_reason if p.gpt_reason != "Processing" else "API error",
#                    "winner": p.winner_type,
#                    "gpt_analysis": p.gpt_analysis
#                })
#        else:
#            if not any(d.get("round") == p.round_number for d in current_history):
#                current_history.append({
#                    "round": p.round_number,
#                    "human_reason": "",
#                    "gpt_reason": "",
#                    "winner": None,
#                    "gpt_analysis": ""
#                    })

#        p.participant.vars["reason_history"] = current_history

########################################################################################################################

# pages

class InstructionPage(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class ProcessingPage(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.gpt_process()

class Results(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

    @staticmethod
    def vars_for_template(player):
        reason_history = player.participant.vars.get("reason_history", [])
        total_phase2_payoff = player.participant.vars.get("total_phase2_payoff")

        return {
            "reason_history": reason_history,
            "total_phase2_payoff": total_phase2_payoff
        }

#        for p in player_history:
#            is_luckywinner = p.participant.vars.get(f'is_luckywinner_{p.round_number}')
            
#            extra_data.append({
#                'round': p.round_number,
#                'is_luckywinner': "是" if is_luckywinner else "否",
#                'result': "您的理由較好" if p.winner_type == "Human" else "AI生成的理由較好",
#                "round_payoff": p.payoff 
#            })
            
#        return {
#            'extra_data': extra_data,
#            "total_payoff": player.participant.payoff
#        }
    
#    def after_all_players_arrive(group):
#        for p in group.get_players():
#            reason_history = []
            
#            for r in C.reasoning_rounds:
#                p_in_r = p.in_round(r)
#                reason_history.append({
#                    "round": int(r),
#                    "reason": p_in_r.reason,
#                    "gpt_reason": p_in_r.gpt_reason
#                })

#            p.participant.vars["reason_history"] = reason_history



page_sequence = [
    InstructionPage,
    ProcessingPage,
    Results
    ]

 