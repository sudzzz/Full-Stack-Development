#Exception Handling
def MyCheck(no1,no2):
    if(no1>no2):
        raise "Invalid Input"
    else:
        print(no1+no2)

try:
    no1=int(input("Enter No1"))
    no2=int(input("Enter No2"))
    MyCheck(no1,no2)
except:
    print("Error In Function")
finally:
    print("Thanks")
