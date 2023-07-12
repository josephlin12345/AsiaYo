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

`{ 'msg': '不支援的target幣別' }` => 參數target幣別不在source對應匯率清單中

`{ 'msg': 'amount格式須為(幣別符號)+金額' }` => 參數amount格式只能是(幣別符號)+可以包含逗號的金額

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
    
    ----------------------------------------------------------------------
    Ran 6 tests in 0.007s
    
    OK
