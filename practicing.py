# variables(변수) = 데이터를 저장할 공간
# 데이터에는 여러 유형이 있다. (string, integer, float, boolean)
# 데이터의 유형 = data type

# string (= 문자열)
my_name = "Yoo janghun"
print(my_name)
print(f"Hello {my_name}")

# integer (= 정수형)
price = 13
print(price)
print(f"This is {price} dollars")

# float (= 실수형, 숫자 뒤에 소숫점이 포함됨)
price = 13.44
print(price)
print(f"This is {price} dollars")

# boolean (True, false)
is_student = False
print(f"{my_name} is student : {is_student}")

if is_student:
    print("You are a student!!")
else:
    print("You are NOT a student!!")