# typecasting(형변환) = 하나의 data type을 다른 type으로 변형하는 것
#                      int(), float(), str(), bool()

my_name = "Yoo Janghun"
grade = 100
gpa = 3.8
is_student = True

# 각 변수의 data type을 type()함수를 이용 하여 확인할 수 있다.
print(type(is_student))

print(int(gpa))     # float를 int로 형변환 할 때, 소숫점 아래 자리는 버림함.

print(float(grade))

print(bool(my_name))

your_name = input("Enter your name = ")

if your_name:
    print(f"Hello!! {your_name}!!")
else:
    print("You didn't write your name!!")

# 아무것도 입력하지 않았을 때는 your_name엔 ""가 저장된다!!