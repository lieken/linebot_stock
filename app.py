from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
from linebot.models import TemplateSendMessage, ButtonsTemplate, PostbackTemplateAction, MessageTemplateAction, URITemplateAction,PostbackEvent


import mongodb

import re

app = Flask(__name__)

line_bot_api = LineBotApi('/u+KR9NmRg9UVRk8NWvx578eKypyJUOaXrSltxJaKtY7hHTIM/UY5Nj9jm1vNNbsODDCxVM6HPftyh9oyTL/oFBuBtBI5cS3j/lWsfaWBu1Ea7OclWBxJnWWk10XyMogmtsyYvX60c9RFwSyRlLCwwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('3a3ec40cb756d1640f70aa711372e431')
line_bot_api.push_message('U1d4e838208d0f278714d687538a07600', TextSendMessage(text='-股票小助手已開始運作-'))
usespeak  = ""
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
    global  usespeak
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
        button_template_message =ButtonsTemplate(
                            title='Menu', 
                            text='Please select',
                            actions=[
                                PostbackTemplateAction(
                                    label='Postback: 測試data和文字', 
                                    data='buy',
                                    text='123'
                                ),
                                MessageTemplateAction(
                                    label='Message: 測試文字', text='message text'
                                ),
                                URITemplateAction(
                                    label='Uri: 可回傳網址', uri='http://www.google.com'
                                ),
                                PostbackTemplateAction(
                                    label='基本資料', 
                                    data='basic'
                                )                                        
                            ]
                        )
        line_bot_api.push_message(uid, TemplateSendMessage(alt_text="Template Example", template=button_template_message))
        return 0

    elif usespeak == '123':
        line_bot_api.push_message(uid, TextSendMessage('Text : 測試編號 '+ usespeak+' 已被觸發'))
        return 0
    

# 處理按下按鈕後的postback
@handler.add(PostbackEvent)
def handle_postback(event):
    # 注意!! 這裡的event.message是取不到text的
    data = event.postback.data
    if data == "buy":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='Data : Buy 代碼測試成功'))
    elif data == "basic":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='Data : basic 代碼測試成功'+ usespeak))
    

    
if __name__ == '__main__':
    app.run(debug=True)
