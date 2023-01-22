class Employee1:
    empcode=101

    def display1(self,n):
        print("Display Employee " + n)
class Employee2:
    empcode=101

    def display2(self,n):
        print("Display Employee " + n)

class HR(Employee1,Employee2):
    empname=""
    def display3(self,n):
        print("Display HR " + n)
        super().display1(n)
        super().display2(n)

HRObj=HR()
HRObj.display3("Aman")