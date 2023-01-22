f=open("MyInfo3.txt","w+")
f.write("aman\n")
f.write("mansi\n")

f.seek(0)
con=f.readlines()
for ln in con:
    print(ln)
