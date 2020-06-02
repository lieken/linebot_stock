from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
from linebot.models import (
        TemplateSendMessage,CarouselTemplate,
        CarouselColumn,PostbackAction,MessageAction,URIAction,FlexSendMessage,
        BubbleContainer,BoxComponent,ImageComponent,TextComponent,ImageSendMessage
)
import mongodb
import re
import Stock_Strategy2
import Flexmessage
import twstock
import Stock_statement
app = Flask(__name__)


line_bot_api = LineBotApi('/u+KR9NmRg9UVRk8NWvx578eKypyJUOaXrSltxJaKtY7hHTIM/UY5Nj9jm1vNNbsODDCxVM6HPftyh9oyTL/oFBuBtBI5cS3j/lWsfaWBu1Ea7OclWBxJnWWk10XyMogmtsyYvX60c9RFwSyRlLCwwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('3a3ec40cb756d1640f70aa711372e431')
line_bot_api.push_message('U1d4e838208d0f278714d687538a07600', TextSendMessage(text='-股票小助手已開始運作-'))



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
    
    
    if re.match('[0-9]{4}[<>][0-9]',usespeak): # 先判斷是否是使用者要用來存股票的
        StockCompany = mongodb.Name_Stock(usespeak[0:4])
        mongodb.write_user_stock_fountion(stock=usespeak[0:4], bs=usespeak[4:5], price=usespeak[5:])
        line_bot_api.push_message(uid, TextSendMessage(StockCompany+' :已經儲存成功'))
        return 0

    
    elif re.match('刪除[0-9]{4}',usespeak): # 刪除存在資料庫裡面的股票
        mongodb.delete_user_stock_fountion(stock=usespeak[2:])
        line_bot_api.push_message(uid, TextSendMessage(usespeak+'已經刪除成功'))
        return 0
    
    elif re.match('[0-9]{4}',usespeak):
        stock = twstock.realtime.get(str(usespeak))
        stockbasic = [stock["info"]["code"] +" " + stock["info"]["name"],
              float(stock["realtime"]["open"]),
              float(stock["realtime"]["high"]),
              float(stock["realtime"]["low"]),
              stock["info"]["time"],
              Stock_Strategy2.Price_Stock2(str(usespeak)),
              stock["realtime"]["latest_trade_price"],
              stock["realtime"]["trade_volume"]
              ]
        Statements = Stock_statement.FinancialStatements(str(usespeak))
        stockStatements = [Statements[0].loc[2019],Statements[1].loc[2019],
                   Statements[2].loc[2019] ]
        Flex_message = Flexmessage.STOCK_BASIC(stockbasic,stockStatements,str(usespeak))
        
        line_bot_api.push_message(uid,Flex_message)
        return 0

    elif usespeak == '123':
        line_bot_api.push_message(uid, TextSendMessage('Text : 測試編號 '+ usespeak+' 已被觸發'))
        return 0
    

# 處理按下按鈕後的postback
@handler.add(PostbackEvent)
def handle_postback(event):
    # 注意!! 這裡的event.message是取不到text的
    data = event.postback.data
    x = data.split("=", 1)
    image = mongodb.show_user_BasicStock_fountion(x[1])
    
    if data == "buy":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='Data : Buy 代碼測試成功'))
        #'Data : basic 代碼測試成功\n股票號碼為 : '+ x[1] + '\n\n' + 
    elif x[0] == "LatestNews":
            line_bot_api.push_message(event.reply_token,ImageSendMessage(original_content_url=image[0], preview_image_url=image[0]))
            line_bot_api.push_message(event.reply_token,ImageSendMessage(original_content_url=image[1], preview_image_url=image[1]))

    elif x[0] == "ThreeInfo":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url=image[0], preview_image_url=image[0]))
    elif x[0] == "BasicStock2":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url=image[1], preview_image_url=image[1]))
        
        
if __name__ == '__main__':
    app.run(debug=True)
