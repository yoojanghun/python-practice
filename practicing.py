# for loop = 우리가 원하는 숫자 만큼 코드를 실행

for counter in range(1, 11, 3):
    print(counter)

for x in range(10, 0, -1):
    print(x)

credit_card = "1234-5678-9"

for x in credit_card:
    print(x)

# continue와 break
# continue : loop 중간에 건너뜀
# break : loop를 빠져나옴

for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)

for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)