import random

# 1 이상 6 이하 난수
number = random.randint(1, 6)
print(number)

# 0이상 1미만 random float number
number = random.random()
print(number)

options = ("rock", "paper", "scissors")
option = random.choice(options)
print(option)

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(cards)
print(cards)

print()

# number guessing game (my version)
lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0

print("Python number guessing game")
num = 0
while num != answer:
    num = input(f"Select a number between {lowest_num} and {highest_num}: ")
    if num.isdigit():
        num = int(num)
        if num < lowest_num or num > highest_num:
            print("That was invalid answer")
            num = input(f"Select a number between {lowest_num} and {highest_num}: ")
        elif num < answer:
            print(f"your num {num} is too low")
            guesses += 1
        else:
            print(f"your num {num} is too high")
            guesses += 1
    else:
        print("That was invalid answer")
        num = input(f"Select a number between {lowest_num} and {highest_num}: ")

print()
print(f"your answer = {num}, computer answer = {answer}")
print(f"guesses count: {guesses}")

# number guessing game (bro code version)
lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Python number guessing game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    num = input("Enter your guess: ")

    if num.isdigit():
        num = int(num)
        guesses += 1

        if num < lowest_num or num > highest_num:
            print("That number is out of range")
            print(f"Select a number between {lowest_num} and {highest_num}")
        elif num < answer:
            print("Too low")
        elif num > answer:
            print("Too High")
        else:
            print(f"Correct! the answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False

    else:
        print("Invalid Guess")
        print(f"Select a number between {lowest_num} and {highest_num}")