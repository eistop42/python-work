from typing import List

from flask import Flask, render_template

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
from sqlalchemy import ForeignKey
from flask_sqlalchemy import SQLAlchemy


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


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:\\Users\\Б - Преподаватель\\Documents\\Евдокимов Илья\\python-work\\db\\bot_todo.db"

db = SQLAlchemy(model_class=Base)
db.init_app(app)

todo = [{'id': 1, 'name': 'погулять'},
        {'id': 2, 'name': 'почитать'},
            {'id': 3, 'name': 'поспать'}
        ]


# ООП MVC
# model - база
# view - как отобразить данные
# contoller - ходит в model, выбирает нужный view


# Framework MVC
# model - база
# template - как отобразить данные
# view - ходит в model, выбирает нужный template

@app.route('/')
def main():

    todo_db = db.session.execute(db.select(Task)).scalars().all()
    users = db.session.execute(db.select(User)).scalars().all()

    return render_template('main.html', todo_data=todo_db, users=users)


@app.route('/aboutpage')
def about_page():
    return render_template('about.html')


@app.route('/tasks/<int:user_id>')
def user_tasks(user_id):
    tasks = db.session.execute(db.select(Task).filter_by(user_id=user_id)).scalars().all()
    return render_template('tasks.html',
                           tasks=tasks, user_id=user_id)


if __name__ == '__main__':
    app.run(debug=True)

