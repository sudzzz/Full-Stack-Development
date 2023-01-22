import sqlite3
from django.db import models

class Employee:
    empcode =""
    empname=""
    empsalary=0

    def EmployeeAdd(self,c,n,s):
        self.empcode=c
        self.empname= n
        self.empsalary= s
