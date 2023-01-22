import string
import re

str_injection = input("Enter String ")
print("Original String value ",str_injection)

# safe_str = str_injection.translate(str_injection.maketrans('@','?',string.printable))
# print("Safe String is ",safe_str)

replace_char = "~"

for char in string.punctuation:
    str_injection = str_injection.replace(char,replace_char)
print("Replaced Charater String is ",str_injection)
