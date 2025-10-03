# split() = 문자열을 일정한 기준(구분자)으로 잘라서 list 형태로 반환하는 메서드
#           문자열.split(구분자, 최대분할횟수)

# 구분자(선택) = 문자열을 어디서 잘라낼지 기준. default값은 공백(스페이스, 탭, 개행문자 등)
# 최대분할횟수(선택) = 몇 번만 분리할 지 정함. (지정하지 않으면 끝까지 분리)

text = "Python is fun"
result = text.split()
print(result)

csv_data = "apple,banana,grape"
csv_result = csv_data.split(",")
print(csv_result)

sentance = "one two three four"
sentance_result = sentance.split(" ", 2)    # ['one', 'two', 'three four']
print(sentance_result)

data = "2025-10-03"
year, month, day = data.split("-")
print(f"{year}년 {month}월 {day}일")

fruit1, fruit2, fruit3 = ["apple", "banana", "orange"]
print(fruit1, fruit2, fruit3)