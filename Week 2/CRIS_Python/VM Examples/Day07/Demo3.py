class Employee:
    empcode=101

    def display1(self,n):
        print("Display Employee " + n)

class HR(Employee):
    empname=""
    def display2(self,n):
        print("Display HR " + n)

HRObj=HR()
HRObj.display1("Aman")
HRObj.display2("Rajat")