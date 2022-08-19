from email import message
import sqlite3


def write_data(user_id, users_name):

    try:
        conn = sqlite3.connect('first_bot.db')
        cursor = conn.cursor()

        # создаем пользователя с юзер айди -101010
        cursor.execute("INSERT OR IGNORE INTO users (user_id, user_name) VALUES (?, ?)", (user_id, users_name))

        # считываем всех пользователей
        users = cursor.execute("SELECT * FROM users")
        print(users.fetchall())

        # подтверждаем изменения
        conn.commit()
    except sqlite3.Error as error:
        print('Error=', error)

    finally:
        if(conn):
            conn.close()


def write_message_from_users(user_name, users_id, message):

    try:
        conn = sqlite3.connect('first_bot.db')
        cursor = conn.cursor()

        # создаем пользователя с юзер айди -101010
        cursor.execute("INSERT INTO records (user_name, users_id, message) VALUES (?, ?, ?)", (user_name, users_id, message))

        # подтверждаем изменения
        conn.commit()
    except sqlite3.Error as error:
        print('Error=', error)

    finally:
        if(conn):
            conn.close()
