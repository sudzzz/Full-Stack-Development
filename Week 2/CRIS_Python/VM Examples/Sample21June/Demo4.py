class SalesEmployee:
    Salesempcode=101
    def display1(self):
        print("In Sales Display")

class AccountsEmployee:
    Accountsempcode=101
    def display2(self):
        print("In Account Display")

class HR(SalesEmployee,AccountsEmployee):

    def display3(self):
        print("In HR Display")
        super().display2()


HRObj=HR()
HRObj.display1()
HRObj.display2()
HRObj.display3()