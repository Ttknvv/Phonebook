import sqlite3

#Обращение к БД
def OutSet():
    db = sqlite3.connect("Phonebook.db")
    sql = db.cursor()
    sql.execute("SELECT * FROM Phonebook")
    phone = sql.fetchall()
    db.commit()
    return phone

#Добавление к БД
def InsSet(name, number):
    db = sqlite3.connect("Phonebook.db")
    sql = db.cursor()
    sql.execute(f"INSERT INTO Phonebook VALUES (?, ?)", (name, number))
    db.commit()

#Удаление записи
