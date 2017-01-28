import sys, time, telepot, json
from toDoDbHelper import DBHelper  //make sure the files are in the same folder
from telepot.namedtuple import InlineKeyboardMarkup
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

db = DBHelper()
TOKEN = 'PUT YOUR TOKEN IN HERE'
bot = telepot.Bot(TOKEN)

def build_keyboard(items):
    keyboard = [[item] for item in items]
    reply_markup = {"keyboard":keyboard, "one_time_keyboard":True}
    return json.dumps(reply_markup)

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        text = msg['text']
        db.__init__()
        items = db.get_items(chat_id)
        if text == "/done":
            keyboard = build_keyboard(items)
            bot.sendMessage(chat_id, "Select and items to delete", reply_markup=keyboard)
        elif text == "/start":
            bot.sendMessage(chat_id, "Welcome to your personnal To Do List! Send and text to me and I'll store it as an item. Send /done to remove items")
        elif text == "/list":
            toDo = db.get_items(chat_id)
            toDoList = "\n\n".join(toDo)
            bot.sendMessage(chat_id, toDoList)
        elif text.startswith("/"):
            pass
        elif text in items:
            db.delete_item(text, chat_id)
            items = db.get_items(chat_id)
            message = "\n\n".join(items)
            bot.sendMessage(chat_id, message)
        else:
            db.add_item(text, chat_id)
            items = db.get_items(chat_id)
            message = "\n\n".join(items)
            bot.sendMessage(chat_id, message)

def main():
    db.setup()
    TOKEN = 'PUT YOUR TOKEN IN HERE'
    bot.message_loop(handle)

    while 1:
        time.sleep(10)

//run the code always, you might want to run with nohup from the command line
//this will keep your bot running as a background script even if you close the terminal
if __name__=='__main__':
    main()
