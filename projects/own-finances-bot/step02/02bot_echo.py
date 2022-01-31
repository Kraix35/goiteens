from telegram.ext import Updater, MessageHandler, Filters

def echo(update, context):
    #отримуємо строку з бота
    print(update.message.text)

    #відправляємо строку з бота
    update.message.reply_text(update.message.text)

updater = Updater("5025054506:AAG0EoelD86J8jKvVJaO_tUkwpEyDAUmsQ0")
dispatcher = updater.dispatcher

dispatcher.add_handler(MessageHandler(Filters.all, echo))

updater.start_polling()
updater.idle()
