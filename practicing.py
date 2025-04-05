age = int(input("Enter your age : "))

if age < 0:
    print("You haven't been born yet")
elif 0 <= age < 18:
    print("You must be 18+ to sign up")
elif 18 <= age < 100:
    print("You are signed up!!")
else:
    print("You are too old to sign up!!")

response = input("Would you like food? (Y/N) : ")

if response == "Y" or response == "y":
    print("Have some food")
else:
    print("No food for you")