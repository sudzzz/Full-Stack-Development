from abc import ABCMeta,abstractmethod

class first:
    __metaclass__=ABCMeta
    def __init__(self,nm):
        self.nm=nm
    @abstractmethod
    def display(self):
        print("Welcome")

class second(first):
    def display(self):
        print("Hello")

sd=second("aman")
sd.display()



