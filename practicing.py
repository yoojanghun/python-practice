# 집합형 자료구조 = 여러 값들을 저장하기 위한 하나의 변수

# list  = 내가 아는 그 배열. 인덱스 있고, 요소 갱신(추가, 삭제, 수정) 가능, 중복 가능
# set   = 내가 아는 그 집합. 인덱스 없고, 요소 수정 불가. 하지만 추가나 삭제는 가능, 중복 불가능
# tuple = 인덱스는 있음. 하지만 요소 갱신(추가, 삭제, 수정) 불가능. 중복 가능

# 그냥 list, set은 내가 아는 배열, 집합이고 나머지 tuple만 외우면 됨.
# tuple은 갱신만 불가능. 나머진 다 있음. 인덱스도 있고, 중복도 가능함.

# list
# fruits = ["apple", "banana", "orange", "coconut", "coconut"]

# print(fruits[::-1])

# for fruit in fruits:
#     print(fruit)

# fruits.append("pineapple")
# fruits.remove("apple")
# fruits[0] = "pineapple"
# print(len(fruits))
# print(fruits.count("coconut"))
# fruits.sort()
# fruits.reverse()
# fruits.insert(4, "pineapple")
# fruits.clear()

# fruits = {"apple", "orange", "coconut", "banana"}
# fruits.add("pineapple")
# fruits.remove("apple")
# fruits.pop()
# print("apple" in fruits)
# print(len(fruits))

# fruits = {"apple", "orange", "coconut", "banana", "banana"}

fruits = ("apple", "apple", "orange", "coconut", "banana")

# print(fruits.index("apple"))
# print(fruits.index("coconut"))
print(fruits.count("apple"))

print(fruits)