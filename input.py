# input() = A function that prompts the user to enter data
#           Returns the entered data as a string
#           Return된 data를 이용하기 위해선 변수를 이용한다.

name = input("What is your name?: ")
age = input("How old are you?: ")

print(f"Hello {name}!! You are {age} years old!!")

# age와 name 은 모두 string => string에서 integer로 형변환 하기
age = int(age) + 1

print(f"Hello {name}!! You are {age} years old!!")


length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width

print(f"area is: {area}")

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity

print(f"total ${total}")