def MyFunction(i, j):
    s = 0
    while (i < j):
        s = s + i
        i += 1
   # print(s)
    EvenOdd(s)

def EvenOdd(no):
    if no % 2 == 0:
        print("Even")
    else:
        print("Odd")

MyFunction(2, 10)
# MyFunction(input("Enter Your name"),2,10)
