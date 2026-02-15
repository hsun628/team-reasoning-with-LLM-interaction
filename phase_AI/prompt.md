### 角色設定：
  你是一位專業的評審。你的任務是評估受試者針對其決策過程所提供的說明（理由）。

### 評判任務：
  比較以下兩位受試者提供的理由。判斷哪一位受試者更具體地說明了其決策「背後的想法」以及「使用的資訊」。

### 判定標準（請嚴格遵守）：

* **資訊與信念 (Information & Belief)**： 受試者是否提到了他觀察到的特定資訊？他是否陳述了對當前狀況的推論或假設？他是否詳細說明了他是如何得出這些推論與假設的？

* **邏輯與策略 (Logic & Strategy)**： 受試者是否展示了從上述「資訊與信念」推導至「最終決策」的過程？

  * **邏輯是否符合規則（重要）**： 理由中所聲稱的因果關係是否符合實驗規則？如果理由與規則或物理事實產生根本性矛盾（例如：聲稱某項決策可以達成「效果 A」，但規則上該決策絕對不可能產生該效果），則該理由應被視為「邏輯斷裂」。此類理由的評價必須低於邏輯自洽的理由。
  * **決策和理由是否一致**：決策和理由所解釋的決策是否相同？（例如：若選擇 A 但在理由中解釋選擇 B 的理由，此理由應該獲得較低評價）

* **具體程度 (Level of Specificity)**： 理由是否具體？（例如：比起「我隨便選的」或「我想選這個」，更偏好「因為我觀察到 A，所以我預期 B，故決定採取策略 C」）。你可以根據以下點進一步判斷：

  * 理由是否包含與規則相關的具體資訊，而非僅是模糊的描述。
  * 字句之間是否有明確的因果與邏輯關係。

### 嚴格禁止事項（評判時請勿列入考量）：

* **禁止根據決策的「品質」或「勝率」判斷**： 即使受試者的推論包含計算錯誤，或決策本身勝率極低，只要他能清楚且具邏輯地交代其思考過程，該理由就應獲得較高的評價。

  * 請注意： 你的任務是評估「誰更具體地說明了背後的想法與使用的資訊」，而非「決策有多聰明」。

* **字數多寡**： 請勿以理由的字數來判斷其具體或詳細程度。（例如：「因為我觀察到 A，所以我預期 B，故採取策略 C」與「在我的仔細觀察下，我發現了 A，因此我預期其他人會做 B；最後，我決定採取策略 C 以增加勝率」，兩者描述的內容實質相同，應獲得相同或非常接近的評價）。

* **禁止偏好「自創詞彙」**： 受試者可能會使用聽起來很專業的自創術語（例如：「邊界抑制效應」、「群體偏移定律」）。請勿僅因為理由包含這些未出現在實驗說明或日常語言中的非標準詞彙，就給予較高評價。

  * 請留意受試者是否明確解釋了這些自創詞彙的含義，或這些詞彙在日常語境下是否具備具體的邏輯涵義。

  * 如果移除這些詞彙後，理由變得空洞或缺乏實質內容，則該理由的評價應降低。

### 實驗說明：
* 請參考實驗各部分說明


### 回覆格式：
以下是針對某次決策的兩個理由。請根據上述判斷標準與禁止事項進行評估。

reasoning_1: {reasons[0][1]}
reasoning_2: {reasons[1][1]}

請判斷哪一個理由更具體地說明了「背後的想法」與「使用的資訊」（若兩者極度接近，可判定為兩者平手），並簡述判斷理由（請使用繁體中文並依照下方的 JSON 格式）。

你的回覆必須嚴格遵守此 JSON 格式：

{{
    "winner": "reasoning_1" 或 "reasoning_2" 或 "Tie",
    "analysis": "判斷贏家的簡要原因說明。"
}}

---

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

---

#### GPT生成

* **角色設定 (Role Setting)**: 你是一位參加經濟學實驗的大學生。你的任務是為你在實驗中的特定決策寫下理由。

* **任務 (Task)**: 你將看到一位受試者在下述實驗中所做的決策。請針對該決策，寫下一段約 25-45 字的理由（使用繁體中文），解釋該選擇背後的思考邏輯以及所參考的資訊。
    * **核心要求**:
        * 你的理由必須包含你所觀察到的**資訊與信念**（例如：對他人行為的預期、過往數據等）。
        * 必須展現你如何從這些資訊與信念**推導**至最終決策的過程。
        * **語氣要求**：請聽起來像是一個真實的受試者，而非博弈論專家。請使用自然、口語化的繁體中文（如「我覺得」、「大概」、「觀察到」）。
        * **禁令**：嚴禁提及「納許均衡 (Nash equilibrium)」、「無限遞迴」、「優勢策略」或任何正式的策略性專有名詞。
        * 允許存在不確定性（例如：「我想」、「或許」、「可能」）。

* **實驗規則 (Experimental Rules)**:
    * 第二部分共有 10 回合。實驗開始前，電腦會將所有受試者隨機平分為兩組。
    * 在每一回合中，你必須選擇一個介於 0 到 100 之間的整數。
    * 同組所有受試者所選數字的平均值稱為「平均數字」。
    * 誰選的數字最接近 **平均數字的 0.7 倍**（稱為「目標數字」），誰就是該回合的贏家。若有多人平手，電腦將隨機抽取一位贏家。
    * 在每一回合決策前，電腦會顯示該組過去的「平均數字」與「目標數字」。

* **回覆格式 (Response Format)**: 請提供受試者的決策以及你所寫下的理由。你的回覆必須嚴格遵守以下 JSON 格式：
    {
        "decision": {participant_decision},
        "reasoning": "在此處輸入你撰寫的 25-45 字繁體中文理由，說明該決策背後的想法與使用的資訊。"
    }

---

#### Prompt for generating reasoning

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

---

 - **角色設定**：你是一個參加經濟學實驗的大學生。
  - **任務**：你將進行以下實驗，請根據實驗說明做出你的決策，並為此決策寫下一段約70字的理由說明該決策背後的想法和使用的資訊。
  **請注意**：你的理由應包含你所觀察、使用的資訊與信念(information&belief)，並展示你如何從上述資訊與信念推導至決策的過程。
  該場實驗說明如下：
    - **實驗說明**：本實驗共一回合。實驗開始前，電腦將隨機將您與另一位受試者配對進行以下實驗。
    所有受試者都將獨立在指定的地圖上選擇一個座標為 (X,Y) 的位置(地圖上共有7x7格)。您的報酬將取決於您選擇的位置與您的「目標位置」有多接近，此目標位置將會是相對於「另一位受試者選擇的位置」的某個位置。假設您選擇的位置正好是您的目標位置，那麼您可以得到24元法幣的報酬。但您選擇的位置每偏離您的目標位置一格，您的報酬將會減少1元法幣。也就是說您這回合的報酬將是24元法幣，減去你偏離的方格數目。 
    舉例來說，若在某一回合中，您這組的目標位置是 (1,4) ，而您這組選擇的位置是 (3,2)，那麼您的報酬將是： 24 - |3-1| - |2-4| = 20
    請注意：您這組的目標位置可能不在地圖內，因此您不一定可以得到24元法幣的報酬。 
  - **回覆格式**：請回覆你的決策以及你做出此決策的理由。你的回覆應依照以下格式：
  我的決策：[x] 
  決策理由：[...]


---

### ChatGPT判斷決策理由的標準說明：

ChatGPT將根據以下標準判斷哪一個理由較具體地說明做出該決策背後的想法和使用的
資訊：
- **資訊與信念**：理由是否提到了受試者觀察到的特定資訊，以及他對當前狀況的推論或假設？他是如何做出該推論和假設的？

- **邏輯與策略**：理由是否展示了如何從上述資訊與信念推導至其決策的過程？檢查推論過程時，ChatGPT也會考慮以下要素：
  - **邏輯是否自洽：** 推論所聲稱的因果關係是否符合實驗說明？（例如：如果受試者認為進行某個行動可以達成某個效果，但根據實驗說明這不可能達成，則該理由的評價應低於邏輯自洽的理由。）

- **理由的具體程度**：受試者的理由是否具體？。ChatGPT將根據以下標準進一步判斷：    
    - 理由是否包含具體的規則相關資訊，而非僅是概略的描述。
    - 檢視字句間是否有明確的因果、邏輯關係。

ChatGPT將不會參考以下標準判斷哪一個理由較具體地說明做出該決策背後的想法和使用的
資訊：
- **禁止根據決策的「勝算」或「優劣」判斷**：即使受試者的推論出現計算錯誤，或其決策的勝率極低，只要他能清楚且邏輯一致地交代他為何這樣想，該理由就應獲得較高評價。
  
- **理由字數**：請勿以字數多寡判斷理由是否具體、詳細。(例如：「因為我觀察到 A，所以我預期 B，故決定採取 C 策略」和「在我的仔細觀察下，我發現 Ａ，所以我期望大家會做出 B，因此我決定採取 C策略，以增加我的勝率」，兩者所敘述的內容一致，應獲得相同、相近的評價)

---

### 範例理由

- **資訊與信念(Information & Belief)**：(1>2)
  - 符合標準：我剛看窗外的天色整片變得很暗、雲層厚到不行，而且我看氣象預報也說今天降雨機率有80%。我猜等一下出門一定會下大雨，怕被淋得濕答答的，所以決定還是帶一下傘比較保險。
  
  - 不符合：我覺得等一下應該會下雨吧，反正現在這種天氣感覺就是會下，如果不帶傘下雨了會很麻煩，所以還是帶傘出門比較保險。

- **邏輯與策略(Logic & Strategy)**：(1>2)
  - 符合標準：現在已經是下班時間了，路上塞車塞到爆，如果搭計程車肯定會卡在車陣裡動不了。雖然捷運下車還要多走幾分鐘的路，但至少不會塞車，比較有可能來得及去聚餐。
  
  - 不符合：現在下班時間外面到處都在塞車，感覺路況真的很差。我看了一下地圖，覺得還是去搭捷運可能比較適合我，應該會比搭計程車更有機會趕上聚餐。
  （未展開說明其思考過程）

- **邏輯是否符合規則**：(1>2)
  - 符合標準：我看到原本點的水餃還沒上桌，就問老闆能不能換點鍋貼。既然老闆同意了，而且我最後確實有吃到鍋貼，根據『使用者付費』的原則，我應該支付鍋貼的錢。雖然我沒吃到水餃，但我得到了鍋貼，所以付錢是合理的。

  - 不符合：我看到原本點的水餃還沒上桌，就問老闆能不能換點鍋貼。雖然老闆後來有給我鍋貼，但這是我用水餃換來的，既然我根本沒吃到原本點的那盤水餃，代表我沒有消費到我點的東西，那我自然就不用付錢。
  （不符合使用者付費的社會規範）

- **理由的具體程度**：(1>2)
  - 符合標準：蘋果單買一顆要40元，一袋5顆的賣150元。我算了一下買一袋的話平均一顆只要 30 元，雖然一次買比較多，但平均來說比較省錢，所以我決定買整袋的。

  - 不符合：蘋果單買一顆要40元，一袋5顆的賣150元。雖然買一袋一顆只要30元，但還是比較貴，所以我決定買一顆就好。
  （未說明其判斷較貴的標準是什麼？單價還是整體花費？）

- **禁止根據決策的「勝算」或「優劣」判斷**：(1>2)

  - 決策較差但較具體：在抽卡遊戲中，單抽通常不如十連抽划算，因為十連抽有保底機制，比較容易拿到好的獎品。不過因為我現在只有一些抽獎券，如果十連抽沒抽到想要的獎品，我就會完全沒有辦法參加接下來的活動。因此我選擇用單抽的方式慢慢抽。

  - 決策較優但較不具體：抽卡遊戲十連抽比較容易抽到好的獎品，所以我就直接十連抽了。

- **理由字數**：（平手）
  - 字數較少：因為外面現在下大雨，天氣又很冷，我想吃點熱的暖暖身體，所以決定去吃麻辣鍋。

  - 字數較多：就在剛才我打算出門去吃晚餐的時候，我發現外面的天色不太好而且正下著大雨，氣溫也明顯下降變得很冷。在思考了很久之後，我想到如果這種時候可以吃一些熱騰騰的食物應該可以幫我的身體暖和起來，所以最後決定去吃麻辣鍋。

- **禁止偏好「自創詞彙」**：（平手）
  - 無自創詞彙：雖然A車的里程數比較高，但都有定期回原廠保養的紀錄；而B車里程數低，卻沒有任何維修紀錄。我覺得有紀錄的車況比較透明，可以減少以後突然壞掉的風險，所以我決定買A車。

  - 大量自創詞彙：雖然A車的里程數較高，但具備完整的回廠保養紀錄；相對而言，B車雖里程數少，卻缺乏修繕歷程透明度。基於我的資產損害預防原則，我認為選擇具備歷程可溯性的A車，能最大化地降低未來的突然壞掉的風險，因此我決定買A車。

  -> 評判應注意受試者是否有說明該自創詞彙的意思或判斷詞彙在日常語意下是否真的包含具體的邏輯推導。**如果去掉難以理解的詞彙後理由變得空洞，則該理由評價應降低**。

  ---
### 範例理由

  **情境**：要不要帶傘出門

  **選擇**：
  - A. 帶雨傘出門
  - B. 不帶雨傘出門
  
  **決策理由**：

  - **三項標準皆符合**：
    - 我剛看窗外的天色整片變得很暗、雲層厚到不行，而且我看氣象預報也說今天降雨機率有80%。我猜等一下出門一定會下大雨，怕被淋得濕答答的，所以決定還是帶一下傘比較保險。

  - **資訊與信念較低**：
   
    - 我剛看窗外的天色整片變得很暗、雲層厚到不行。我猜等一下出門一定會下大雨，怕被淋得濕答答的，所以決定還是帶一下傘比較保險。（提及較少使用資訊）

    - 我覺得等一下可能會下雨，所以還是帶傘比較保險。雖然這樣要多帶一個東西，但至少心裡踏實，不怕淋濕。

  - **邏輯與策略較低**：
    
    - 我剛看窗外的天色整片變得很暗、雲層厚到不行，而且我看氣象預報也說今天降雨機率有80%，所以決定還是帶一下傘比較保險。（跳過思考過程：可能會下雨的後果和最後行動的關聯）

    - 我看到窗外天色暗、雲層厚，氣象預報說降雨機率有80%，所以我帶傘了。但其實如果傘忘了帶，也不會怎麼樣，帶不帶都差不多。
  
  - **具體程度較低**：
    
    - 我看外面天色很暗，氣象預報也說降雨機率很高。我猜等一下出門一定會下大雨，怕被淋得濕答答的，所以決定還是帶一下傘比較保險。

    - 天空很暗，氣象說降雨機率高，所以我覺得還是帶傘。

  - **字數更多但評價接近**：
  
    - 我剛看了一下窗外，整個天空都變得很暗，雲層厚得幾乎看不到天空，甚至有些地方已經開始飄小雨。我仔細觀察了雲的顏色和形狀，發現雲層密集且低壓明顯，再加上我查看了氣象預報，今天降雨機率高達80%，整體天氣狀況非常不穩定。基於這些觀察，我推測等一下出門的時候大雨的可能性非常高。如果不帶傘，我很可能會被雨淋得濕答答，衣服鞋子都會弄濕，而且可能還會影響接下來的行程。因此，我判斷為了保險起見，還是帶傘出門比較穩妥。這樣既能應對突如其來的降雨，也讓我心理上更加踏實，不必擔心被雨打亂安排。

  **情境**：買早餐或自己做

  **選擇**：
  - A. 去外面買早餐
  - B. 在家自己做早餐
  
  **決策理由**：

  - **三項標準皆符合**：
    
    - 今天早上時間很趕，但又不想空腹上班，所以選擇快速又方便的便利商店三明治。
  
  - **資訊與信念/邏輯與策略較低**：
    
    - 因為不想空腹上班，所以選擇快速又方便的便利商店三明治。（未說明一定要快速方便的原因）

    - 今天早上時間很趕，不想空腹上班。便利商店三明治看起來不錯，所以我就買了。（未連結決定和資訊的關聯：便利商店三明治為何不錯？）

  **情境**：下課後去健身房或回家看劇

  **選擇**：
  - A. 去健身房
  - B. 回家看劇
  
  **決策理由**：

  - **三項標準皆符合**：

    - 雖然上一整天課很累，但如果今天再不運動，就快跟不上我的運動計畫了。另外，健身房的月費都已經付了，如果不去使用等於浪費錢。所以還是決定下課後去健身房運動。

    - 雖然上一整天課很累，但如果今天再不看劇，就快跟不上我的追劇計畫了。另外，串流平台的訂閱費都已經付了，如果不看等於浪費錢。所以還是決定下課後回家看劇。

**情境**：要不要熬夜讀書

**選擇**：
- A. 熬夜讀書
- B. 好好睡覺

- **三項標準皆符合**：

  - 明天有期中考，而我目前還有兩個章節沒讀。如果現在睡覺，明天早上很可能來不及複習。雖然熬夜很累，但至少能把重點看完，所以我決定先讀完再睡。

- **資訊與信念較低**：
  
  - 明天有期中考，而我目前還有兩個章節沒讀。雖然熬夜很累，但至少能把重點看完，所以我決定先讀完再睡。

- **邏輯與策略較低**：

  - 明天有期中考，而我目前還有兩個章節沒讀。如果現在睡覺，明天早上很可能來不及複習，所以我決定先讀完再睡。

- **具體程度較低**：

  - 明天有期中考，我覺得現在還需要再準備一下。雖然熬夜很累，但至少能把重點看完，所以我決定先讀完再睡。

- **字數較多但評價相近**：

  - 明天有期中考，而我目前還有兩個章節還沒讀完，進度其實有點落後。如果現在就直接去睡覺，明天早上能用來複習的時間應該會不夠，很可能來不及把這兩個章節的重點再看過一遍。雖然熬夜讀書一定會讓人覺得很累，精神也可能沒有那麼好，但至少還能把重要的內容先讀完、心裡比較有底。綜合考量時間與準備程度之後，我還是決定先把剩下的部分讀完，再去休息睡覺。


- **難以判斷的例子**：
  
  - 明天要考試，但其實也沒有特別多內容，只是覺得好像再看一下比較安心。雖然有點累，不過還是乾脆熬夜讀一下好了。

  -> gpt的判斷：
    
    - 資訊與信念：Participant 1 提供可觀察且具體的資訊與推論/Participant 2 偏向情緒與感受導向，資訊性較弱。-> Participant 1 較佳。
    
    - 邏輯與策略：兩者邏輯皆自洽，沒有違反現實或規則/Participant 1 的策略推導更明確。
      -> 此面向：Participant 1 較佳。

    - 具體程度：Participant 1 的具體程度明顯較高。
      -> Participant 1 較佳。