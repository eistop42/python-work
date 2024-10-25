import telebot
from telebot import types
from  gpt import YandexGPT


token = ''
bot = telebot.TeleBot(token)

user_state = ''
DIALOG_STATE = 'dialog'

y_token = ''
y_catalog = ''

yandex_bot = YandexGPT(y_token, y_catalog)

@bot.message_handler(commands=["start"])
def start(message):
    description = 'Я бот - нейросеть. Жми на кнопку или вводи команду /ask чтобы задать вопрос'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('задать вопрос')
    markup.add(button)

    bot.send_message(message.chat.id, description, reply_markup=markup)



@bot.message_handler(commands=["ask"])
@bot.message_handler(regexp='задать вопрос')
def ask(message):
    global user_state
    user_state = DIALOG_STATE
    bot.reply_to(message, 'Диалог начат. Чтобы выйти - жми команду /end')


@bot.message_handler(func=lambda message: True)
def get_question(message):
    if user_state == DIALOG_STATE:
        # место для соединения с нейросетью

        response = yandex_bot.send_request(message.text)
        bot.reply_to(message, response)


bot.infinity_polling()
