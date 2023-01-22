f=open("MyInfo2.txt","w")
f.write("aman\n")
f.write("mansi\n")
f.close()

f=open("MyInfo2.txt","r")
print(f.readline())
print(f.readline())
print(f.readline())

f=open("MyInfo2.txt","r")
con=f.readlines()
for ln in con:
    print(ln)
