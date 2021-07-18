from .bot import BotControl

token = ''
with open('token.txt', 'r') as f:
    token = f.readline()

bot_control = BotControl(token)
bot_control.build_bot()

bot_control.polling(none_stop=True)
