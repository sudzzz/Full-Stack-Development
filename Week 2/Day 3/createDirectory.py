import os

def createDir():
    path = os.getcwd()
    print("The current working directory is ",path)
    os.mkdir("Sudhir")

createDir()