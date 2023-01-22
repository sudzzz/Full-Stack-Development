import sqlite3

createdb=sqlite3.connect('taskdb1')
qr=createdb.cursor()

def CreateTable():
    qr.execute("create table if not exists Digital(MobilePh number,name varchar(20),age number,location varchar(20))")
    qr.execute("create table if not exists Reminder(EventDate date,EventName varchar(20),EventType varchar(20))")
    qr.execute("create table if not exists Reminder2(EventDate date,EventName varchar(20),EventType varchar(20),No number REFERENCES Digital(MobilePh))")



def InputInfoDigital():
    MobilePh=input("Enter Mobile Ph")
    name=input("Enter name")
    age=int(input("Enter Age"))
    location=input("Enter Mobile location")
    InsertDigital(MobilePh,name,age,location)

def InsertDigital(m,n,a,l):
    qr.execute("insert into Digital values(?,?,?,?)",(m,n,a,l))
    createdb.commit()

def InputInfoReminder():
    EventDate=input("Enter Event Date")
    EventName=input("Enter Event Name")
    EventType=input("Enter Event Type")
    InsertReminder(EventDate,EventName,EventType)

def InsertReminder(d,n,t):
    qr.execute("insert into Reminder values(?,?,?)",(d,n,t))
    createdb.commit()


CreateTable()
#InputInfoDigital()
#qr.execute("select * from Digital")
InputInfoReminder()
qr.execute("select * from Reminder")
for ln in qr:
    print(ln)


qr.execute("select EventName from Reminder where EventDate=date('now')")
for ln in qr:
    print(ln[0])

qr.execute("select STRFTIME('%m',EventDate) ,STRFTIME('%dd',EventDate) from Reminder where EventDate=date('now')")
for ln in qr:
    print(ln[0])

'''print('after')
qr.execute("select  current_date ")
for ln in qr:
    print(ln)

qr.execute("select  date('now') ")
for ln in qr:
    print(ln)'''