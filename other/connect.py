import psycopg2
from psycopg2 import sql

# Параметры подключения к базе данных
host = "localhost"  # Адрес сервера
database = "top"  # Название базы данных
user = "ilya"  # Имя пользователя
password = "ilya"  # Пароль пользователя
port = "5432"  # Порт, по умолчанию 5432 для PostgreSQL


# Подключение к базе данных
connection = psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password,
    port=port
)

# # Создание курсора для выполнения SQL-запросов
cursor = connection.cursor()

# Пример выполнения SQL-запроса
cursor.execute("SELECT * from product;")
cursor.fetchone()
# Получение результата запроса
db_version = cursor.fetchone()
print(f"Версия базы данных: {db_version}")

# # Закрытие курсора и соединения
cursor.close()
connection.close()

