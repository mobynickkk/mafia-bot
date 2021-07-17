import telebot

from .gamelogic import Game


token = ''
with open('token.txt', 'r') as f:
    token = f.readline()


bot = telebot.TeleBot(token)
active_games = {}


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет!')


@bot.message_handler(commands=['startgame'])
def start_game(message):
    game = Game(message.chat.id, message.from_.id, message.from_.name)
    active_games[message.chat.id] = game
    bot.send_message(message.chat.id, game.gather_players())


@bot.message_handler(commands=['join'])
def join_game(message):
    game = active_games[message.chat.id]
    bot.send_message(message.chat.id, game.gather_player(message.from_.id, message.from_.name))

