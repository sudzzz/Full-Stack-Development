with open("MyData1.txt","w") as f:
    f.write("welcome")
    f.write("To File Handling")
    f.close()


with open("MyData1.txt","r") as f:
    print(f.readlines())
    f.close()


f=open("MyData1.txt","r")
for ln in f:
    print(ln)

