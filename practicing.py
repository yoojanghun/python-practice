# while loop  = 어떤 조건이 참일 때, 코드를 계속 실행시킴.

name = input("Enter your name : ")

while name == "":
    print("You didn't write your name")
    name = input("Write your valid name : ")

print(f"Hello!! {name}!!")

food = input("Enter the food you like (q to quit) : ")

while not food == "q":
    print(f"You like {food}!!!")
    food = input("Enter another food (q to quit) : ")

print("Bye")

age = int(input("Enter your age : "))

while age < 0:
    print("Your age is not valid")
    age = int(input("Enter your age again: "))

print(f"You are {age} years old")

number = int(input("Write your number from 1 to 10 : "))

while number < 1 or number > 10:
    print("Your number is not valid")
    number = int(input("Write your number again : "))

print(f"Your number is : {number}")