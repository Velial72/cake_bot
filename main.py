import os
import sqlite3

from datetime import datetime
import time
import telebot
from telebot import types


bot = telebot.TeleBot('6125022357:AAHc-FiPd5qsIyHhKaAiTKIft-1h1Jq34HU')

cakes = [['торт 1', 1000], ['торт 4',3000], ['торт 3',3000]]

@bot.message_handler(commands=['start'])
def start(message):
    start_text = "Привет! Прежде чем оформить заказ, давайте Вы разрешите нам пользоваться данными которые нам необходимо будет получить от Вас? \n \n Нажимая на кнопку продолжить - вы подтверждаете что ознакомились с нашими условиями и приняли их."
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(types.InlineKeyboardButton("ПРИНИМАЮ >>", callback_data="main_page"))
    bot.send_message(message.chat.id, start_text, reply_markup=markup)

@bot.message_handler(commands=['admin'])
def admin(message):
    if message.from_user.username == 'Only1_MMA':
        start_text = "Здравствуй хозяин, что изволишь?"
        markup = types.InlineKeyboardMarkup()
        markup.row_width = 1
        button1 = types.InlineKeyboardButton("Количество пользователей", callback_data="members")
        button2 = types.InlineKeyboardButton("Заказы", callback_data="orders")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, start_text, reply_markup=markup)

    else:
        start_text = "Куда лезешь!? Ты не мой хозяин!\n\nВведи /start"
        bot.send_message(message.chat.id, start_text)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'members':
        # func
        markup = types.InlineKeyboardMarkup()
        markup.row_width = 1
        orders = types.InlineKeyboardButton("Заказы", callback_data="orders")
        markup.add(orders)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text=f"Всего зарегистрированных пользователей: ?", reply_markup=markup)

    elif call.data == 'orders':
        markup = types.InlineKeyboardMarkup()
        markup2 = types.InlineKeyboardMarkup()
        markup.row_width = 1
        members = types.InlineKeyboardButton("Количество пользователей", callback_data="members")
        done = types.InlineKeyboardButton("Выполнен", callback_data="done")
        markup.add(done)
        markup2.add(members)
        num = 0
        for name, price in cakes:
            num += 1
            bot.send_message(call.message.chat.id, text=f"Заказ №{num}:\n{name}\nцена {price}", reply_markup=markup)
        bot.send_message(call.message.chat.id, text='поработаем еще?', reply_markup=markup2)

    elif call.data == 'main_page':
        text = "Что ты хочешь?"
        markup = types.InlineKeyboardMarkup()
        markup.row_width = 1
        get_order = types.InlineKeyboardButton("Заказать", callback_data="get_order")
        prices = types.InlineKeyboardButton("Узнать цены", callback_data="prices")
        my_orders = types.InlineKeyboardButton("Мои заказы", callback_data="my_orders")
        markup.add(get_order, prices, my_orders)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=text, reply_markup=markup)

    elif call.data == 'get_order':
        text = "дальше не прописал.. возможно"
        markup = types.InlineKeyboardMarkup()
        markup.row_width = 1
        get_order = types.InlineKeyboardButton("кликабельная кнопка", callback_data="x")
        markup.add(get_order)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=text, reply_markup=markup)

    elif call.data == 'x':
        text = "больше не нажимай кнопки, вдруг сломаешь"
        markup = types.InlineKeyboardMarkup()
        markup.row_width = 1
        get_order = types.InlineKeyboardButton("а если нажать?", callback_data="y")
        markup.add(get_order)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=text, reply_markup=markup)

    elif call.data == 'y':
        text = "Я ЖЕ СКАЗАЛ, СЛОМАЕШЬ!!!"
        markup = types.InlineKeyboardMarkup()
        markup.row_width = 1
        get_order = types.InlineKeyboardButton("нажми меня", callback_data="b")
        markup.add(get_order)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=text, reply_markup=markup)

    elif call.data == 'b':
        text = "Поздравляю! ты сломал бота"
        markup = types.InlineKeyboardMarkup()
        markup.row_width = 1
        get_order = types.InlineKeyboardButton("нажми меня", callback_data="b")
        markup.add(get_order)
        bot.send_message(call.message.chat.id, text)

    elif call.data == 'prices':
        text = "дальше не прописал.. возможно"
        markup = types.InlineKeyboardMarkup()
        markup.row_width = 1
        get_order = types.InlineKeyboardButton("кликабельная кнопка", callback_data="x")
        markup.add(get_order)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=text, reply_markup=markup)

    elif call.data == 'my_orders':
        text = "дальше не прописал.. возможно"
        markup = types.InlineKeyboardMarkup()
        markup.row_width = 1
        get_order = types.InlineKeyboardButton("кликабельная кнопка", callback_data="x")
        markup.add(get_order)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=text, reply_markup=markup)



def main():
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as error:
            print(error)
            time.sleep(5)


if __name__ == '__main__':
    main()
