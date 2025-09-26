import math

# 연산자: +, -, *, /, **, %
friends = 0

friends = friends + 4   # 4
friends += 1            # 5
friends -= 2            # 3
friends *= 3            # 9
friends /= 3            # 3
friends **= 2           # 9
friends %= 2            # 1

print(friends)

# built-in math related functions:
x = 3.5
y = -4
z = 5

resultx = round(x)  # 반올림
print(resultx)

resulty = abs(y)
print(resulty)

print(pow(4, 3))

print(max(x,y,z))   # maximum value 찾음
print(min(x,y,z))

# import math 하면 math 모듈을 사용해 더 복잡한 함수나 상수들을 이용 가능
# 모듈이란 함수나 변수 또는 클래스를 모아 놓은 파이썬 파일이다.
# 모듈은 다른 파이썬 프로그램에서 불러와 사용할 수 있도록 만든 파이썬 파일이라고도 할 수 있다.
print(math.pi)
print(math.e)
print(math.sqrt(9))
print(math.ceil(3.13))  # 올림
print(math.floor(3.93)) # 버림

radius = float(input("Enter the radius of a circle: "))
circumference = 2 * math.pi * radius
area = math.pi * pow(radius, 2)

print(f"The circumference is: {circumference}")
print(f"The circumference is: {round(circumference, 2)}")   # 소숫점 2자리만 나타내도록 반올림

print(f"The area is: {area}cm^2")
print(f"The area is: {round(area, 3)}cm^2")     # 소숫점 3자리만 나타내도록 반올림