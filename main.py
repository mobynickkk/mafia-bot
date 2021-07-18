from .bot import BotControl, get_token

bot_control = BotControl(get_token())
bot_control.build_bot()

bot_control.polling(none_stop=True)
