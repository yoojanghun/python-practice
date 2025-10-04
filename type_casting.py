# typecasting = the process of converting a variable from one data type to another
#               str(), int(), float(), str()

name = "Janghun"
age = 24
gpa = 3.2
is_student = True

print(type(name))           # <class 'str'>
print(type(age))            # <class 'int'>
print(type(gpa))            # <class 'float'>
print(type(is_student))     # <class 'bool'>

print()

print(str(age))             # 24 (string)
print(str(gpa))             # 3.2 (string)
print(str(is_student))      # True (string)

print()

print(bool(name))           # True
print(bool(""))             # False
print(bool([]))             # False
print(bool(0))              # False
print(bool(" "))            # True
print(bool(age))            # True
print(bool(gpa))            # True

print()

print(int(gpa))             # 3
print(int(is_student))      # 1
print(int(False))           # 0

print()

print(3 / 5)                # 0.6
print(3 / 5.0)              # 0.6

print()

print(float(age))           # 24.0
print(float(is_student))    # 1.0

print()

age = str(age)              # 24
age += "1"                  # 241
print(age)