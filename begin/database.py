import sqlite3

connect = sqlite3.connect("sqlite3.db")

cur = connect.execute("""CREATE TABLE IF NOT EXISTS info(
                      CityID int NOT NULL,
                      PersonID int NOT NULL,
                      CityName varchar(15) DEFAULT "TASHKENT",
                      LastName varchar(20),
                      FirstName varchar(15)
                      )""")




connect.commit()

connect.close()
