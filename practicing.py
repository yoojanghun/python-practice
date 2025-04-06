# keyword 인자 = 인자 앞에 함수 매개변수에 해당하는 변수 이름을 작성함
# 가독성이 좋아짐. 인자의 순서가 중요하지 않게 됨.
# keyword 인자와 default parameter는 둘 다 positional 뒤에 와야 함.

def hello(greeting, title, first, last):
    print(f"{greeting}, {title} {first} {last}")

hello(greeting="hello", title="Mr.", first="Yoo", last="Janghun")

# print에서 두 번째 인자인 end=" "는 사실 keyword argument이다.
for x in range(1, 11):
    print(x, end=" ")

print("1", "2", "3", "4", "5", sep="---")

