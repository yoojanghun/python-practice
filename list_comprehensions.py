# list comprehension = A concise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]
from math import sqrt

doubles = []
for x in range(1, 11):
    doubles.append(x * 2)

print(doubles)

print()

doubles = [x * 2 for x in range(1, 11)]
print(doubles)

print()

triples = [y * 3 for y in range(1, 11)]
print(triples)

print()

roots = [round(sqrt(z), 2) for z in range(1, 11)]
print(roots)

print()

fruits = ['apple', 'orange', 'coconut', 'banana']
fruits = [fruit.upper() for fruit in fruits]
print(fruits)

print()

fruits = ['apple', 'orange', 'coconut', 'banana']
fruits = [fruit[0] for fruit in fruits]
print(fruits)

print()

numbers = [1, -2, 3, -4, 5, -6, 8, -7]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2]
print(positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)

print()

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)

# y = 4
# x = 3 if y % 2 else 5
# print(x)