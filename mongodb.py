# -*- coding: utf-8 -*-
from pymongo import MongoClient
import urllib.parse
import datetime
import requests
from bs4 import BeautifulSoup
import pandas as pd



# Authentication Database認證資料庫
Authdb='linebot_stock'

##### 資料庫連接 #####
def constructor():
    client = MongoClient('mongodb://kikp2929:kik759136@stockfree-shard-00-00-vskh2.azure.mongodb.net:27017,stockfree-shard-00-01-vskh2.azure.mongodb.net:27017,stockfree-shard-00-02-vskh2.azure.mongodb.net:27017/test?ssl=true&replicaSet=stockfree-shard-0&authSource=admin&retryWrites=true&w=majority')
    db = client[Authdb]
    return db
   
#----------------------------儲存使用者的股票--------------------------
def write_user_stock_fountion(stock, bs, price):  
    db=constructor()
    collect = db['mystock']
    collect.insert({"stock": stock,
                    "data": 'care_stock',
                    "bs": bs,
                    "price": float(price),
                    "date_info": datetime.datetime.utcnow()
                    })
    
#----------------------------殺掉使用者的股票--------------------------
def delete_user_stock_fountion(stock):  
    db=constructor()
    collect = db['mystock']
    collect.remove({"stock": stock})
    
#----------------------------秀出使用者的股票--------------------------
def show_user_stock_fountion():  
    db=constructor()
    collect = db['mystock']
    cel=list(collect.find({"data": 'care_stock'}))

    return cel


#----------------------------股票處理--------------------------------
def Name_Stock(stock):
    url = 'https://tw.stock.yahoo.com/q/q?s=' + str(stock) 
    list_req = requests.get(url)
    soup = BeautifulSoup(list_req.content, "html.parser")
    StockN='/q/bc?s='+str(stock) 
    StockName = soup.find('a', {'href':StockN}).text
    return StockName
