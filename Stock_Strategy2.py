
import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime

timeS = datetime.datetime.strftime(datetime.datetime.now(),'%Y%m%d')


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
    #Word = '時間: '+ T +'\n開盤價: '+OP+'\n收盤價: '+CP+'\n漲跌價差: '+Diff+'\n交易數量: '+Tv
    Word = Tv
    return Word
    



