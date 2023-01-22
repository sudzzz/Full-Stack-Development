import sqlite3

createDb=sqlite3.connect('June28_Join.db')
qrcur=createDb.cursor()

def createTable():
    qrcur.execute('''CREATE TABLE IF NOT
    EXISTS Items(id INTEGER PRIMARY KEY AUTOINCREMENT,
    category VARCHAR(20),name VARCHAR(20))''')

    qrcur.execute('''CREATE TABLE IF NOT
    EXISTS Items2(iid INTEGER PRIMARY KEY AUTOINCREMENT,
    amt number)''')



def AddItems():
    qrcur.execute("insert into Items(category,name)"
                  "values('ele','MP3')")
    createDb.commit()
    qrcur.execute("insert into Items2(amt)"
                  "values(2220)")
    createDb.commit()



def main():
    createTable()
    #AddItems()

    qrcur.execute("SELECT * FROM Items")

    for rw in qrcur:
        print(rw)
    qrcur.execute("select * from Items2")

    for rw in qrcur:
        print(rw)

    qrcur.execute("select * from Items2 join items on items2.iid=items.id")

    for rw in qrcur:
        print(rw)


main()


