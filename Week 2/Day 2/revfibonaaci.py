val = input("Enter the number for reverse fibonaaci ")
val = int(val)

list1= []
list1.append(0)
list1.append(1)

for i in range(2,val):
    ele = list1[i-1]+list1[i-2]
    list1.append(ele)
    

list2 = []
# sum = list1[1]+list1[0]
sum = 2
print(list2)
for i in range(0,val) :
    if(i<2):
        list2.append(list1[i])
    else:
        list2.append(sum)
        
        ele = list1[i]+list2[i-1]
        list2.append(ele)

print(list1)
print(list2)


list3 =[]
sum_i = 0
for i in list1:
  sum = 0
  if (i<2):
    list3.append(i)
  else:
      for j in range(0,i):
          sum += list1[i] 
          list3.append(sum)
    
      
print(list3)