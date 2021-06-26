import config
# mastrobot_example.py
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# function to handle the /start command
def start(update, context):
    name = update.message.from_user.first_name
    update.message.reply_text(f'САСАТЬ {name.upper()}')

# function to handle the /help command
def help(update, context):
    update.message.reply_text('help command received')

# function to handle errors occured in the dispatcher 
def error(update, context):
    update.message.reply_text('an error occured')

# function to handle normal text 
def text(update, context):
    text_received = update.message.text
    #{'is_bot': False, 'username': 'SumZbrod', 'id': 1094965520, 'language_code': 'ru', 'first_name': 'Никита'}
    name = update.message.from_user.first_name
    update.message.reply_text(f'{name}, did you said "{text_received}" ?')

def main():
    with open(config.path_to_token, 'r') as f:
        TOKEN = f.read()
    # create the updater, that will automatically create also a dispatcher and a queue to 
    # make them dialoge

    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

   
    # add handlers for start and help commands
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))

    # add an handler for normal text (not commands)
    dispatcher.add_handler(MessageHandler(Filters.text, text))

    # add an handler for errors
    dispatcher.add_error_handler(error)

    # start your shiny new bot
    updater.start_polling()

    # run the bot until Ctrl-C
    updater.idle()
if __name__ == '__main__':
    main()

