# while loop = execute some code WHILE some condition remains true

name = input("Enter your name: ")

while name == "":
    print("You didn't enter your name")
    name = input("Enter your name: ")

print(f"Hello!! {name}!!")

age = int(input("Enter your age: "))

while age < 0:
    print("Your age must be positive value")
    age = int(input("Enter your age: "))

print(f"Your age is {age} years old")

food = input("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"you like {food}")
    food = input("Enter a food you like (q to quit): ")

print("Bye!!")

num = int(input("Enter a # between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1 - 10: "))

print(f"Your number is {num}")