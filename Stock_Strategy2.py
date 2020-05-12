# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 12:18:38 2020

@author: zang
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime

###股票的名字
#stock='2002'
#要抓取的網址
#url = 'https://tw.stock.yahoo.com/q/q?s=' + stock 
#請求網站
#list_req = requests.get(url)
#將整個網站的程式碼爬下來
#soup = BeautifulSoup(list_req.content, "html.parser")
#股票的名字
#StockN='/q/bc?s='+stock
#soup.find('a', {'href':StockN}).text
timeS = datetime.datetime.strftime(datetime.datetime.now(),'%Y%m%d')

##股票的漲幅交易量
stock='2002'
url2 ='https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date='+timeS+'&stockNo='+stock
geturl2=pd.read_html(url2,encoding='utf-8',header=1)
df = pd.concat(geturl2)
dfL = len(df)-1
#時間開盤收盤價差買賣量
T = df.iloc[dfL][0]
OP = df.iloc[dfL][3]    
CP = df.iloc[dfL][6]
Diff = df.iloc[dfL][7]
Tv = df.iloc[dfL][8]


def Name_Stock(stock):
    url = 'https://tw.stock.yahoo.com/q/q?s=' + str(stock) 
    list_req = requests.get(url)
    soup = BeautifulSoup(list_req.content, "html.parser")
    StockN='/q/bc?s='+str(stock) 
    StockName = soup.find('a', {'href':StockN}).text
    return StockName


def Price_Stock(stock):
    global  timeS
    timeS = datetime.datetime.strftime(datetime.datetime.now(),'%Y%m%d') #先設定要爬的時間
    url2 ='https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date='+timeS+'&stockNo='+str(stock) 
    geturl2=pd.read_html(url2,encoding='utf-8',header=1)
    df = pd.concat(geturl2)
    dfL = len(df)-1
    T = str(df.iloc[dfL][0])
    OP = str(df.iloc[dfL][3])
    CP = str(df.iloc[dfL][6])
    Diff = str(df.iloc[dfL][7])
    Tv = str(df.iloc[dfL][8])
    Word = '時間: '+ T +'\n開盤價: '+OP+'\n收盤價: '+CP+'\n漲跌價差: '+Diff+'\n交易數量: '+Tv
    return Word
    



