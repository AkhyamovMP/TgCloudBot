import telebot
import requests
import config
import manager

bot = telebot.TeleBot(config.bot_token)

users = {}
print(manager.translate_folder_id(1))

class User:
    def __init__(self):
        self.state = 'SETUP'
        self.channel_id = '-1001559868838'
        self.folders = {}


def get_user(msg):
    uid = msg.from_user.id
    if uid in users:
        return users[uid]
    users[uid] = User()
    return users[uid]


@bot.message_handler(commands=["start"])
def start(msg, res=False):
    get_user(msg).state = 'SETUP'
    main_message = ('Приступим к настройке. Чтобы хранить файлы, мне нужен приватный канал. Действуй по инструкции:\n'
    + '1 - Создай приватный канал\n'
    + '2 - Добавь меня туда в роли администратора со стандартными настройками\n'
    + '3 - Запости туда любое сообщение и перешли его в этот чат\n')
    bot.send_message(msg.chat.id, 'Йо, этот бот категоризирует файлы по папкам. \nСписок команд: /help')
    bot.send_message(msg.chat.id, main_message)
    bot.send_message(msg.chat.id, 'Отказываюсь делать что-либо, пока ты не выполнишь то, что я сказал')


@bot.message_handler(commands=["help"])
def print_commands(msg):
    bot.send_message(msg.chat.id, 'TODO: список команд')


@bot.message_handler(commands=["post"])
def post(msg):
    post_message = 'new message!'
    res = requests.get('https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s' % (config.bot_token, channel_id, post_message))


@bot.message_handler(func=lambda msg: get_user(msg).state == 'MAIN_MENU')
def main(message):
    bot.send_message(message.chat.id, 'there is main menu')


@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, message)



bot.infinity_polling()
