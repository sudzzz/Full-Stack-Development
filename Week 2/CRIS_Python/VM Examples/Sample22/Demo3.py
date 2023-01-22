#iterators

class Check:
    def __init__(self,mx):
        self.mx=mx

    def __iter__(self):
        self.a=0
        self.b=1
        return  self

    def next(self):
        tmp=self.a
        if(tmp>self.mx):
            raise StopIteration

        self.a,self.b=self.b,self.a+self.b
        return tmp


for i in Check(10):
    print(i)