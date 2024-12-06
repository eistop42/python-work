import telebot
from  typing import List
from telebot import types

from sqlalchemy import create_engine

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
from sqlalchemy import select, ForeignKey, delete



class Base(DeclarativeBase):
    pass


class Task(Base):
    __tablename__ = 'task'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))

    user: Mapped["User"] = relationship(back_populates='tasks')

    def __repr__(self):
        return f"{self.id} - {self.name}"


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    telegram_id: Mapped[int]

    tasks: Mapped[List["Task"]] = relationship(back_populates='user')

    def __repr__(self):
        return f"{self.telegram_id}"


class TaskModelORM:
    def __init__(self, db_name):
        self.engine = create_engine(f'{db_name}')

    def get_tasks(self, user_id):
        with Session(self.engine) as session:
            tasks = session.scalars(select(Task).where(Task.user_id == user_id)).all()
            return tasks

    def get_user(self, telegram_id):
        with Session(self.engine) as session:
            r = session.scalars(select(User).where(User.telegram_id == telegram_id)).one_or_none()
            return r

    def add_task(self, name, user_id):
        with Session(self.engine) as session:
            task = Task(name=name, user_id=user_id)
            session.add(task)
            session.commit()

    def delete_task(self, task_id, user_id):
        with Session(self.engine) as session:

            session.execute(delete(Task).where(Task.id == task_id))
            session.commit()


token = ''
bot = telebot.TeleBot(token)

user_state = ''
ADD_STATE = 'add'
DEL_STATE = 'del'

db_name = 'postgresql+psycopg2://postgres:postgres@localhost:5432/bot_tasks'
db = TaskModelORM(db_name)


@bot.message_handler(commands=["start"])
def start(message):
    description = 'Я бот для создания списка дел. Жми кнопку или команду /add для добавления'

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('добавить задачу')
    button2 = types.KeyboardButton('посмотреть задачи')
    markup.add(button)
    markup.add(button2)

    telegram_id = message.chat.id
    user = db.get_user(telegram_id)
    print(telegram_id, user)
    if not user:
        db.add_user(telegram_id)
        bot.reply_to(message, 'я вас добавил ')

    bot.send_message(message.chat.id, description, reply_markup=markup)


@bot.message_handler(regexp='добавить задачу')
@bot.message_handler(commands=["add"])
def add(message):
    global user_state
    user_state = ADD_STATE
    bot.reply_to(message, 'Введи текст задачи: ')


@bot.message_handler(commands=["del"])
def delete_task(message):
    global user_state
    user_state = DEL_STATE

    telegram_id = message.chat.id
    user = db.get_user(telegram_id)
    tasks = db.get_tasks(user.id)
    tasks_str = 'Выбирай задачу: \n\n'
    for number, task in enumerate(tasks, 1):
        tasks_str += f'{number}. {task.name} \n'
    bot.reply_to(message, tasks_str)


@bot.message_handler(regexp='посмотреть задачи')
@bot.message_handler(commands=["tasks"])
def get_task_list(message):
    telegram_id = message.chat.id
    user = db.get_user(telegram_id)
    if not user:
        return bot.reply_to(message, 'вас нет в базе ')
    # print(user)
    tasks = db.get_tasks(user.id)
    if not tasks:
        return bot.reply_to(message, 'у вас нет задач ')
    tasks = [task.name for task in tasks]
    tasks_string = '\n'.join(tasks)
    bot.reply_to(message, tasks_string)


@bot.message_handler(commands=["end"])
def end_state(message):
    global user_state
    user_state = ''
    bot.reply_to(message, "Мы вышли из сеанса добавленя задачи")


@bot.message_handler(commands=["keyboard"])
def keyboard(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('добавить задачу')
    markup.add(button)

    bot.send_message(message.chat.id, 'Какой-то текст', reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def get_task(message):
    global user_state
    telegram_id = message.chat.id
    user = db.get_user(telegram_id)
    if user_state == ADD_STATE:
        db.add_task(message.text, user.id )
        user_state = ''
        bot.reply_to(message, 'Добавил в базу')
    if user_state == DEL_STATE:
        try:
            task_number = int(message.text)
        except Exception:
            print('ошибка')
            return

        user = db.get_user(telegram_id)
        tasks = db.get_tasks(user.id)

        if 0 < task_number < len(tasks)+1:
            task = tasks[task_number-1]
            print(task)
            db.delete_task(task.id, user.id)
            bot.reply_to(message, 'удалил задачу')
        else:
            print('такой задачи нет')


bot.infinity_polling()
