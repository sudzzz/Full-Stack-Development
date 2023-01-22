import os
import pandas as pd

def excelReading():
    data = pd.read_excel("training.xlsx")
    print(data)

if __name__ == '__main__':
    excelReading()


# When we get error -> Execution of scripts is disabled on your machine
# Open Power shell in administrator mode and write command "set-executionpolicy remotesigned -scope currentuser"
