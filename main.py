import telebot
from pyexpat.errors import messages
from telebot import types
from telebot.types import InlineKeyboardMarkup

Token = "7337994678:AAEOqV7DceI1Y6_WX1KJzi3Rf5ErvTMGCQU"
bot = telebot.TeleBot(Token)

@bot.message_handler(commands=["game"])
def Game(message):
    text = "Вы очнулись на острове, справа вы видите двух капибар, слева разрушенный корабль"

    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="подойти к капибарам", callback_data="1.1")
    btn2 = types.InlineKeyboardButton(text="подойти к разрушенному кораблю", callback_data="1.2")
    keyboard.add(btn1, btn2)

    bot.send_message(message.chat.id, text, reply_markup = keyboard)

@bot.callback_query_handler(func=lambda call: True)
def Answering(call):
    if call.data == "1.1":
        Kapibars(call)
    elif call.data == "1.2":
        Treasers(call)
    elif call.data == "2.1":
        WithKapibars(call)
    elif call.data == "2.2":
        WithoutKapibars(call)
    elif call.data == "3.1":
        WithTreasers(call)
    elif call.data == "3.2":
        WithKapibars(call)


def Kapibars(call):
    text = "Вы подошли к капибарам, они смотрят на вас и ждут, что вы сделаете дальше"

    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Подружиться с ними", callback_data="2.1")
    btn2 = types.InlineKeyboardButton(text="Отойти", callback_data="2.2")
    keyboard.add(btn1, btn2)

    bot.send_message(call.from_user.id, text=text, reply_markup=keyboard)

def WithKapibars(call):
    text = "И жили вы долго и счастливо вместе с капибарами. Конец"
    bot.send_message(call.from_user.id, text= text)

def WithoutKapibars(call):
    text = "И жили вы долго и несчастно без капибар :( Конец"
    bot.send_message(call.from_user.id, text=text)

def Treasers(call):
    text = "Исследовав разрушенный корабль вы нашли сокровища!"

    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Забрать сокровища", callback_data="3.1")
    btn2 = types.InlineKeyboardButton("...Или все же подружиться с капибарами?", callback_data="3.2")
    keyboard.add(btn1, btn2)
    bot.send_message(call.from_user.id, text = text, reply_markup=keyboard)

def WithTreasers(call):
    text="И жили вы долго и богато, но без капибар"
    bot.send_message(call.from_user.id, text = text)

bot.polling(none_stop=True)