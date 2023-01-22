contacts={
    'Rajat':{'phone':'99944455','addr':'LA'},
'Parul':{'phone':'999999888','addr':'NY'},
'Mansi':{'phone':'998282222','addr':'DL'}
}

name=input("Enter Searched Name")
Request=input("Phonenumber(p) or address (a)")

if Request == 'p':
    k='phone'
if Request == 'a':
    k='addr'

if name in contacts:
    print(contacts[name][k])

