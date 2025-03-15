# Variable = A container for a value (data type: string, integer, float boolean)
#            A variable behaves as if it was the value it contains

# Strings (문자열)
first_name = "Yoo"
print("first_name")
print(first_name)
print(f"Hello mr.{first_name}\n") # text와 변수를 함께 쓰는 방법

#integer (= whole number)
my_age = 24
print(f"you are {my_age} year old\n")

# float
price = 10.99
print(f"The price is ${price}\n")

# Boolean (True False)
is_student = True
print(f"Are you a student? :{is_student}")

if is_student:
    print("You are a student!!\n")
else:
    print("you are not a student\n")