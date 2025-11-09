# Lambda function = A small anonymous function for a one time use (throw away function)
#                   They take any number of arguments, but have only 1 expression
#                   Helps keep the namespace clean and is useful with higher-order functions
#                   'sort()', 'map()', 'filter()', 'reduce()'
#                   lambda parameters: expression
#                   익명의 한줄 함수 (가독성 높임)

double = lambda x: x * 2
print(double(2))

add = lambda x, y: x + y
print(add(2, 4))

max_val = lambda x, y: x if x > y else y
print(max_val(5, 7))

min_val = lambda x, y: x if x < y else y
print(min_val(6, -2))

full_name = lambda first, last: first + " " + last
print(full_name("janghun", "Yoo"))

is_even = lambda x: x % 2 == 0
print(is_even(4))
print(is_even(5))

age_check = lambda age: True if age >= 18 else False
print(age_check(21))
print(age_check(12))

data = [(1, 'B'), (3, 'A'), (2, 'C')]
data.sort(key=lambda x: x[1])
print(data)

data.sort(key=lambda x: x[0])
print(data)