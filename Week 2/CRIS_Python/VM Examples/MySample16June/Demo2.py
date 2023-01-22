f=open("Mydata2.txt", "w")
f.write("123456")
f.close()

f=open("Mydata2.txt", "r")
f.seek(3)
print(f.read())

