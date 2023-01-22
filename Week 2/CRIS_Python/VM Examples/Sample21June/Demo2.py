class Employee:
    empcode=0
    empname=""
    empcount=0

    def __init__(self,c,n):
        self.empcode=c
        self.empname=n
        Employee.empcount+=1

    def display(self):
        print(self.empcode, self.empname)

    def displaycount(self):
        print(Employee.empcode)


emp1=Employee(201,"Aman")
emp1.display()

emp2=Employee(303,"Parul")
emp2.display()

print(Employee.empcode)