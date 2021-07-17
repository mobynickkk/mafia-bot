import telebot

token = ''
with open('token.txt', 'r') as f:
    token = f.readline()


bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет!')

