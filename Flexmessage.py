# -*- coding: utf-8 -*-
"""
Created on Tue May 26 13:02:30 2020

@author: zang
"""
from linebot.models import FlexSendMessage

def STOCK_BASIC(stockbasic,BASIC):
    #stockbasic處理
   color2 = "#00DB00"
   if float(stockbasic[5]) > 0:
       color2 = "#FF0000"
       diff ="+ " + str(stockbasic[5])
   #elif float(stockbasic[5]) < 0 :
    #   diff =" " + str(stockbasic[5])
       
   if stockbasic[6] == "-":
       Nnprice = "-"
   else :
       Nnprice = float(stockbasic[6])

   name = stockbasic[0]   
   latestprice = "最新: " + str(Nnprice)
   price = "開盤: " + str(stockbasic[1])
   hprice = "最高: " + str(stockbasic[2])
   lprice = "最低: " + str(stockbasic[3])
   time = stockbasic[4]
   volume = "交易數量: " + str(stockbasic[7])
   
   #stockStatements
   
   
   STOCK_BASIC = FlexSendMessage(alt_text=BASIC+"股票資訊", contents={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "url": "https://imgur.com/G8ENDN1.jpg"
      },
  "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "股票基本資訊"
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
            "type": "text",
            "text": name,
            "weight": "bold",
            "size": "xl",
            "position": "relative",
            "align": "start",
            "gravity": "center"
              },
              {
                "type": "text",
                "text": diff,
                "size": "xl",
                "color": color2,
                "weight": "bold",
                "position": "relative",
                "align": "center"
              }
            ]
          },
          {
        "type": "separator",
        "margin": "lg"
          },
 {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": latestprice,
                "color": "#0000C6",
                "weight": "bold",
                "size": "lg",
                "align": "start"
              },
              {
                "type": "text",
                "text": price,
                "weight": "bold",
                "size": "lg",
                "align": "start"
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": hprice,
                "weight": "bold",
                "size": "lg",
                "align": "start"
              },
              {
                "type": "text",
                "text": lprice,
                "weight": "bold",
                "size": "lg",
                "align": "start"
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": volume,
                "weight": "bold",
                "size": "lg",
                "align": "start"
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": time,
                "size": "md"
              }
            ]
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "postback",
              "label": "最近資訊",
              "data": "LatestNews="+BASIC
            }
          },
          {
            "type": "button",
            "style": "primary",
            "action": {
              "type": "postback",
              "label": "三大法人資訊",
              "data": "ThreeInfo="+BASIC
            }
          }
        ]
      }
    }

  ]
}
)
   return STOCK_BASIC
