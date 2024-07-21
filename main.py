import telebot
from parsing import parsing_all_movies, parsing_the_best
from parsing import best_movies, all_films
from telebot import types
import random
from TOKEN import token

pars_bot = telebot.TeleBot(token)


@pars_bot.message_handler(commands=['start'])
def greetings(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    random_from_five_hundred = types.KeyboardButton("Случайный с лучших")
    random_from_everyone = types.KeyboardButton("Случайный со всех")
    markup.add(random_from_five_hundred, random_from_everyone)
    pars_bot.send_message(message.chat.id, text="Привет, {0.first_name}! Вы попали в бот для фильмов".format(message.from_user), reply_markup=markup)

@pars_bot.message_handler(content_types=['text'])
def five_hundred_best(message):
    if message.text == "Случайный со всех":
        if len(all_films) == 0:
            parsing_all_movies()
            pars_bot.send_message(message.chat.id, random.choice(all_films))
        else:
            pars_bot.send_message(message.chat.id, random.choice(all_films))
    elif message.text == "Случайный с лучших":
        if len(best_movies) == 0:
            parsing_the_best()
            pars_bot.send_message(message.chat.id, random.choice(best_movies))
        else:
            pars_bot.send_message(message.chat.id, random.choice(best_movies))
    
pars_bot.polling()