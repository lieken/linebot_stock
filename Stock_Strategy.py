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
    x = Basic[4].split("\n", 1)
    Diff = x[0].replace('▽', '-').replace('△', '')
    return Diff



Authdb='linebot_stock'

##### 資料庫連接 #####
def constructor():
    client = MongoClient('mongodb://kikp2929:kik759136@stockfree-shard-00-00-vskh2.azure.mongodb.net:27017,stockfree-shard-00-01-vskh2.azure.mongodb.net:27017,stockfree-shard-00-02-vskh2.azure.mongodb.net:27017/test?ssl=true&replicaSet=stockfree-shard-0&authSource=admin&retryWrites=true&w=majority')
    db = client[Authdb]
    return db
##### 秀出基本股票數值的圖片 #####
def show_user_BasicStock_fountion(stock):  
    db=constructor()
    collect = db['BasicStock_image']
    cel=list(collect.find({ "stock": int(stock)}))
    return cel

#####秀出股票分析數值
def show_user_stockanalytics(stock):  
    db=constructor()
    collect = db['BasicStock2']
    cel=list(collect.find({ "stock": int(stock)}))[0]
    collect = db['BasicStock']
    cel2=list(collect.find({ "stock": int(stock)}))[0]
    cel.update(cel2)

    return cel



#####秀出三大法人圖片
def show_user_ThreeStock_StockImages(stock):  
    db=constructor()
    collect = db['ThreeStock_StockImages']
    cel=list(collect.find({ "stock": int(stock)}))[0]
    return cel['url']

#####K線圖圖片
def show_user_CandlestickChart_StockImages(stock):  
    db=constructor()
    collect = db['CandlestickChart_StockImages']
    cel=list(collect.find({ "stock": int(stock)}))[0]
    return cel['url']
#####均線圖片
def show_user_MovingAverage_StockImages(stock):  
    db=constructor()
    collect = db['MovingAverage_StockImages']
    cel=list(collect.find({ "stock": int(stock)}))[0]
    return cel['url']
