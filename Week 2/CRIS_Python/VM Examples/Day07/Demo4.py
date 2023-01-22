class Employee:
    empcode=101

    def display(self,n):
        print("Display Employee " + n)

class HR(Employee):
    empname=""
    def display(self,n):
        print("Display HR " + n)
        super().display(n)

HRObj=HR()
HRObj.display("Aman")
HRObj.display("Rajat")