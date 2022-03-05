from telegram.ext import Updater,CommandHandler
import main
TOKEN = input("请输入token")
updater = Updater(TOKEN)
dispatcher = updater.dispatcher
def ping(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Pong~")
def clear(update, context):
    ins = main.schedule()
    ins.clear()
    context.bot.send_message(chat_id=update.effective_chat.id, text=ins.ok)
def done(update, context):
    ins = main.schedule()
    ins.done()
    context.bot.send_message(chat_id=update.effective_chat.id, text=ins.kp)
def show(update, context):
    ins = main.schedule()
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"已打卡{ins.day}天")
Ping = CommandHandler('ping', ping)
Clear = CommandHandler('clear', clear)
Done = CommandHandler('done', done)
Show = CommandHandler('show', show)
dispatcher.add_handler(Ping)
dispatcher.add_handler(Clear)
dispatcher.add_handler(Done)
dispatcher.add_handler(Show)
updater.start_polling()
