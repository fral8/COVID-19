import sys
import time
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import requests
import json
from pprint import pprint

def getDataFromJson(url):
    data = requests.get(url)
    jsonData = data.json()
    return jsonData

def json2dict(jsonData):
    pass

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text = 'Testuali',callback_data = 'textualData')],
            [InlineKeyboardButton(text = 'Grafiche',callback_data = 'Images')]])
        bot.sendMessage(chat_id, "ultime informazioni:", reply_markup = keyboard)

def on_callback_query(msg):
    # global query_id, from_id, query_data, decided
    query_id, from_id, query_data = telepot.glance(msg, flavor = 'callback_query')
    print('Callback query:',query_id, from_id, query_data)
    if query_data == "textualData":
        jsonData = getDataFromJson(bot.urlNationalData)
        msg_str = ""
        for key, value in jsonData[-1].items():
            msg_str += str(key) + ': ' + str(value) +'\n'
        bot.sendMessage(from_id, msg_str)
  

if __name__ == "__main__":
    TOKEN = sys.argv[1]  # get token from command-line
    urlNationalData = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json"
    bot = telepot.Bot(TOKEN)
    bot.urlNationalData = urlNationalData
    MessageLoop(bot, {'chat':on_chat_message,'callback_query':on_callback_query}).run_as_thread()
    print ('Listening ...')

    # Keep the program running.
    while 1:
        time.sleep(10)
