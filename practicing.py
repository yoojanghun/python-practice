# 논리 연산자: 여러 조건들을 계산할 수 있게 하는 연산자 (or, and, not)

# 온도가 너무 덥거나 추우면, 또는 비가 내리면 야외활동 취소
# temp = 25
# is_raining = False
#
# if temp < 0 or temp > 25 or is_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("Have some fun")

temp = 25
is_sunny = False

if temp >= 28 and is_sunny:
    print("It is hot outside and it is sunny")
elif temp <= 0 and is_sunny:
    print("It is cold outside and it is sunny")
elif 0 < temp < 28 and is_sunny:
    print("It is warm outside and it is sunny")
elif temp >= 28 and not is_sunny:
    print("It is hot outside and it is not sunny")
elif temp <= 0 and not is_sunny:
    print("It is cold outside and it is not sunny")
else:
    print("It is warm outside and it is not sunny")