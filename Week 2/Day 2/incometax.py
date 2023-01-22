income = input("Enter income : ")
income = int(income)
tax = 0

if (income > 10000 and income < 20000 ) :
    income = income - 10000
    tax = tax + 0.1*income

if (income > 20000) :
    tax = tax + 1000
    income = income - 20000
    tax = tax + 0.2*income

print("Income Tax is ", tax)