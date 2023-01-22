f=open("MyInfo.txt","w")
f.write("aman verma")
f.close()

f=open("MyInfo.txt","r")
f.seek(2)
print(f.read())