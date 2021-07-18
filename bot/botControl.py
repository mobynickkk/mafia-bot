import telebot

from gamelogic import Game


class BotControl:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token)
        self.active_games = {}

    def build_bot(self):

        @self.bot.message_handler(commands=['start'])
        def start_message(message):
            self.bot.send_message(message.chat.id, 'Привет!')

        @self.bot.message_handler(commands=['startgame'])
        def start_game(message):
            game = self.active_games.get(message.chat.id,
                                         Game(message.chat.id, message.from_user.id, message.from_user.username))
            if game.is_game_started:
                self.bot.send_message(message.chat.id, 'Извините, игра уже началась!')
                return
            self.active_games[message.chat.id] = game
            self.bot.send_message(message.chat.id, game.gather_players())

        @self.bot.message_handler(commands=['join'])
        def join_game(message):
            game = self.active_games[message.chat.id]
            if game.is_game_started:
                self.bot.send_message(message.chat.id, 'Игра уже началась!')
            else:
                self.bot.send_message(message.chat.id,
                                      game.gather_player(message.from_user.id,
                                                         message.from_user.username))

        @self.bot.message_handler()
        def make_vote(message):
            """ Метод для дневного голосования (в общем чате) """
            pass

        @self.bot.message_handler()
        def make_special_vote(message):
            """ Метод для голосования мафии/ареста офицера (в лс) """
            pass

    def polling(self, *args, **kwargs):
        try:
            self.bot.polling(*args, **kwargs)
        except:
            self.polling(*args, **kwargs)
