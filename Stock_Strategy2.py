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
    #先設定要爬的時間
    timeS = datetime.datetime.strftime(datetime.datetime.now(),'%Y%m%d') 
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
    


def Basic_Stock(stock):
    url = 'https://tw.stock.yahoo.com/q/q?s=' + str(stock) 
    list_req = requests.get(url)
    soup = BeautifulSoup(list_req.content, "html.parser")
    Basic = {}
    for i in range(0,10,1):
        Basic[i] = soup.find_all('td', {'bgcolor':"#FFFfff"})[i].text
    T = Basic[0]
    OP = Basic[2]
    CP =Basic[3]
    x = Basic[4].split("\n", 1)
    Diff = x[0]
    S = Basic[7]
    TOP = Basic[8]
    BOT = Basic[9]
    Word = '時間: '+ T +'\n買進: '+OP+'\n賣出: '+CP+'\n漲跌價差: '+Diff + '\n開盤: '+S + '\n最高: '+TOP + '\n最低: '+BOT
    return Word

def Price_Stock2(stock):
    url = 'https://tw.stock.yahoo.com/q/q?s=' + str(stock) 
    list_req = requests.get(url)
    soup = BeautifulSoup(list_req.content, "html.parser")
    Basic = {}
    for i in range(0,10,1):
        Basic[i] = soup.find_all('td', {'bgcolor':"#FFFfff"})[i].text
    T = Basic[0]
    OP = Basic[2]
    CP =Basic[3]
    x = Basic[4].split("\n", 1)
    Diff = x[0].replace('▽', '-').replace('△', '')
    S = Basic[7]
    TOP = Basic[8]
    BOT = Basic[9]
    Word = '時間: '+ T +'\n買進: '+OP+'\n賣出: '+CP+'\n漲跌價差: '+Diff + '\n開盤: '+S + '\n最高: '+TOP + '\n最低: '+BOT
    return Diff

