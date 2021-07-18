from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

from gamelogic.roles import Mafia


def get_mafia_markup(game):
    civilians = filter(lambda gamer: not isinstance(gamer.role, Mafia), game.gamers)
    keyboard = InlineKeyboardMarkup()
    for civilian in civilians:
        keyboard.add(InlineKeyboardButton(civilian.name))
        return keyboard
