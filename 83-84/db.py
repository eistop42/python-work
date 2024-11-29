from sqlalchemy import create_engine, text


db_name = 'C:\\Users\\Б - Преподаватель\\Documents\\Евдокимов Илья\\python-work\\db\\bot_todo.db'
engine = create_engine(f'sqlite:///{db_name}')

with engine.connect() as con:
    res = con.execute(text('select * from task')).all()

    print(res)


with engine.connect() as con:
    res = con.execute(text('select * from task where user_id=:user_id'), {'user_id': 10}).all()

    print(res)


with engine.connect() as con:
    res = con.execute(text('insert into task (name, user_id) values(:name, :user_id)'),
                      {'user_id': 1, 'name': 'написать запрос'})
    con.commit()
