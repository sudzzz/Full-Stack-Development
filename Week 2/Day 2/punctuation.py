import string
str_injection = input("Enter String ")
print("Original String Value ",str_injection)

safe_str = str_injection.translate(str_injection.maketrans('','',string.punctuation))
print("Safe String is ",safe_str)

