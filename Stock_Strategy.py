import requests
from bs4 import BeautifulSoup
import datetime
# -*- coding: utf-8 -*-
from pymongo import MongoClient
from datetime import date


today = str(date.today())
timeS = datetime.datetime.strftime(datetime.datetime.now(),'%Y%m%d')

def Price_Stock(stock):
    url = 'https://tw.stock.yahoo.com/q/q?s=' + str(stock) 
    list_req = requests.get(url)
    soup = BeautifulSoup(list_req.content, "html.parser")
    Basic = {}
    for i in range(0,10,1):
        Basic[i] = soup.find_all('td', {'bgcolor':"#FFFfff"})[i].text
    #T = Basic[0]
    #OP = Basic[2]
    #CP =Basic[3]
    x = Basic[4].split("\n", 1)
    Diff = x[0].replace('▽', '-').replace('△', '')
    #S = Basic[7]
    #TOP = Basic[8]
    #BOT = Basic[9]
    #Word = '時間: '+ T +'\n買進: '+OP+'\n賣出: '+CP+'\n漲跌價差: '+Diff + '\n開盤: '+S + '\n最高: '+TOP + '\n最低: '+BOT
    return Diff

Authdb='linebot_stock'
##### 資料庫連接 #####
def constructor():
    client = MongoClient('mongodb://kikp2929:kik759136@stockfree-shard-00-00-vskh2.azure.mongodb.net:27017,stockfree-shard-00-01-vskh2.azure.mongodb.net:27017,stockfree-shard-00-02-vskh2.azure.mongodb.net:27017/test?ssl=true&replicaSet=stockfree-shard-0&authSource=admin&retryWrites=true&w=majority')
    db = client[Authdb]
    return db
#----------------------------秀出基本股票數值的圖片--------------------------
def show_user_BasicStock_fountion(stock):  
    db=constructor()
    collect = db['BasicStock_StockImages']
    cel=list(collect.find({ "stock": int(stock), "date": today}))
    URL= {}
    for i in range(0,2,1):
        URL[i]=cel[i]['url']
    return URL