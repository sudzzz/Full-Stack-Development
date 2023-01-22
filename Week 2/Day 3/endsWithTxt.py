import os

def myfunction():
    path = os.getcwd()
    print("The current working directory is %s" % path)
    for x in os.listdir():
        if x.endswith(".txt"):
            print(x)

myfunction()