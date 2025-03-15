# for loops = execute a block of code a fixed number of times.
#             You can iterate over a range, string, sequence, etc.

# 1부터 10까지 count
for x in range(1, 11):
    print(x)

print("Happy new year!")

# 10부터 1까지 count
for x in reversed(range(1, 11)):
    print(x)

print("Happy new year!")

# 1부터 10까지 2칸 간격으로 count
for x in range(1, 11, 2):
    print(x)

print("Happy new year!")

# 문자열도 반복 가능함
credit_card = "1234-456-789-156"

for x in credit_card:
    print(x)

# 반복문에서 건너 뛰려면 continue 사용 (아래에서 13 건너뜀)
for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)

# 반복문을 빠져나오려면 break 사용
for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)