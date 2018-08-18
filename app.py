# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 01:00:17 2018

@author: linzino
"""


from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('+H5p42N7WpMATH0EEdqEluucdrnPzToVeyGQlZUig1pPkLKzslY1cr5oLP4oNdr0UrjF/Zy39eYmz33kelHXF35OJ4Vljc+o2wnE14Bk0e4NFfddu0UvzzjP+sJHJL8Mn+Bd9N5bL7dC8Epx6dtP8wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('5c6f3a03138a4a6ee6e39ad41e0d00ea')



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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
 

if __name__ == '__main__':
    app.run(debug=True)