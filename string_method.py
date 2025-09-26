name = input("Enter your full name: ")  # Bro Code

print(len(name))            # string의 length를 반환하는 function
print(name.find(" "))       # 문자열에서 첫 번째로 나타나는 글자 위치 반환
print(name.find("B"))       # index는 0부터 count
print(name.find("o"))
print(name.rfind("o"))      # 문자열에서 마지막에 나타나는 글자 위치 반환
print(name.find("q"))       # find method는 찾을 수 없는 글자는 -1 반환

print(name.capitalize())    # 문자열 첫 번째 글자만 대문자로, 나머지는 소문자로
print(name.upper())         # 문자열 전체를 다 대문자로
print(name.lower())         # 문자열 전체를 다 대문자로

print(name.isdigit())       # 문자열에 숫자만 있을 때만 True 반환
print(name.isalpha())       # 문자열에 알파벳만 있을 때만 True 반환 (숫자, 빈칸 X)

phone_number = input("Enter your phone number: ")
print(phone_number.count("-"))

print(phone_number.replace("-", " "))

print(help(str))

username = input("Enter username: ")
if len(username) > 12:
    print("Your username is too long")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {username}")