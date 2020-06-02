# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 15:52:04 2020

@author: zang
"""
import datetime
from io import StringIO
import pandas as pd


def Basic_Stock2(stock):
    global  timeS
    #先設定要爬的時間
    timeS = datetime.datetime.strftime(datetime.datetime.now(),'%Y%m%d') 
    url2 ='https://www.twse.com.tw/exchangeReport/BWIBBU?response=html&date='+timeS+'&stockNo='+str(stock) 
    geturl2=pd.read_html(url2,encoding='utf-8',header=1)
    df = pd.concat(geturl2)
    dfL = len(df)-1
    T = str(df.iloc[dfL][0])
    DY = str(df.iloc[dfL][1])
    PE = str(df.iloc[dfL][3])
    PBR = str(df.iloc[dfL][4])
    #時間 殖利率 本益比 股價淨值比
    DATA = [T,DY,PE,PBR]
    return DATA



#本益比(PE) 股票淨值(PBR) 現金殖利率
#本益比(Price-to-Earning Ratio ) 簡稱 PE 或 PER，顧名思義是「成本和獲利的比例」
#1. 何時需要用到本益比?
#>當你已經評估完一間公司的體質與成長性沒問題之後，
#>需要判斷價格是否貴或便宜，就可以使用這項指標。
#2. 本益比數字越小代表股價越便宜，你的投資可以越快回本
#3. 虧損或是獲利高低很不穩定的股票，不適合用本益比評價
#4. 正確的本益比計算應該使用「預估未來EPS」，但現實中我們大多是用「過去歷史EPS」
#5. 本益比的高低本身也反映了人們對未來的預期 (反映在股價高低)
#>觀察一間公司股價高低,可以參考它自身歷史的本益比，以及同業的本益比
#一般你會在書上看到本益比的判斷標準如下：
#>較貴: 本益比高於20算貴 (報酬率低於5%)
#>接受: 本益比在15左右算可接受 (報酬率6.6%)
#>便宜: 本益比低於12算便宜 (報酬率8.3%以上)

#股票淨值比的英文叫做PBR(Price-Book Ratio)，股價淨值比帶你看出一間公司的真實價值，
#1. 因此要怎麼運用股價淨值比呢？最簡單的想法就是：
#>股價淨值比<1時，代表現在比較便宜，可以考慮買進；
#>股價淨值比>1時，代表現在比較昂貴，可以考慮賣出。
#2. 運用『股價淨值比』來進行投資時，一定要先了解股票過去的表現，以及相同產業的表現，了解相對關係後，才能活用指標，旗開得勝！

#現金殖利率(英文 Dividend yield)，簡稱殖利率。
#它代表投資股票時，現金股利與當下股價的比率，是把投資股票當成領利息的報酬率概念。
#1. 殖利率就是把一筆錢長期投入股市，每年能拿回的利息
#2. 在台灣大多數人喜歡高配息、穩定配息，其實配息穩定不代表企業穩定，只代表人們對企業不信任
#3. 殖利率不是高就好，要小心賺了股利賠了本金、一次性的高配息、用增資配息的情況
#4. 至少要殖利率高於4%才算比較理想的數字。

#目標找出 本益比(PE)<=15 股票淨值(PBR)<1 現金殖利率>=4