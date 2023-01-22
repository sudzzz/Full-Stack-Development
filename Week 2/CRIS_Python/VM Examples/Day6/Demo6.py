def MyCheck(no1,no2):
    if(no1>no2):
        raise "Invalid Input"
    else:
        print(no1+no2)

try:
    no1=int(input(""))
    no2=int(input(""))
    MyCheck(no1,no2)
except:
    print("Error")
finally:
    print("Thanks")