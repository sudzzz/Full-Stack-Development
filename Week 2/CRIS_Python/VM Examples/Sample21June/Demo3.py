class Employee:
    empcode=101
    def display2(self,n):
        print("In Display"+ n)

class HR(Employee):
    empname=""
    def display(self):
        print("In Display")


HRObj=HR()
HRObj.display()
HRObj.display2("Aman")