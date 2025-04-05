# python 에서 이용 가능한 수학적 표현
import math

number = 3
# number = number + 4
# number += 4
# number -= 2
# number /= 2.3
# number %= 2
# number **= 4
# number *= 4
# print(number)

x = 3.2
y = -4.6
z = 2

print(max(x, y, z))
print(round(x), round(y))   # 반올림
print(abs(y))               # 절댓값
print(pow(x, z))

print(math.ceil(x))
print(math.floor(y))

print(round(math.pi, 6))