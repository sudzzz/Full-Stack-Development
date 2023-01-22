class Student:
    stdcount=0

    def __init__(self,c,n):
        self.stdcode=10
        self.stdname=20
        Student.stdcount+=1

    def display(self):
        print(self.stdcode,self.stdname)

    def displaycount(self):
        print(Student.stdcount)


##MAIN

std1=Student(202,"Aman")
std1.display()

std2=Student(203,"Parul")
std2.display()


print("Std Counter ", Student.stdcount)

Student.stdcount=10
print("Std Counter ", Student.stdcount)