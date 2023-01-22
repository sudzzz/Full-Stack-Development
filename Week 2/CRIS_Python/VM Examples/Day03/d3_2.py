def MyFunction(i, j):
    s = 0
    while (i < j):
        s = s + i
        i += 1
    return (s)


def EvenOdd(no):
    if no % 2 == 0:
        print("Even")
    else:
        print("Odd")


res=MyFunction(2, 10)
print(res)
EvenOdd(res)
#EvenOdd(MyFunction(2, 10))

# MyFunction(input("Enter Your name"),2,10)
