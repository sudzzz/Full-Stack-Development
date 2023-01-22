#Exception Handling

try:
    no1=int(input("Enter No1"))
    no2=int(input("Enter No2"))
    print(no1 / no2)
except ZeroDivisionError:
    print("Division Error")
finally:
    print("Thanks")
