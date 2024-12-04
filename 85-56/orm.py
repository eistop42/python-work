from typing import List

from sqlalchemy import create_engine

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
from sqlalchemy import select, ForeignKey, delete


db_name = 'C:\\Users\\Б - Преподаватель\\Documents\\Евдокимов Илья\\python-work\\db\\bot_todo.db'
engine = create_engine(f'sqlite:///{db_name}')


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


session = Session(engine)

r = session.scalars(select(Task)).all()
task = r[0]

session.close()


task = Task(name='прибраться дома')
session.add(task)
session.commit()


users = session.scalars(select(User)).all()

# print(users[0].name, users[0].id, users[0].telegram_id)

tasks = session.scalars(select(Task).where(Task.user_id == 3)).all()


# for task in tasks:
#     print(task.name, task.user.telegram_id)

user = session.scalars(select(User).where(User.id == 3)).one()
tasks = user.tasks
print(tasks)

session.execute(delete(Task).where(Task.id == 2))
session.commit()

session.close()
