import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime

timeS = datetime.datetime.strftime(datetime.datetime.now(),'%Y%m%d')

def Price_Stock(stock):
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

