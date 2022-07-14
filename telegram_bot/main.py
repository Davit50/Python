from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler


def echo(update, context):
    cur = update.message.text
    if "hello" in cur:
        update.message.reply_text("HI nice to met you")
    else:
        update.message.reply_text("How are you")


def main():
    token = "5258797595:AAHataUFMJ8K3tKAeApQgGpArjkofQYKVx4"
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    text_handler = MessageHandler(Filters.text, echo)
    dp.add_handler(text_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
