import telebot
from telebot import types
from gpt import YandexGPT


token = ''
bot = telebot.TeleBot(token)

user_state = ''
DIALOG_STATE = 'dialog'

y_token = ''
y_catalog = ''

yandex_bot = YandexGPT(y_token, y_catalog)

users = {}

@bot.message_handler(commands=["start"])
def start(message):
    description = 'Я бот - нейросеть. Жми на кнопку или вводи команду /ask чтобы задать вопрос'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('задать вопрос')
    markup.add(button)

    users[message.chat.id] = {'count': 0}
    print(users)

    bot.send_message(message.chat.id, description, reply_markup=markup)



@bot.message_handler(commands=["ask"])
@bot.message_handler(regexp='задать вопрос')
def ask(message):
    global user_state
    user_state = DIALOG_STATE
    bot.reply_to(message, 'Диалог начат. Чтобы выйти - жми команду /end')


@bot.message_handler(commands=["end"])
def end(message):
    global user_state
    user_state = ''
    bot.reply_to(message, 'Пока!')


@bot.message_handler(func=lambda message: True)
def get_question(message):
    if user_state == DIALOG_STATE:

        chat_id = message.chat.id
        if chat_id in users:
            if users[chat_id]['count'] < 5:
                response = yandex_bot.send_request(message.text)
                users[chat_id]['count'] += 1
                bot.reply_to(message, response)
            else:
                bot.reply_to(message, 'Плати деньги')
    print(users)


bot.infinity_polling()
