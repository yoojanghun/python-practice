# *args     = allows you to pass multiple non-key arguments
# **kwargs  = allows you to pass multiple keyword-arguments
#            * unpacking operator

def add_type(*args):
    print(type(args))           # tuple

add_type(1, 2, 3, 4)

def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(add(1, 2, 3))
print(add(1, 2, 3, 4, 5))
print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

print()

def display_num(*names):
    for name in names:
        print(name, end=" ")
    print()

display_num("Dr.", "Spongebob", "SquarePants")

print()

def print_address_type(**kwargs):
    print(type(kwargs))          # dictionary

print_address_type(street="123 fake St.",
                   city="Detroit",
                   state="MI",
                   zip="54321")

print()

def print_address(**kwargs):
    for value in kwargs.values():
        print(value)
    print()
    for key, value in kwargs.items():
        print(f"{key} : {value}")
    print()

print()

print_address(street="123 fake St.",
              city="Detroit",
              state="MI",
              zip="54321")

# dictionary = {
#     "name": "janghun",
#     "age": 23,
#     "is_student": True
# }
# print(dictionary.values())
# for value in dictionary.values():
#     print(value)
#
# print()

# **kwargs, *args 순서로 파라미터 받으면 동작 오류
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")

    print()

    if "apt" in kwargs:         # apt를 인자로 넘기지 않았을 때 None이 출력됨
        print(f"{kwargs.get("street")} {kwargs.get("apt")}")
    else:
        print(f"{kwargs.get("street")}")

    print(f"{kwargs.get("city")} {kwargs.get("zip")}")

shipping_label("Dr.", "Spongebob", "Squarepants", "III",
               street="123 fake St.",
               apt="100",
               city="MI",
               zip="54321")