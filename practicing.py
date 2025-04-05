# input() = 사용자로부터 입력 값을 받아 string으로 return 하는 함수
#           입력 값을 이용하기 위해선 변수에 return된 값을 저장

price = float(input("Enter the price : "))
quantity = int(input("Enter the quantity : "))

print(f"The total price is {price * quantity}")

# float와 int를 곱한 결과는 float가 되는 듯 하다.