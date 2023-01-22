#### First Program
# income = 45000
# tax_pay = 0
#
# print("Income of Person is ", income)
#
# if income<10000:
#     tax_pay = 0
#
# elif income <=20000:
#     # No tax on first 10,000
#     x = income - 10000
#     # 10% tax
#     tax_pay = 10000 * 10 / 100
#
# else:
#     # first 10,000
#     tax_pay = 0
#
#     # next 10,000
#     tax_pay = 10000 * 10 / 100
#
#     # remaining 20% tax
#     tax_pay += (income - 20000) * 20 / 100
#
# print("Total Tax to be paid is ", tax_pay)
#
#
#
#
# # Second Program
#
# def finallist(list1, list2):
#     result = []
#
#     # Iterating for Odd List
#     for num in list1:
#         if num%2 != 0:
#             result.append(num)
#     # Iterating for Even List
#     for num in list2:
#         if num%2 == 0:
#             result.append(num)
#         return result
#
# list1 = [20, 30, 35, 40, 45]
# list2 = [50, 55, 70, 85, 100]
# print("result final list3 is ", finallist(list1, list2))
#

# Third Program
# print("Print Current and Previous Number and their sum ")
# prev_num = 0
#
# # Loop
# for i in range(1, 11):
#     x_sum = prev_num + i
#     print("Current Number ", i, " Previous Number ", prev_num, " sum: ", x_sum)
#     prev_num = i
#

# Fourth Program
# word = input('Enter Characters')
# print("Complete String is ", word)
#
# name = list(word)
# first = ''
# last = ''
# for i in name[0::2]:
#     first += i
# for i in name[1::2]:
#     last += i
#
# print("Full name is ", first, " ", last)

# Fifth Program
# number = int(input('Enter Number'))
# print("Original Number is ", number)
#
# while number > 0:
#     digit = number % 10
#     number = number // 10
#     print(digit, end=" ")


# Sixth Program
# def validatePassword(password):
#     char_count = 0
#     digit_count = 0
#     special_count = 0
#
#     for char in password:
#         if char.isalpha():
#             char_count += 1
#         elif char.isdigit():
#             digit_count += 1
#         else:
#             special_count += 1
#
#     print("characters = ", char_count, " Digits = ", digit_count, "Special Chars = ", special_count)
#
# password = input("Enter your Password to validate ")
# print("Original Password is ", password)
# validatePassword(password)

# Seventh Program - Removing Special Symbols / Punctuation marks from String
# import string
#
# str_injection = input("Enter String ")
# print("Original String Value ", str_injection)
# replace_char = "~"
# for char in string.punctuation:
#     str_injection = str_injection.replace(char, replace_char)
# print("Replaced Characters String is ", str_injection)
# safe_str = str_injection.translate(str_injection.maketrans('','',string.punctuation))
# print("Safe String is ", safe_str)


# Eight Program - Set from List
# base_val = [1,2,3,4,5,6,7,8,9,10]
# exp_val = [1,4,9,16,25,36,49,64,81,100]
#
# final_pair_data = zip(base_val, exp_val)
# final_set = set(final_pair_data)
# print(final_set)


# Ninth Program
# train_number = [1,2,3,4,5,6,7,8,9,10]
# train_status = {1: 'ontime', 2: 'delayed', 5: 'cancelled', 8: 'ontime'}
# train_status1 = {'ontime': 1, 'delayed': 2, 'cancelled': 5, ' ontime': 8}
#
# train_number[:] = [train for train in train_number if train in train_status.keys()]
# print("Train with Running Status ", train_number)
# train_number[:] = [train for train in train_number if train in train_status1.values()]
# print("Train with Running Status ", train_number)


###############    OOPS   ###############################
# 1. Create a Class with instance variables
import json
from json import JSONEncoder

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

def vehicleDecoder(obj):
        return Vehicle(obj['name'], obj['max_speed'], obj['mileage'])

vehicleObj1 = json.loads('{"name": "Toyota","max_speed": 125,"mileage": 15}',
                         object_hook = vehicleDecoder)
print(vehicleObj1.name, vehicleObj1.max_speed, vehicleObj1.mileage)

class VehicleEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

vehicle = Vehicle("Toyota", 125, 15)
vehicleJSON = json.dumps(vehicle, indent=4, cls=VehicleEncoder)
print(vehicleJSON)
#     def seating_capacity(self, capacity):
#         return f"The Seating Capacity of {self.name} is {capacity} persons"
#
# class Car(Vehicle):
#     def seating_capacity(self, capacity):
#         return super().seating_capacity(capacity)
#
# hondaCar = Car("City", 120, 15)
# print(hondaCar.name, hondaCar.max_speed, hondaCar.mileage)
# print(hondaCar.seating_capacity(7))


######################### JSON ######################################

# data_dictionary = {"key1":"value1", "key2":"value2", "key3":"Value3"}
#
# json_data = json.dumps(data_dictionary)
# print(json_data)
#
# read_json_data = json.loads(json_data)
# print(read_json_data['key2'])

########### Sorting JSON Keys
from setuptools.command.egg_info import write_file
# dict = {"id":1, "name":"himanshu", "age": 10}
# print("writing JSON data in a file with keys sorted")
# with open("data.json", "w") as write_file:
#     json.dump(dict, write_file, indent=4, sort_keys=True)
# print("JSON Writing Done, Please Check JSON File for Output")

