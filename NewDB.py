import sqlite3

def InpSet():
    db = sqlite3.connect("Phonebook.db")
    sql = db.cursor()
    sql.execute("""CREATE TABLE IF NOT EXISTS Phonebook (
        name TEXT, 
        number BIGINT
    )""")
    db.commit()

InpSet()