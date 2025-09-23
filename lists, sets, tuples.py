# collection = single "variable" used to store multiple values
#   List    = [] ordered(인덱스 쓸 수 O) and mutable(Add/Remove OK). Duplicates OK(같은 원소 2개 쓸 수 있음)
#   Set     = {} unordered(인덱스 못 씀) and mutable(Add/Remove OK). NO duplicates(같은 원소 여러개 써도 하나로 취급)
#   Tuple   = () ordered and immutable(수정 불가). Duplicates OK. FASTER

# List = A collection which is ordered and changeable (index-value pairs). Allow duplicate members.
# Tuple = A collection which is ordered and unchangeable (index-value pairs). Allows duplicate members. (list인데 변경 X)
# Set = A collection which is unordered and changeable (values only). no duplicate members.
# Dictionary = A set of key-value pairs. A collection which is unordered but indexed, and changeable.
#              No duplicate members (set인데 key-value 쌍)

fruits = ["apple", "orange", "banana", "coconut"]

print(fruits)
print(fruits[0])
print(fruits[3])

# 처음 ~ 3번째까지 print
print(fruits[0:3])
print(fruits[:3])

for fruit in fruits:
    print(fruit)

# # collection에서 이용 가능한 method를 찾기 위해선
# print(dir(fruits))
#
# # collection에서 각 methods의 설명을 찾기 위해선
# print(help(fruits))

print(len(fruits))

# in 연산자는 list 안에 요소가 있는 지 확인하는 것 (True False 반환)
print("apple" in fruits)

# changeable
fruits[0] = "pineapple"

for fruit in fruits:
    print(fruit)

# list 마지막에 요소를 append 하기 위한 method
fruits.append("melon")
print(fruits)

# list에서 요소 없애는 method
fruits.remove("melon")
print(fruits)

# list에서 특정 index에 요소를 끼워 넣는 method. 나머지 요소는 한 칸씩 밀림.
fruits.insert(1, "apple")
print(fruits)

# 요소들을 정렬 (알파벳 순)
fruits.sort()
print(fruits)

# 요소들의 순서를 거꾸로
fruits.reverse()
print(fruits)

# 모든 요소 clear
fruits.clear()
print(fruits)

fruits = ['pineapple', 'orange', 'coconut', 'banana', 'apple']

# 요소들의 index 반환
print(fruits.index("pineapple"))

# 요소들의 수 찾기
print(fruits.count("pineapple"))

fruits = {'pineapple', 'orange', 'coconut', 'banana', 'apple'}
print(fruits)

# set의 모든 attributes와 method를 확인하려면
# print(dir(fruits))
# print(help(fruits))

# fruits[0] 인덱스 사용 불가
fruits.add("melon")
print(fruits)

fruits.remove("melon")
print(fruits)

# pop method는 가장 처음 요소를 삭제
fruits.pop()
print(fruits)

# fruits.clear()

fruits = ('pineapple', 'orange', 'coconut', 'banana', 'apple')

print(fruits)
print(fruits[0])

# fruits[0] = "chicken"
# print(fruits[0]) 이렇게 바꾸는 것 불가능