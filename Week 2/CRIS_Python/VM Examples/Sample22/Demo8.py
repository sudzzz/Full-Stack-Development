'''

def myfunction(x):
    return x*x;
print(myfunction(int(input("Enter No"))))

lr1=lambda x:x*x
print(lr1(2))
def myfunction2(x):
    x+=1
    x+=20
    return x*x;

print(myfunction2(int(input("Enter No"))))
'''

lr2=lambda x:(print(x) or x+4)
print(lr2(22))
print("New One")
lr3=lambda x:(x+4,x*x)
print(lr3(3))

