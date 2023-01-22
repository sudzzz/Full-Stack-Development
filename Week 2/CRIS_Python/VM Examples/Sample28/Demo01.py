import sqlite3

createDb=sqlite3.connect('June28.db')
qrcur=createDb.cursor()

def createTable():
    qrcur.execute('''create table if not
EXISTS Items2(id INTEGER PRIMARY KEY AUTOINCREMENT,
category varchar(20),name varchar(20), price number, qty number)''')

def AddItems():
    qrcur.execute("insert into Items(name,price,qty)"
                  "values('MP3',200,20)")
    createDb.commit()



def main():
    createTable()
    AddItems()
    qrcur.execute("update sqlite_sequence set seq=100 where name='items'")
    createDb.commit()


    qrcur.execute("select * from Items")

    for rw in qrcur:
        print(rw)

main()


