#from flask import Flask, request, abort

#from linebot import (
#    LineBotApi, WebhookHandler
#)
#from linebot.exceptions import (
#    InvalidSignatureError
#)
#from linebot.models import (
#    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
#)

#from googletrans import Translator

#app = Flask(__name__)

#from config import * 

#line_bot_api = LineBotApi(channel_access_token)
#handler = WebhookHandler(channel_secret)


##@app.route("/callback", methods=['POST'])
#@app.route("/", methods=["GET", "POST"])
#def callback():
#    # get X-Line-Signature header value
#    signature = request.headers['X-Line-Signature']

#    # get request body as text
#    body = request.get_data(as_text=True)
#    app.logger.info("Request body: " + body)

#    # handle webhook body
#    try:
#        handler.handle(body, signature)
#    except InvalidSignatureError:
#        print("Invalid signature. Please check your channel access token/channel secret.")
#        abort(400)

#    return 'OK'

#def translate_text(text,dest='en'):
#    """�Hgoogle½Ķ�Ntext½Ķ���ؼлy��

#    :param text: �n½Ķ���r��A����UTF-8�s�X�C
#    :param dest: �n½Ķ���ؼлy���A�Ѿ\googletrans.LANGCODES�y���C��C
#    """
#    translator = Translator()
#    result = translator.translate(text, dest).text
#    return result

#import mplfinance as mpf
#import yfinance as yf
## import pandas_datareader.data as web
#import pyimgur

#IMGUR_CLIENT_ID = imgur_client_id

#def plot_stcok_k_chart(IMGUR_CLIENT_ID,stock="0050" , date_from='2020-01-01' ):
#    """
#    �i��Ӫ�K�uø�s�A�^�Ǧܩ󶳺ݹϧɪ��s���C�N��ܥ]�t5MA�B20MA�ζq�����Y�A�_�l�w�]��2020-01-01�_���Q�馬�L���C
#    :stock :�ӪѥN�X(�r��)�A�w�]0050�C
#    :date_from :�_�l��(�r��)�A�榡��YYYY-MM-DD�A�w�]��2020-01-01�_�C
#    """
#    stock = str(stock)+".tw"
#    # df = web.DataReader(stock, 'yahoo', date_from) 
#    df = yf.download(stock, date_from) 
#    mpf.plot(df,type='candle',mav=(5,20),volume=True, ylabel=stock.upper()+' Price' ,savefig='testsave.png')
#    PATH = "testsave.png"
#    im = pyimgur.Imgur(IMGUR_CLIENT_ID)
#    uploaded_image = im.upload_image(PATH, title=stock+" candlestick chart")
#    return uploaded_image.link

#@handler.add(MessageEvent, message=TextMessage)
#def handle_message(event):
#    if event.source.user_id =='Udeadbeefdeadbeefdeadbeefdeadbeef':
#        return 'OK'
#    if event.message.text[:3] == "@½�^":
#        content = translate_text(event.message.text[3:], "en")
#        message = TextSendMessage(text=content)
#        line_bot_api.reply_message(event.reply_token, message)
#    if event.message.text[:3] == "@½��":
#        content = translate_text(event.message.text[3:] , "ja")
#        message = TextSendMessage(text=content)
#        line_bot_api.reply_message(event.reply_token, message)
#    if event.message.text[:3] == "@½��":
#        content = translate_text(event.message.text[3:] , "zh-tw")
#        message = TextSendMessage(text=content)
#        line_bot_api.reply_message(event.reply_token, message)
#    if event.message.text[:2].upper() == "@K":
#        input_word = event.message.text.replace(" ","") #�X�֦r������ť�
#        stock_name = input_word[2:6] #2330
#        start_date = input_word[6:] #2020-01-01
#        content = plot_stcok_k_chart(IMGUR_CLIENT_ID,stock_name,start_date)
#        message = ImageSendMessage(original_content_url=content,preview_image_url=content)
#        line_bot_api.reply_message(event.reply_token, message)

#    else: line_bot_api.reply_message(event.reply_token,
#                                     TextSendMessage(text=event.message.text))


#if __name__ == "__main__":
#    app.run()

#line bot echo -- run ok
import os
from datetime import datetime

from flask import Flask, abort, request

# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
#from googletrans import Translator

app = Flask(__name__)

from config import * 

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)


@app.route("/", methods=["GET", "POST"])
def callback():

    if request.method == "GET":
        return "Hello Heroku"
    if request.method == "POST":
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)

        return "OK"

#def translate_text(text,dest='en'):
#    """�Hgoogle½Ķ�Ntext½Ķ���ؼлy��

#    :param text: �n½Ķ���r��A����UTF-8�s�X�C
#    :param dest: �n½Ķ���ؼлy���A�Ѿ\googletrans.LANGCODES�y���C��C
#    """
#    translator = Translator()
#    result = translator.translate(text, dest).text
#    return result


#@handler.add(MessageEvent, message=TextMessage)
#def handle_message(event):
#    get_message = event.message.text

#    # Send To Line
#    reply = TextSendMessage(text=f"{get_message}")
#    line_bot_api.reply_message(event.reply_token, reply)

IMGUR_CLIENT_ID = imgur_client_id

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.source.user_id =='Udeadbeefdeadbeefdeadbeefdeadbeef':
        return 'OK'
    #if event.message.text[:3] == "@½�^":
    #    #content = translate_text(event.message.text[3:], "en")
    #    message = TextSendMessage(text=event.message.text[3:])
    #    line_bot_api.reply_message(event.reply_token, message)
    #if event.message.text[:3] == "@½��":
    #    content = translate_text(event.message.text[3:] , "ja")
    #    message = TextSendMessage(text=content)
    #    line_bot_api.reply_message(event.reply_token, message)
    #if event.message.text[:3] == "@½��":
    #    content = translate_text(event.message.text[3:] , "zh-tw")
    #    message = TextSendMessage(text=content)
    #    line_bot_api.reply_message(event.reply_token, message)
    #if event.message.text[:2].upper() == "@K":
    #    input_word = event.message.text.replace(" ","") #�X�֦r������ť�
    #    stock_name = input_word[2:6] #2330
    #    start_date = input_word[6:] #2020-01-01
    #    content = plot_stcok_k_chart(IMGUR_CLIENT_ID,stock_name,start_date)
    #    message = ImageSendMessage(original_content_url=content,preview_image_url=content)
    #    line_bot_api.reply_message(event.reply_token, message)

    else: line_bot_api.reply_message(event.reply_token,
                                     TextSendMessage(text=event.message.text))

#@handler.add(MessageEvent, message=TextMessage)
#def handle_message(event):
#    if event.source.user_id =='Udeadbeefdeadbeefdeadbeefdeadbeef':
#        return 'OK'
#    if event.message.text[:3] == "@½�^":
#        content = translate_text(event.message.text[3:], "en")
#        message = TextSendMessage(text=content)
#        line_bot_api.reply_message(event.reply_token, message)
#    if event.message.text[:3] == "@½��":
#        content = translate_text(event.message.text[3:] , "ja")
#        message = TextSendMessage(text=content)
#        line_bot_api.reply_message(event.reply_token, message)
#    if event.message.text[:3] == "@½��":
#        content = translate_text(event.message.text[3:] , "zh-tw")
#        message = TextSendMessage(text=content)
#        line_bot_api.reply_message(event.reply_token, message)
#    if event.message.text[:2].upper() == "@K":
#        input_word = event.message.text.replace(" ","") #�X�֦r������ť�
#        stock_name = input_word[2:6] #2330
#        start_date = input_word[6:] #2020-01-01
#        content = plot_stcok_k_chart(IMGUR_CLIENT_ID,stock_name,start_date)
#        message = ImageSendMessage(original_content_url=content,preview_image_url=content)
#        line_bot_api.reply_message(event.reply_token, message)

#    else: line_bot_api.reply_message(event.reply_token,
#                                     TextSendMessage(text=event.message.text))