# if = Do some code only IF some condition is True
#      Else do something else

age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to sign up")
elif age < 0:
    print("You haven't been born yet!")
elif age >= 18:
    print("You are sign up!!")
else:
    print("You must be 18+ to sign up")


response = input("Would you like food? (Y/N): ")

if response == "Y":
    print("Have some food!")
else:
    print("No food for you")


name = input("Enter your name: ")

if name == "":
    print("You didn't type in your name!")
else:
    print(f"Hello! {name}!")

online = True
if online:
    print("You are online!")
else:
    print("You are offline")