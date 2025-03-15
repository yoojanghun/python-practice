# logical operators = evaluate multiple conditions (or, and, not)
#                     or = at least one condition must be True
#                     and = both conditions must be True
#                     not = inverts the condition (not False, not True)

temp = 69
is_raining = False

if temp > 35 or temp < 0 or is_raining:         # 하나라도 True이면 if 실행
    print("The outdoor event is cancelled")
else:                                           # 모두 False이면 else 실행
    print("The outdoor event is still scheduled")

temp = 25
is_sunny = False

if temp >= 28 and is_sunny:
    print("It is hot outside")
    print("It is sunny")
elif temp <=0 and is_sunny:
    print("It is cold outside")
    print("It is sunny")
elif 0 < temp < 28 and is_sunny:
    print("It is Warm outside")
    print("It is sunny")
elif temp >= 28 and not is_sunny:
    print("It is hot outside")
    print("It is cloudy")
elif temp <=0 and not is_sunny:
    print("It is cold outside")
    print("It is cloudy")
elif 0 < temp < 28 and not is_sunny:
    print("It is Warm outside")
    print("It is cloudy")