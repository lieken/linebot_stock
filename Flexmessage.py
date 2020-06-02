# -*- coding: utf-8 -*-
"""
Created on Tue May 26 13:02:30 2020

@author: zang
"""
from linebot.models import FlexSendMessage
a = 50
def STOCK_BASIC(stockbasic,stockStatements):
    
    
    #stockbasic處理
   color2 = "#00DB00"
   if float(stockbasic[5]) > 0:
       color2 = "#FF0000"
       diff ="+ " + str(stockbasic[5])
   elif float(stockbasic[5]) < 0 :
       color2 = "#00DB00"
       diff =" " + str(stockbasic[5])
       
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
   
   
   STOCK_BASIC = FlexSendMessage(alt_text="hello", contents={
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
              "data": " LatestNews"
            }
          },
          {
            "type": "button",
            "style": "primary",
            "action": {
              "type": "postback",
              "label": "三大法人資訊",
              "data": " ThreeInfo"
            }
          }
        ]
      }
    },
{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "財務報表",
        "weight": "bold",
        "color": "#1DB446",
        "size": "sm"
      },
      {
        "type": "text",
        "text": "2019 年度報表",
        "weight": "bold",
        "size": "xxl"
      },
      {
        "type": "separator",
        "margin": "xs"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "資產負債表",
            "size": "md",
            "color": "#aaaaaa",

          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "資產總計",
                "size": "sm",
                "color": "#555555",
                "flex": 0
              },
              {
                "type": "text",
                "text": str(int(stockStatements[0][1]))+ " 元",
                "size": "sm",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "負債總計",
                "size": "sm",
                "color": "#555555",
                "flex": 0
              },
              {
                "type": "text",
                "text": str(int(stockStatements[0][2]))+ " 元",
                "size": "sm",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "權益總計",
                "size": "sm",
                "color": "#555555",
                "flex": 0
              },
              {
                "type": "text",
                "text": str(int(stockStatements[0][3]))+ " 元",
                "size": "sm",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "separator",
            "margin": "xs"
          }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "綜合損益表",
            "size": "md",
            "color": "#aaaaaa",

          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "本期淨值",
                "size": "sm",
                "color": "#555555",
                "flex": 0
              },
              {
                "type": "text",
                "text": str(int(stockStatements[1][1]))+ " 元",
                "size": "sm",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "營業成本合計",
                "size": "sm",
                "color": "#555555",
                "flex": 0
              },
              {
                "type": "text",
                "text": str(int(stockStatements[1][2]))+ " 元",
                "size": "sm",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "營業毛利",
                "size": "sm",
                "color": "#555555",
                "flex": 0
              },
              {
                "type": "text",
                "text": str(int(stockStatements[1][3]))+ " 元",
                "size": "sm",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "營業費用合計",
                "size": "sm",
                "color": "#555555",
                "flex": 0
              },
              {
                "type": "text",
                "text": str(int(stockStatements[1][4]))+ " 元",
                "size": "sm",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "營業外收支合計",
                "size": "sm",
                "color": "#555555",
                "flex": 0
              },
              {
                "type": "text",
                "text": str(int(stockStatements[1][5]))+ " 元",
                "size": "sm",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "營業利益",
                "size": "sm",
                "color": "#555555",
                "flex": 0
              },
              {
                "type": "text",
                "text": str(int(stockStatements[1][6]))+ " 元",
                "size": "sm",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "每股盈餘 EPS",
                "size": "sm",
                "color": "#555555",
                "flex": 0
              },
              {
                "type": "text",
                "text": str(float(stockStatements[1][7]))+ " 元",
                "size": "sm",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "separator",
            "margin": "xs"
          }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "現金流量表",
            "size": "md",
            "color": "#aaaaaa",

          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "營業活動之淨現金",
                "size": "sm",
                "color": "#555555",
                "flex": 0
              },
              {
                "type": "text",
                "text": str(int(stockStatements[2][1]))+ " 元",
                "size": "sm",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "投資活動之淨現金",
                "size": "sm",
                "color": "#555555",
                "flex": 0
              },
              {
                "type": "text",
                "text": str(int(stockStatements[2][2]))+ " 元",
                "size": "sm",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "籌資活動之淨現金",
                "size": "sm",
                "color": "#555555",
                "flex": 0
              },
              {
                "type": "text",
                "text": str(int(stockStatements[2][3]))+ " 元",
                "size": "sm",
                "color": "#111111",
                "align": "end"
              }
            ]
          }
        ]
      }
    ]
  },
  "styles": {
    "footer": {

    }
  }
}
            
            
            
            
  ]
}
)
   return STOCK_BASIC