from django.db import models

import sqlite3

class MyDatabase:
    def __init__(self):
        self.createDb=sqlite3.connect('maindb.db')
        self.qrcur=self.createDb.cursor()

    def createTable(self):
        self.qrcur.execute('''create table if not EXISTS Customers
(id INTEGER PRIMARY KEY,name TEXT, street TEXT,balance REAL)''')

    def addCust(self,cd,nm,st,bl):
        self.qrcur.execute('''insert into Customers
                  values(?,?,?,?)''',(cd,nm,st,bl))
        self.createDb.commit()

    def readCust(self):
        self.qrcur.execute("select * from Customers")
        #s=""
        #for ln in self.qrcur:
        #    s+=(ln[1])
        #print(s)
        #nm=[row[1] for row in self.qrcur.fetchall()]
        nm = [row[1] for row in self.qrcur.fetchall()]

        return nm

    def readCust2(self):
        self.qrcur.execute("select * from Customers")
        # s=""
        # for ln in self.qrcur:
        #    s+=(ln[1])
        # print(s)
        # nm=[row[1] for row in self.qrcur.fetchall()]
        #nm = [self.qrcur.fetchall()]

        return self.qrcur.fetchall()

    def delCust(self):
        self.qrcur.execute("delete from Customers")
        self.createDb.commit()

    def MyPieData(self):
        '''
'''
        self.qrcur.execute("select * from Teams")
        return self.qrcur.fetchall()