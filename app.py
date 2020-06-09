from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
from linebot.models import (
        MessageAction,QuickReply,TextSendMessage,QuickReplyButton,
        ImageSendMessage,PostbackAction
        
)
import re
import Stock_Strategy
import Flexmessage
from twstock import BestFourPoint,Stock
import twstock

app = Flask(__name__)

a = 1
line_bot_api = LineBotApi('/u+KR9NmRg9UVRk8NWvx578eKypyJUOaXrSltxJaKtY7hHTIM/UY5Nj9jm1vNNbsODDCxVM6HPftyh9oyTL/oFBuBtBI5cS3j/lWsfaWBu1Ea7OclWBxJnWWk10XyMogmtsyYvX60c9RFwSyRlLCwwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('3a3ec40cb756d1640f70aa711372e431')
line_bot_api.push_message('U1d4e838208d0f278714d687538a07600', TextSendMessage(text='請輸入股票代號'))



# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

#訊息傳遞區塊
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    ### 抓到顧客的資料 ###
    profile = line_bot_api.get_profile(event.source.user_id)
    uid = profile.user_id #使用者ID
    usespeak=str(event.message.text) #使用者講的話
    #usespeak = "2002"
    if re.match('[0-9]{4}',usespeak):
        if re.match('00[0-9]{2}',usespeak):
            line_bot_api.push_message(uid, TextSendMessage(text='您輸入的並不是上市公司股票號碼'))
                
        elif usespeak in twstock.twse :
            #資料處理
            stock = twstock.realtime.get(usespeak)
            stockbasic = [stock["info"]["code"] +" " + stock["info"]["name"],
                          float(stock["realtime"]["open"]),
                          float(stock["realtime"]["high"]),
                          float(stock["realtime"]["low"]),
                          stock["info"]["time"],
                          Stock_Strategy.Price_Stock(str(usespeak)),
                          stock["realtime"]["latest_trade_price"],
                          stock["realtime"]["trade_volume"]
                          ]
            stockanalytics = Stock_Strategy.show_user_stockanalytics(usespeak)
            stockimage = Stock_Strategy.show_user_BasicStock_fountion(usespeak)[0]

            Flex_message = Flexmessage.STOCK_BASIC(stockbasic,stockanalytics,str(usespeak),stockimage)
        
            line_bot_api.push_message(uid,Flex_message)
            return 0
        else :
            line_bot_api.push_message(uid, TextSendMessage(text='您輸入的並不是上市股票號碼'))
    
    elif re.match('技術面 [0-9]{4} 資料',usespeak):
        stock = Stock(usespeak[4:8])
        bfp = BestFourPoint(stock)
        stock = list(bfp.best_four_point())           # 綜合判斷
        if stock[0] :
            Text_linebot = stock[1]
            line_bot_api.push_message(uid, TextSendMessage(text='符合四大買進點:\n'+Text_linebot+'\n建議符合兩大買進點再進行購買'))  
        else :
            Text_linebot = stock[1]
            line_bot_api.push_message(uid, TextSendMessage(text='符合四大賣出點:\n'+Text_linebot+'\n建議符合兩大賣出點再進行賣出'))  
            
        QuickReply_text_message = TextSendMessage(
                text = '搭配其他圖',
                quick_reply = QuickReply(
                        items = [
                                QuickReplyButton(
                                        action = PostbackAction(label = "K線圖",data = "CandlestickChart="+usespeak[4:8])
                                        ),
                                QuickReplyButton(
                                        action = PostbackAction(label = "均線圖(短期)",data = "MovingAverage="+usespeak[4:8])
                                        )
                                ]
        )
    )
        line_bot_api.push_message(uid,QuickReply_text_message)            
       
    elif re.match('三大法人 [0-9]{4} 資料',usespeak):
       stock = usespeak[5:9]
       picture = Stock_Strategy.show_user_ThreeStock_StockImages(stock)
       line_bot_api.push_message(uid, ImageSendMessage(original_content_url=picture, preview_image_url=picture))   
        
    else :
        if a==1:
            line_bot_api.push_message(uid, TextSendMessage(text='您輸入的並不是股票號碼'))


# 處理postback
@handler.add(PostbackEvent)
def handle_postback(event):
    profile = line_bot_api.get_profile(event.source.user_id)
    uid = profile.user_id #使用者ID
    # 注意!! 這裡的event.message是取不到text的
    data = event.postback.data
    x = data.split("=", 1)

    global a

    if data == "buy":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='Data : Buy 代碼測試成功'))
        #'Data : basic 代碼測試成功\n股票號碼為 : '+ x[1] + '\n\n' + 
    elif x[0] == "MoreNews":
        a=0
        QuickReply_text_message = TextSendMessage(
                text = '你想要什麼方面資訊呢',
                quick_reply = QuickReply(
                        items = [
                                QuickReplyButton(
                                        action = MessageAction(label = "技術面分析", text = '技術面 '+x[1]+' 資料')
                                        ),
                                QuickReplyButton(
                                        action = MessageAction(label = "三大法人", text = '三大法人 '+x[1]+' 資料')
                                        )
                                ]
        )
    )
        line_bot_api.push_message(uid,QuickReply_text_message)
    elif x[0] == 'CandlestickChart':
        stock = x[1]
        picture = Stock_Strategy.show_user_CandlestickChart_StockImages(stock)
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=picture, preview_image_url=picture))
        
    elif x[0] == 'MovingAverage':
        stock = x[1]
        picture = Stock_Strategy.show_user_MovingAverage_StockImages(stock)
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=picture, preview_image_url=picture))
        
if __name__ == '__main__':
    app.run(debug=True)
