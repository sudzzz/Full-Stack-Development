from django.db import models
import sqlite3
# Create your models here.

class MyDatabase:
    def __init__(self):
        self.createDb=sqlite3.connect('mainDb.db')
        self.qrcur=self.createDb.cursor()

    def createTable(self):
        self.qrcur.execute("create table if not "
            "exists Customers(id integer primary key,"
                "name text, street text, balance real)")

    def addCust(self,cd,nm,st,bl):
        self.qrcur.execute('''insert into Customers
values(?,?,?,?)''',(cd,nm,st,bl))
        self.createDb.commit()

    def ReadCust(self):
        self.qrcur.execute("select * from Customers")
        nm=[row[1] for row in self.qrcur.fetchall()]
        return nm

    def ReadCust2(self):
        self.qrcur.execute("select * from Customers")
        #nm = [row[1] for row in self.qrcur.fetchall()]
        return self.qrcur.fetchall()


    def ReadIds(self):
        self.qrcur.execute("select * from Customers")
        nm = [row[0] for row in self.qrcur.fetchall()]
        return nm
