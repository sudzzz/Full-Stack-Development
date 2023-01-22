lst = [10, 20, 30]

def Check(lt):
    s = 0
    for l in lt:
        if(l%2==0):
            s=s+l
    return s

print(Check(lst))