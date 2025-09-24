# 2d list = collection made of collections

fruits =     ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats =      ["chicken", "fish", "turkey"]

groceries1 = [fruits, vegetables, meats]

print(groceries1)
print(groceries1[0])         # 전체 0행 출력
print(groceries1[0][2])      # 0행 2열 출력 [행][열]

print()

# 아래처럼 해도 된다
groceries2 = [["apple", "orange", "banana", "coconut"],
              ["celery", "carrots", "potatoes"],
              ["chicken", "fish", "turkey"]]

for i in range(len(groceries2)):
    for j in range(len(groceries2[i])):
        print(groceries2[i][j])

print()

for collection in groceries2:
    for food in collection:
        print(food, end=" ")
    print()

print()

# list 대신 set, tuple 등을 사용해도 된다
num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for numbers in num_pad:
    for number in numbers:
        print(number, end=" ")
    print()