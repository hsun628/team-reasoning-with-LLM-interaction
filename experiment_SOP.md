## 實驗前
和曉芳姐確認可以跑實驗的時間+找小幫手
確認後和老師確認點錢時間(實驗前、後皆須確認)

註：如錢箱零錢不夠，原則上是到公館台灣銀行換幣

### step1 Tassel網站開心實驗+寄送邀請

主電腦密碼：tassel

https://www.tassel.econ.ntu.edu.tw/admin/

複製一場剛結束的實驗 -> 我的實驗 -> 指派對象 -> 套用先前儲存的查詢條件 -> 搜尋與檢視-> 全選 -> 去除學號t開頭受試者 -> assign only selected participants -> 此實驗主頁-> 寄送邀請Email -> 記得每天確認報名人數

註1：查詢條件：受試者入學時間>2019 & 限台大學生 & 系統隨機選取300人
註2：寄太多信要到slack recruitment letter告知

## 實驗前30分鐘

### step1 印製空白受試者收據、實驗說明

D槽 -> 公用檔案 -> 紙本資料 -> 空白受試者收據
D槽 -> team_reasoning_p_beauty -> experiment_instruction -> experimental_instruction_new_design.pdf (影印前確認為雙面黑白)

### step2 印製受試者名單+拿錢箱給曉芳姐

實驗主頁 -> 已登記對象 -> 複製名單到excel列印 (額外準備外籍生空白收據)

D槽 -> 公用檔案 -> 紙本資料 -> 空白受試者收據

### step3 deploy???　(heroku步驟)

otree prodserver

### step4 播放投影片


## 實驗開始

### step1 


***

## 附錄：更改treatment設定or版本更新

### step1 本地修改 & 測試

修改程式碼 -> 本地存檔 & 測試(otree devserver)

### step2 heroku deploy

1. 開啟終端機 -> `cd C:\otree\otree_code`

2. 存入Git -> 
   
    `git add .`
    `git commit -m "treatment adjustment"`
    (commit message)

3. 推送到heroku -> `git push heroku main`
   
    (確認出現 `remote: Verifying deploy... done.`)

4. 同步資料庫(修改Constants或欄位時必要) 注意！ -> 
   
   `heroku run otree resetdb` (**這將刪除heroku上現有所有實驗數據！**)

### step3 實驗室受試者電腦設置

1. 取得實驗網址：終端機輸入`heroku open`

2. 建立session：