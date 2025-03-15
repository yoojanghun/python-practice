# input() = A function that prompts the user to enter data
#           Returns the entered data as a string

name = input("What is your name?: ")
age = input("How old are you?: ")

# age와 name 은 모두 string

age = int(age) + 1

print(f"Hello {name}!!")
print(f"You are {age} years old")

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width

print(f"area is: {area}")

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity

print(f"total ${total}")