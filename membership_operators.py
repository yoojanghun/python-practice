# Membership operators = used to test whether a value or variable is found in a sequence
#                        값이나 변수가 안에 있니?
#                        (string, list, tuple, set, dictionary)
#                        1. in
#                        2. not in

word = "APPLE"

letter = input("Guess a letter in the secrete word: ")

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")

if letter not in word:
    print(f"{letter} was not found")
else:
    print(f"There is a {letter}")

print()

students = {"kim", "park", "yoo"}

student = input("Enter the name of the student: ")

if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} was not found")

print()

user = {
    "name": "janghun",
    "age": 23,
    "is_student": True
}

info = input("Enter user info: ")

if info in user:                        # dictionary에서 in은 key를 검사
    print(f"{info} is a key of user")
    print(f"the value is: {user.get(info)}")
else:
    print(f"{info} is not a key of user")

print()

email = "yoojanghun@naver.com"

if "@" in email and "." in email:
    print("Valid Email")
else:
    print("Invalid Email")