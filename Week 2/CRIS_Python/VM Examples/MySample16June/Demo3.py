def process(s):
    print(s)

f=open("Mydata2.txt", "r")
ch=f.read(1)
while ch:
    process(ch)
    ch=f.read()


