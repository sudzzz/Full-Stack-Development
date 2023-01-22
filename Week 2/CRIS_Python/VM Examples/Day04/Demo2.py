with open("MyData2.txt","a") as f:
    #f.write("welcome")
    f.write("To File Handling")
    f.close()

f=open("MyData2.txt","r")
for ln in f:
    print(ln)

