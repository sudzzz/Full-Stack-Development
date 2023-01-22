str=input("Enter Your Name")

count={x:sum([1 for char in str if(char==x)]) for x in 'abcdef'}
print(count)

count={x:sum([1 for char in str if(char ==x)])
       for x in 'aeiou'}
print(count)