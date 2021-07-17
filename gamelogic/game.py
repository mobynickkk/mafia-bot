from random import shuffle
from time import sleep
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

roles_by_number_of_gamers = {4: ['Мафия', 'Житель', 'Житель', 'Житель'],
                             5: ['Мафия', 'Мафия', 'Житель', 'Житель', 'Житель'],
                             6: ['Мафия', 'Мафия', 'Житель', 'Житель', 'Житель', 'Житель'],
                             7: ['Мафия', 'Мафия', 'Офицер', 'Житель', 'Житель', 'Житель', 'Житель']}



class Gamer:
    def __init__(self, source_id):
        self.source_id = source_id

    def set_role(self, role):
        pass

    def do_step(self):
        """"""
        pass

class Game:

    def __init__(self, chat_id, source_id):
        self.gamers = [Gamer(source_id)]
        self.chat_id = chat_id
        self.votes = {}
        self.count_of_nights = 0
        self.mafia_votes = {}
        self.is_day = True

    def start(self):
        if len(self.gamers) in roles_by_number_of_gamers.keys():
            roles = shuffle(roles_by_number_of_gamers[len(self.gamers)])
            for gamer in self.gamers:
                gamer.set_role(roles.pop())

            #self.is_day = False
            self.make_turn()
            return 'Город засыпает, просыпается мафия и знакомится друг с другом'
        else:
            return 'Игроков должно быть от 4 до 7'

    def end(self):
        pass

    def make_turn(self):
        """ """
        # логика ходов, проверка, что мафия сходилась.
        # сделать через потоки (sleep)
        # если день, то проверку, что все проголосовали

        # для ночи
        if not self.is_day:
            pass
        elif self.is_day:
            pass




# в первый день голосуют и в первую ночь убивают