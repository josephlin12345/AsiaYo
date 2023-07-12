# API說明

**環境:**

python 3.6或以上

**執行步驟:**

以下所有步驟指令均在資料夾下執行

* step 1:

  安裝需要的套件

      pip install - r requirements.txt

* step 2:

  啟動api，啟動後會在localhost的port 5000執行

      python api.py

**範例GET:**

匯率轉換api的endpoint在/api/convert

    GET http://localhost:5000/api/convert?source=USD&target=JPY&amount=$1,525
    
    回傳 {'msg': 'success', 'amount': '$170,496.52'}

**異常回傳說明:**

 `{ 'msg': '不支援的source幣別' }` => 參數source幣別不在匯率清單中

`{ 'msg': '不支援的target幣別' }` => 參數target幣別不在匯率清單中

`{ 'msg': 'amount不能為空' }` => 參數amount為空字串

`{ 'msg': '無法將amount正確轉換成float數值' }` => 參數amount除了幣別符號以外有不是逗號或數字的字元

# 單元測試說明

**環境:**

同API環境

**執行:**

以下指令在資料夾下執行

    python test_api.py

**範例輸出:**

    test_convert1 (__main__.TestApi) ... ok
    test_convert2 (__main__.TestApi) ... ok
    test_convert3 (__main__.TestApi) ... ok
    test_convert4 (__main__.TestApi) ... ok
    test_convert5 (__main__.TestApi) ... ok
    test_convert6 (__main__.TestApi) ... ok
    test_convert7 (__main__.TestApi) ... ok
    
    ----------------------------------------------------------------------
    Ran 7 tests in 0.007s
    
    OK
