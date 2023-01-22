class Checking:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __add__(self, other):
        self.a=self.a+other.a;
        return  (self)

    def DispA(self):
        print(self.a)
Ch1=Checking(2,10)
Ch2=Checking(3,20)
Ch4=Checking(1,20)

Ch1+Ch2+Ch4
print(Ch1.a)
print(Ch1.DispA())
