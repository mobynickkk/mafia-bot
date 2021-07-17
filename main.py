import telebot

with open('token.txt', 'r') as f:
    body = [line for line in f]
token = body[0]

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет!')

