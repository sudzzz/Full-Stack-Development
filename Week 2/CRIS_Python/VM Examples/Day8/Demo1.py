class HarmeetException(Exception):
    def __init__(self,msg,un):
        raise HarmeetException("Invalid Values",uname)
except HarmeetException:
    print("Your Exception Caught")



