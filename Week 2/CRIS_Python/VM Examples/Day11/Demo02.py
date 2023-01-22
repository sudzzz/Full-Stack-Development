import sqlite3

createdb=sqlite3.connect('mymaindb')
qr=createdb.cursor()

qr.execute("select julianday('now')-julianday('2016-06-03')")
for ln in qr:
    print(ln[0])


qr.execute("select date('now'),datetime(date('now'),'+5 days')")
for ln in qr:
    print(ln)


qr.execute("select date('now'),current_time,datetime(current_time,'+5 minutes')")
for ln in qr:
    print(ln)

qr.execute("select lower(substr('Harmeet',1,1)) "
           "|| upper(substr('Harmeet',2,length('Harmeet')-1))")
for ln in qr:
    print(ln[0])
