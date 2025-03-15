# Typecasting = the process of converting from one data type to another
#               str(), int(), float(), bool()

name = "Yoo Janghun"
age = 24
gpa = 3.2
is_student = True

type(name)
print(type(is_student))

gpa = int(gpa)
print(gpa)          # 3

gpa += 1
print(gpa)          # 4

age = float(age)
print(age)          # 24.0

age = str(age)
print(type(age))    # "24.0

age += "1"
print(age)          # "24.01"

name = bool(name)
print(name)        # string 안에 값이 있으면 True

hi = ""
hi = bool(hi)
print(hi)          # 값이 없으면 False