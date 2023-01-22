import sqlite3

#createdb=sqlite3.connect(':memory:')

createdb=sqlite3.connect('mymaindb')
qr=createdb.cursor()

def CreateTable():
    qr.execute("create table if not exists Customers(id INTEGER PRIMARY KEY, name TEXT(20),age INTEGER)")

def AddCust():
    qr.execute("insert into Customers values(101,'Aman',20)")
    createdb.commit()

def AddCustManual(r,n,a):
    qr.execute("insert into Customers values(?,?,?)",(r,n,a))
    createdb.commit()

def ModCust(r):
    qr.execute("update Customers set name='Harmeet',age=25 where id=" + str(r))


CreateTable()
#AddCust()
#AddCustManual(104,'Ravi',30)
ModCust(104)
qr.execute("select id from Customers")
for ln in qr:
    print(ln[0])



