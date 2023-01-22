lst=["India","Australia",2000]
for lstvalue in lst:
    print(lstvalue)

lst.append("Pakistan")
for lstvalue in lst:
    print(lstvalue)

lst[3]="WestIndies"
for lstvalue in lst:
    print(lstvalue)

del lst[2]
for lstvalue in lst:
    print(lstvalue)