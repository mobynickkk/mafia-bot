from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

from gamelogic.roles import Mafia


class MarkupCreator:

    def __init__(self, game):
        self.game = game

    def get_mafia_markup(self):
        civilians = filter(lambda gamer: not isinstance(gamer.role, Mafia), self.game.gamers)
        keyboard = InlineKeyboardMarkup()
        for civilian in civilians:
            keyboard.add(InlineKeyboardButton(civilian.name))
        return keyboard
