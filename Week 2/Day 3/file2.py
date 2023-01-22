def reading1():
    file = open("file3.txt","r+")
    print("File name is ",file.name)

    contents = file.readlines()

    for line in contents:
        print(line)
    file.close()


def reading2():
    file = open("file3.txt","r+")
    print("File name is ",file.name)

    contents = file.readline()

    while(contents):
        print(contents)
        contents = file.readline()
    file.close()

reading1()
reading2()