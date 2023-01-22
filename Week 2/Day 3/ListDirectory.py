import os
def directoryList():
    path = os.getcwd()
    dir_list = os.listdir(path+"/Sudhir")
    print("Files and directories in '",path,"' : ")
    print(dir_list)

if __name__ == '__main__':
    directoryList()