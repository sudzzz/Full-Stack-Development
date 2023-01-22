val = input("Enter String ")

print("Complete String is ",val)

name = list(val)

firstname = ""
lastname = ""

for i in range(0,len(name)):
    if(i%2==0):
        firstname = firstname + name[i]
    else:
        lastname = lastname + name[i]

print(firstname,lastname)