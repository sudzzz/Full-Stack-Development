class Employee:
    empcode=10
    empname="aman"

    def __init__(self,c,n):
        self.empcode=c
        self.empname=n

    def display(self):
        print(self.empcode,self.empname)

emp=Employee(202,"Ajay")
emp.display()
