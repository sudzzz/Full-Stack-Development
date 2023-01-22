#User defined exception with class

class HarmeetException(Exception):
    def __init__(self,msg):
        self.args=msg

try:
    no1=int(input("Enter First No"))
    no2=int(input("Enter Second No"))
    if(no1>no2):
        raise HarmeetException("Not Possible")
except HarmeetException:
    print("Harmeet Your Exception caught")


