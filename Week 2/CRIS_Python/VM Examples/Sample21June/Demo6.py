class Checking:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __add__(self, other):
        return (self.a+other.a)

ch1=Checking(2,10)
ch2=Checking(3,4)
print(ch1+ch2)