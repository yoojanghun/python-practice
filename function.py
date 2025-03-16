# function = A block of reusable code
#            place () after the function name to invoke(부르다) it
# 코드를 한 번 쓰고 원할 때마다 호출해서 사용

# name, age은 매개변수(parameter) 순서 고려 해야 함.
def happy_birthday(name, age):
    print(f"hello {name}")
    print(f"You are {age} years old!")

# 전달 인자(argument) 보낼 수 있음. 순서 고려 해야 함
happy_birthday("Jang hun", 22)
happy_birthday("Jang hun", 24)
happy_birthday("Jang hun", 34)

def display_invoice(username, amount, due_date):
    print(f"Hello Nice to meet you {username}")
    print(f"Your bill of ${amount:.2f} is due:{due_date}")

display_invoice("Janghun", 42.50, "01/09")

# return = statement used to end a function
#          and send a result back to the caller

def add(x,y):
    z = x + y
    return z
def subtract(x,y):
    z = x - y
    return z
def multiply(x,y):
    z = x * y
    return z
def divide(x,y):
    z = x / y
    return z

print(add(2,3))
print(subtract(2,3))
print(multiply(2,3))
print(divide(2,3))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return  first + " " + last

full_name = create_name("yoo", "janghun")
print(full_name)