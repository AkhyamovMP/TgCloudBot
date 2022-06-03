import telebot
import config
import manager

bot = telebot.TeleBot(config.bot_token)

manager.create_folder()

@bot.message_handler(commands=["start"])
def start(message, res=False):
    bot.send_message(message.chat.id, 'Йо, этот бот категоризирует файлы по папкам. \nСписок команд: /help')

@bot.message_handler(commands=["help"])
def print_commands(message, res=False):
    bot.send_message(message.chat.id, 'TODO: список команд')




users = {}

class User:
    def __init__(self):
        self.state = 'PRE_MENU'
        self.folders = {}



# Получение сообщений от юзера


@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, message.text)



bot.infinity_polling()
