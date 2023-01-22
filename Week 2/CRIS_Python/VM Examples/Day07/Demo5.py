class Univ:
    def Accept(self):
        self.RollNo=input("Enter RollNo")
    def Display(self):
        print(self.RollNo)

class College(Univ):
    def Accept(self):
        super().Accept()
        self.CollegeNm=input("Enter College Name")
    def Display(self):
        print(self.CollegeNm)


class Student(College):
    def Accept(self):
        super().Accept()
        self.StdNm = input("Enter Student Name")
    def Display(self):
        print(self.RollNo)


Lst=[]
i=0
while i<3:
    s1=Student()
    s1.Accept()
    Lst.append(s1)
    i+=1

for l in Lst:
    l.Display()