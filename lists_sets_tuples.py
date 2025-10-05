# collection = single "variable" used to store multiple values
#   List     = [] ordered(인덱스 쓸 수 O) and changeable(Add/Remove OK). Allows duplicate members. (index-value pairs)
#   Tuple    = () ordered and unchangeable(수정 불가). Allows duplicate members. FASTER (index-value pairs, list인데 변경 X)
#             list에서 수정 삭제 메소드 빼면 tuple의 메소드
#   Set      = {} unordered(인덱스 못 씀) and changeable(Add/Remove OK). NO duplicates(같은 원소 여러개 써도 하나로 취급)
# Dictionary = A set of key-value pairs. A collection which is unordered but indexed, and changeable.
#              No duplicate members (set인데 key-value 쌍)

fruits = ["apple", "orange", "banana", "coconut"]

print(fruits)
print(fruits[0])        # 개별 요소 print
print(fruits[3])

# 처음 ~ 3번째까지 print
print(fruits[0:3])      # 배열로 print
print(fruits[:3])

for fruit in fruits:
    print(fruit)

# collection에서 이용 가능한 method를 찾기 위해선
# print(dir(fruits))
#
# collection에서 각 methods의 설명을 찾기 위해선
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

print()

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

print()

fruits = ('pineapple', 'orange', 'coconut', 'banana', 'apple')

print(fruits)
print(fruits[0])
print(fruits.index("coconut"))
print(fruits.count("coconut"))

# fruits[0] = "chicken"
# print(fruits[0]) 이렇게 바꾸는 것 불가능

print()

# constructor(생성자)
# 파이선의 list(), set(), tuple()은 내장함수로,
# 다른 자료형을 해당 컬렉션 타입으로 변환(생성)할 때 사용
thislist1 = list(("apple", 1, True))
thislist2 = list()
thislist3 = list("hello")
print(thislist1)
print(thislist2)
print(thislist3)

print()

thistuple1 = tuple(("banana", 2, False))
thistuple2 = tuple()
thistuple3 = tuple("nice to meet you")
thistuple4 = tuple([1, 2, 3])           # list를 tuple로 변환
print(thistuple1)
print(thistuple2)
print(thistuple3)
print(thistuple4)

print()

thisset1 = set(("coconut", 3, True))
thisset2 = set()
thisset3 = set("great")
thisset4 = set([1, 1, 2, 3, 3,])        # list를 set으로 변환
print(thisset1)
print(thisset2)                         # set() 이라고 출력됨
print(thisset3)
print(thisset4)