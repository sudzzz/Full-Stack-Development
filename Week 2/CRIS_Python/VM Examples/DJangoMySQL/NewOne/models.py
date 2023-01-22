from __future__ import unicode_literals

from django.db import models
import MySQLdb

# Create your models here.

class Customer:
    def __init__(self):
        cn=MySQLdb.connect(host="localhost",user="root",passwd="mysql@python",db="pythondb")
        c=cn.cursor()


    def ReadCustomers(self):
        cn = MySQLdb.connect(host="localhost", user="root", passwd="mysql@python", db="pythondb")
        c = cn.cursor()
        c.execute("select * from Employee")
        data=c.fetchall()
        return data

