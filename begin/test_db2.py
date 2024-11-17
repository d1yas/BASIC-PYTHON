import sqlite3
import os

if os.path.exists('kutubxona.db'):
    os.remove('kutubxona.db')
else:
    pass

connect = sqlite3.connect('kutubxona.db')
cursor = connect.cursor()


def create_table():
    cursor.execute("DROP TABLE IF EXISTS kutubhona")
    cursor.execute("""CREATE TABLE IF NOT EXISTS kutubhona (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    book_info TEXT,
    author TEXT,
    data TEXT,
    page_all INTEGER,
    status BOOL
    )""")
    connect.commit()



def add_book(name: str, book_info: str, author: str, data: str, page_all: int, status: bool):
    values_for = (name, book_info, author, data, page_all, status)
    cursor.execute("INSERT INTO kutubhona(name,book_info,author,data,page_all,status) VALUES (?,?,?,?,?,?)", values_for)
    connect.commit()


def delete_book(kitob_id: int):
    cursor.execute("DELETE FROM kutubhona WHERE id = ?", (kitob_id,))
    connect.commit()


def register():
    cursor.execute("""CREATE TABLE IF NOT EXISTS users_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
    )""")

    user_data = (input("Username: "), input("Password: "))
    cursor.execute("INSERT INTO users_data(username,password) VALUES (?,?)", user_data)
    connect.commit()
    print("Ro'yxatdan muvaffaqiyatli o'tdingiz!")
    return user_data


def login():
    username = input("Username: ")
    password = input("Password: ")
    cursor.execute("SELECT * FROM users_data WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    if user:
        print("Tizimga muvaffaqiyatli kirdingiz!")
        return True
    else:
        print("Login yoki parol xato!")
        return False


def select_book():
    cursor.execute("SELECT * FROM kutubhona")
    books = cursor.fetchall()
    if books:
        print("Hamma kitobla royhati: ")
        for book in books:
            print(
                f"""id-'{book[0]}'.\nKitob - {book[1]}.\nKitob haqida - {book[2]} (Avtor: {book[3]}),\n Chiqazilgan sanasi - {book[4]},\nPage_all - {book[5]},\nStatus - {book[6]}""")
    else:
        print("Kitoblar mavjud emas.")


def band_qilish(kitob_id: int):
    cursor.execute("SELECT * FROM kutubhona WHERE id = ?", (kitob_id,))
    book = cursor.fetchone()

    if book:
        if book[5]:
            cursor.execute("UPDATE kutubhona SET status = 0 WHERE id = ?", (kitob_id,))  # Set status to 0 (False)
            connect.commit()
            print(f"{book[1]} kitobi band qilindi.")
        else:
            print("Bu band qilinib bogan .")
    else:
        print("Kitob topilmadi.")


def band_qilinmagan():
    cursor.execute("SELECT * FROM kutubhona WHERE status = 1")
    books = cursor.fetchall()
    if books:
        print("Band qilinmagan kitoblar ro'yxati:")
        for book in books:
            print(
                f"""id-'{book[0]}'.\nKitob - {book[1]}.\nKitob haqida - {book[2]} (Avtor: {book[3]}),\nChiqazilgan sana - {book[4]},\nPage_all - {book[5]},\nStatus - {book[6]}""")
    else:
        print("Band qilinmagan kitoblar mavjud emas.")


def band_qilingan():
    cursor.execute("SELECT * FROM kutubhona WHERE status = 0")
    books = cursor.fetchall()
    if books:
        print("Band qilingan kitoblar ro'yxati:")
        for book in books:
            print(
                f"""id-'{book[0]}'.\nKitob - {book[1]}.\nKitob haqida - {book[2]} (Avtor: {book[3]}),\nChiqazilgan sana - {book[4]},\nPage_all - {book[5]},\nStatus - {book[6]}""")
    else:
        print("Band qilingan kitoblar mavjud emas.")


def start():
    create_table()

    while True:
        choose = int(input("1 - Register\n2 - Login\n"))
        if choose == 1:
            register()
        elif choose == 2:
            if login():
                while True:
                    action = int(input(
                        "1 - Kitoblar ro'yxatini ko'rish\n2 - Kitob band qilish\n3 - Chiqish\n4 - Kitob qo'shish\n5 - Band qilinmagan kitobla\n6 - Band qilingan kitobla\n"))
                    if action == 1:
                        select_book()
                    elif action == 2:
                        kitob_id = int(input("Band qilmoqchi bo'lgan kitob ID raqamini kiriting: "))
                        band_qilish(kitob_id)
                    elif action == 3:
                        print("Chiqildi.")
                        break
                    elif action == 4:
                        name = input("Kitob nomi: ")
                        book_info = input("Kitob haqida: ")
                        author = input("Avtor: ")
                        data = input("Chiqazilgan sana: ")
                        page_all = int(input("Page soni: "))
                        status = True
                        add_book(name, book_info, author, data, page_all, status)
                        print("Kitob qo'shildi.")
                    elif action == 5:
                        band_qilinmagan()
                    elif action == 6:
                        band_qilingan()
        else:
            print("Error")


start()
