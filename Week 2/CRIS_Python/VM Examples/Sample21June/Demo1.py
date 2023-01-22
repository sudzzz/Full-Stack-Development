class Employee:
    empcode=0
    empname=""

    def __init__(self,c,n):
        self.empcode=c
        self.empname=n


    def display(self):
        print(self.empcode,self.empname)

emp=Employee(201,"Aman")
emp.display()