str=input("Enter Your Name")
#print(str[0])
#print(str[len(str)-1])

p=0
print(str[0])
while p< len(str):
    if str[p]==' ':
        print(str[p - 1])
        print(str[p+1])
    p+=1

print(str[len(str)-1])