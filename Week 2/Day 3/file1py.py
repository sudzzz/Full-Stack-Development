def reading():
    file = open("file3.txt","r+")
    print("File name is ",file.name)

    contents = file.readlines()

    print(contents[0])
    file.close()

reading()