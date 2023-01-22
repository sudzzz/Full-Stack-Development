info=["welcome","to","welcome","loop"]
name=input("enter new value")
info.append(name)
for n in info:
    print(n)

info.remove("welcome")
print ("after")
for n in info:
    print(n)