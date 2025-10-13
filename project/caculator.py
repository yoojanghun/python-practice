# print(3 / 5) 는 0.6
# print(3 / 5.0) 도 0.6으로 동일하게 출력됨

# 아래에서 float 대신 int로 형변환 하면 소숫점이 버려짐
operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    print(round(num1 + num2, 2))
elif operator == "-":
    print(round(num1 - num2, 2))
elif operator == "*":
    print(round(num1 * num2, 2))
elif operator == "/":
    print(round(num1 / num2, 2))
else:
    print(f"{operator} is unvalid operator")