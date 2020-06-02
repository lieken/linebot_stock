# -*- coding: utf-8 -*-
from pymongo import MongoClient
import urllib.parse
import datetime
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
import Stock_Data2

today = str(date.today())
###############################################################################
#                       股票機器人 Python基礎教學 【pymongo教學】                      #
###############################################################################

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
#----------------------------秀出基本股票數值的圖片--------------------------
def show_user_BasicStock_fountion(stock):  
    db=constructor()
    collect = db['BasicStock_StockImages']
    cel=list(collect.find({ "stock": int(stock), "date": today}))
    URL= {}
    for i in range(0,2,1):
        URL[i]=cel[i]['url']
    return URL
#----------------------------股票處理--------------------------------
def Name_Stock(stock):
    url = 'https://tw.stock.yahoo.com/q/q?s=' + str(stock) 
    list_req = requests.get(url)
    soup = BeautifulSoup(list_req.content, "html.parser")
    StockN='/q/bc?s='+str(stock) 
    StockName = soup.find('a', {'href':StockN}).text
    return StockName

#----------------------------儲存三大法人的圖片--------------------------
def Save_ThreeStock_fountion(stock, url):  
    db=constructor()
    collect = db['ThreeStock_StockImages']
    collect.remove({"stock": int(stock)})
    collect.insert({"stock": int(stock),
                    "url": url,
                    "data_info": "Three_Stock",
                    "date": today
                    })

#----------------------------儲存基本股票數值的圖片--------------------------
    stock = 2002
def Save_BasicStock_fountion(stock, url):  
    db=constructor()
    basicstock = Stock_Data2.Basic_Stock2(stock)
    collect = db['BasicStock_StockImages']
    collect.remove({"stock": int(stock)})
    collect.insert({"stock": int(stock),
                    "url": url[0],
                    "data_info": "BasicStock1",
                    "date": today
                    })
    collect.insert({"stock": int(stock),
                    "url": url[1],
                    "data_info": "BasicStock2",
                    "date": today
                    })
    collect = db['BasicStock']
    collect.remove({"stock": stock})
    #時間 殖利率 本益比 股價淨值比
    collect.insert({"stock": int(stock),
                    "DY": basicstock[1],
                    "PE": basicstock[2],
                    "PBR": basicstock[3],
                    "date": basicstock[0]
                    })


def delete_user_Stockfountion(stock):  
    db=constructor()
    collect = db['BasicStock_StockImages']
    collect.remove({"stock": stock})
    collect = db['ThreeStock_StockImages']
    collect.remove({"stock": stock})
    
