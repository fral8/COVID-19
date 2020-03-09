import sys
import time
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(msg)
    if content_type == 'text':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text = 'Testuali',callback_data = 'textualData')],
            [InlineKeyboardButton(text = 'Grafiche',callback_data = 'Images')]])
        bot.sendMessage(chat_id, "ultime informazioni:", reply_markup = keyboard)

def on_callback_query(msg):
    # global query_id, from_id, query_data, decided
    query_id, from_id, query_data = telepot.glance(msg, flavor = 'callback_query')
    print('Callback query:',query_id, from_id, query_data)
    bot.answerCallbackQuery(query_id, text = 'Great, now send me a picture!')
  

if __name__ == "__main__":
    TOKEN = sys.argv[1]  # get token from command-line
    bot = telepot.Bot(TOKEN)
    MessageLoop(bot, {'chat':on_chat_message,'callback_query':on_callback_query}).run_as_thread()
    print ('Listening ...')

    # Keep the program running.
    while 1:
        time.sleep(10)
