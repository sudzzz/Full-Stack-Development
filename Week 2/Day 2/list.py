def finallist(list1,list2):
    result = []
    
    for val1 in list1:
        if(val1%2 != 0):
            result.append(val1)
    
    for val2 in list2:
        if(val2%2 == 0):
            result.append(val2)

    return result
        
    

list1 = [20,30,35,40,45]
list2 = [50,55,70,85,100]

print("result final list3 is ",finallist(list1,list2))