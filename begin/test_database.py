import sqlite3

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
def add_book(name: str, author: str, data: str, page_all: int, status: bool):
    for i in range(10):
        values_for = (input("Book name: "),input("Book_info: ") ,input("Book author: "), input("Create book data: "), int(input("page book: ")),True)
        cursor.execute("INSERT INTO kutubhona(name,author,data,page_all,status) VALUES (?,?,?,?,?)", values_for)
    connect.commit()

    # values = ("TEst_name", "Alisher Navoyi", "21 yanvar", 552, False)
# def update_book(kitob_id: int, name: str, author: str, data: str, page_all: int, status: bool):
#     cursor.execute("UPDATE kutubxona SET name = ?, data = ?, author = ?, page_all = ?, status = ? WHERE id = ?",
#                    (name, data, author, page_all, kitob_id),status)
#     connect.commit()

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
    return user_data

def login():
    pass

def select_book(kitob_id: int):
    kitob = cursor.execute("SELECT * FROM kutubhona WHERE kitob_id = ?", (kitob_id,))
    return kitob


def id_select():
    cursor.execute("SELECT id FROM kutubhona")
    return cursor.fetchall()

def band_qilish(name: str, author: str, data: str, page_all: int, status: bool):
    cursor.execute("""CREATE TABLE IF NOT EXISTS bron (
    id INTEGER PRIMARY KEY AUTOINCREMENT
    
    )""")
def start():
    choose = int(input("1 register -\n2 login -\n"))
    if choose == 1:
        register()
        a = cursor.execute("SELECT username FROM users_data")

    elif choose == 2:
        login()

start()




# insert_book()
# register()
# create_table()

