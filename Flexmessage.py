from linebot.models import FlexSendMessage
from datetime import date

def STOCK_BASIC(stockbasic,stock,number):
    #stockbasic處理
   color2 = "#00DB00"
   today = str(date.today())
   if float(stockbasic[5]) >= 0:
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
   time = today
   volume = "交易數量: " + str(stockbasic[7])
   
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
              "data": " LatestNews="+str(number)
            }
          },
          {
            "type": "button",
            "style": "primary",
            "action": {
              "type": "postback",
              "label": "三大法人資訊",
              "data": " ThreeInfo="
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
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "基本分析",
                "weight": "bold",
                "color": "#1DB446",
                "size": "xl"
              }
            ],
            "flex": 10
          }
        ]
      },
      {
        "type": "separator",
        "margin": "sm"
      },
      {
        "type": "text",
        "text": "穩定度",
        "size": "lg",
        "color": "#aaaaaa"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "ROA",
            "size": "lg",
            "color": "#555555",
            "flex": 3,
            "weight": "bold",
            "decoration": "none",
            "position": "relative",
            "align": "start",
            "gravity": "center"
          },
          {
            "type": "text",
            "text": str(stock["ROA"]+"%"),
            "size": "md",
            "color": "#111111",
            "align": "center",
            "gravity": "center",
            "flex": 2,
            "position": "relative"
          },
          {
            "type": "image",
            "url": "https://imgur.com/fV8ISrN.png",
            "aspectMode": "cover"
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "ROE",
            "size": "lg",
            "color": "#555555",
            "flex": 3,
            "weight": "bold",
            "decoration": "none",
            "position": "relative",
            "align": "start",
            "gravity": "center"
          },
          {
            "type": "text",
            "text": str(stock["ROE"]+"%"),
            "size": "md",
            "color": "#111111",
            "align": "center",
            "gravity": "center",
            "flex": 2,
            "position": "relative"
          },
          {
            "type": "image",
            "url": "https://imgur.com/pOcsIoX.png",
            "aspectMode": "cover"
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "現金流量 ",
            "size": "lg",
            "color": "#555555",
            "flex": 3,
            "weight": "bold",
            "decoration": "none",
            "position": "relative",
            "align": "start",
            "gravity": "center"
          },
          {
            "type": "text",
            "text": str(stock["money1"]+"%"),
            "size": "md",
            "color": "#111111",
            "align": "center",
            "gravity": "center",
            "flex": 2,
            "position": "relative"
          },
          {
            "type": "image",
            "url": "https://imgur.com/pOcsIoX.png",
            "aspectMode": "cover"
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "現金流量允當",
            "size": "lg",
            "color": "#555555",
            "flex": 3,
            "weight": "bold",
            "decoration": "none",
            "position": "relative",
            "align": "start",
            "gravity": "center"
          },
          {
            "type": "text",
            "text": str(stock["money2"]+"%"),
            "size": "md",
            "color": "#111111",
            "align": "center",
            "gravity": "center",
            "flex": 2,
            "position": "relative"
          },
          {
            "type": "image",
            "url": "https://imgur.com/pOcsIoX.png",
            "aspectMode": "cover"
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "現金再投資",
            "size": "lg",
            "color": "#555555",
            "flex": 3,
            "weight": "bold",
            "decoration": "none",
            "position": "relative",
            "align": "start",
            "gravity": "center"
          },
          {
            "type": "text",
            "text": str(stock["money3"]+"%"),
            "size": "md",
            "color": "#111111",
            "align": "center",
            "gravity": "center",
            "flex": 2,
            "position": "relative"
          },
          {
            "type": "image",
            "url": "https://imgur.com/pOcsIoX.png",
            "aspectMode": "cover"
          }
        ]
      },
      {
        "type": "separator",
        "margin": "sm"
      },
      {
        "type": "text",
        "text": "價值",
        "size": "lg",
        "color": "#aaaaaa"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "本益比",
            "size": "lg",
            "color": "#555555",
            "flex": 3,
            "weight": "bold",
            "decoration": "none",
            "position": "relative",
            "align": "start",
            "gravity": "center"
          },
          {
            "type": "text",
            "text": str(stock["PE"]+" 倍"),
            "size": "md",
            "color": "#111111",
            "align": "center",
            "gravity": "center",
            "flex": 2,
            "position": "relative"
          },
          {
            "type": "image",
            "url": "https://imgur.com/pOcsIoX.png",
            "aspectMode": "cover"
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "股價淨值比",
            "size": "lg",
            "color": "#555555",
            "flex": 3,
            "weight": "bold",
            "decoration": "none",
            "position": "relative",
            "align": "start",
            "gravity": "center"
          },
          {
            "type": "text",
            "text": str(stock["PBR"]+"%"),
            "size": "md",
            "color": "#111111",
            "align": "center",
            "gravity": "center",
            "flex": 2,
            "position": "relative"
          },
          {
            "type": "image",
            "url": "https://imgur.com/pOcsIoX.png",
            "aspectMode": "cover"
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "殖利率",
            "size": "lg",
            "color": "#555555",
            "flex": 3,
            "weight": "bold",
            "decoration": "none",
            "position": "relative",
            "align": "start",
            "gravity": "center"
          },
          {
            "type": "text",
            "text": str(stock["DY"]+" 倍"),
            "size": "md",
            "color": "#111111",
            "align": "center",
            "gravity": "center",
            "flex": 2,
            "position": "relative"
          },
          {
            "type": "image",
            "url": "https://imgur.com/pOcsIoX.png",
            "aspectMode": "cover"
          }
        ]
      },
      {
        "type": "separator",
        "margin": "xl"
      },
      {
        "type": "text",
        "text": "評比",
        "size": "lg",
        "color": "#aaaaaa",
        "weight": "bold"
      },
      {
        "type": "text",
        "text": stock["Appraisal"]+stock["Appraisal2"],
        "size": "lg",
        "color": "#555555",
        "flex": 3,
        "weight": "bold",
        "decoration": "underline",
        "position": "relative"
      }
    ]
  }
}
            
            
            
            
  ]
}
)
   return STOCK_BASIC
