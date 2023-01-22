val = int(input())
print(val)
rev = 0
while(val!=0):
    digit = val%10
    rev = rev*10 + digit
    val //= 10

print(rev)
