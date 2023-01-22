with open("Mydata.txt", "w") as f:
    f.write("hello")

with open("Mydata.txt", "r") as f:
    print(f.readlines())

file=open("Mydata.txt", "r")
for ln in file:
    print(ln)


