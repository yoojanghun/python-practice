# keyword argument = an argument preceded by an identifier(식별자가 앞에 붙은 인자)
#                    helps with readability
#                    order of arguments doesn't matter

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello", "Mr.", "Janghun", "Yoo")

# 인자 앞에 title=를 붙이면 인자의 순서가 바뀌어도 된다.
hello(title="Mr.", last="Yoo", first="Janghun", greeting="Hello")

# 일반 인자와 keyword argument를 같이 쓰는 경우엔 일반 인자를 먼저 써야 한다.
hello("Hello", title="Mr.", last="Yoo", first="Janghun")

# end도 사실 keyword argument임.
for x in range(1, 11):
    print(x, end=" ")

# print와 같이 이미 만들어진 function에는 사용 가능한 keyword argument가 있음
print("1", "2", "3", "4", "5", sep="-")

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1, area=123, first=456, last=789)
print(phone_num)