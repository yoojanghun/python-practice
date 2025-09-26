# Iterables = An object/collection that can return its elements one at a time,
#             allowing it to be iterated over in a loop
from dis import print_instructions

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number, end=" ")

print()

for number in reversed(numbers):
    print(number, end=" ")

print()

numbers = (1, 2, 3, 4, 5)

for number in numbers:
    print(number, end=" ")

print()

fruits = {"apple", "banana", "orange", "coconut"}

for fruit in fruits:        # set이라 순서가 없어서 print는 랜덤
    print(fruit, end=" ")            # reversed(fruits)는 안됨

print()

name = "Yoo Janghun"

for char in name:
    print(char, end=" ")

print()

user = {
    "name": "janghun",
    "age": 23,
    "is_student": True
};

for info in user:
    print(info, end=" ")

print()

for info_val in user.values():
    print(info_val, end=" ")

print()

for info_key in user.keys():
    print(info_key, end=" ")

print()

for info_key, info_val in user.items():
    print(f"{info_key} : {info_val}")

print()

print(user.items())     # dict_items([('name', 'janghun'), ('age', 23), ('is_student', True)])