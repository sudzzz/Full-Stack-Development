def print_hi2():
    file = open("file2.txt","w")
    name = input("Enter your name : ")

    file.writelines(name)
    file.close()

print_hi2()
