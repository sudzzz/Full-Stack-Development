list=["aa","bb"]
listread=[]
with open(v"file.txt","w")as f1:
    for s in list:
        f1.write(s + ":")
with open("file.txt","r")as f2:
   listread=[line.rstrip(':') for line in f2]
for nm in listread:
    print(nm)