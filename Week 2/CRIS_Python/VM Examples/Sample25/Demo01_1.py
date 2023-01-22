import sqlite3

#createDb=sqlite3.connect(':memory:')
createDb=sqlite3.connect('maindb.db')
qrcur=createDb.cursor()

def createTable():

    qrcur.execute('''create table if not EXISTS Customers
(id INTEGER PRIMARY KEY,name TEXT, street TEXT,balance REAL)''')

def addCust(nm,st,bl):
    qrcur.execute('''insert into Customers(name,street,balance)
                  values(?,?,?)''',(nm,st,bl))

def modCust(id):
    qrcur.execute("update Customers set name='Harmeet' where id=" +str(id))


def main():
    createTable()

    #addCust("Aman","JP",29293)
    #createDb.commit()
    modCust(4)

    qrcur.execute("select * from Customers")
    for ln in qrcur:
        print(ln)

    qrcur.execute("select sqlite_version()")
    for ln in qrcur:
        print(ln)


main()

