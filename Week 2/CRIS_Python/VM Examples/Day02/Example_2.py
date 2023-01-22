Info=[]
i=0
while i<2:
    Info.append(input("enter name value"))
    Info.append(input("enter age value"))
    Info.append(input("enter jan sal value"))
    Info.append(input("enter feb sal value"))
    i+=1
print(len(Info))

i=0

while i<2:
    print(Info[i] + Info[i+1]+ Info[i+2]+ Info[i+3])
    i+=1
