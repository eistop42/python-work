import telebot
import random

token = ''
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['weather'])
def weather(message):
    print(message)
    bot.reply_to(message, 'Погода не очень!😎')

@bot.message_handler(commands=['hello'])
def hello(message):
    bot.reply_to(message, 'Привет!')


@bot.message_handler(commands=['coin'])
def coin(message):
    res = random.choice(['Орел', 'Решка'])
    bot.reply_to(message, res)


@bot.message_handler(regexp="привет")
def hello_m(message):
    bot.reply_to(message, 'привет!')


todo = []
user_state = ''
ADD_STATE = 'add'

@bot.message_handler(commands=["add"])
def add(message):
    global user_state
    user_state = ADD_STATE
    bot.reply_to(message, 'Введи текст задачи: ')

@bot.message_handler(commands=["tasks"])
def get_task_list(message):
    bot.reply_to(message, ",".join(todo))

@bot.message_handler(func=lambda message: True)
def get_task(message):
    global user_state
    if user_state == ADD_STATE:
        todo.append(message.text)
        user_state = ''
        bot.reply_to(message, 'Добавил в базу')











bot.infinity_polling()
