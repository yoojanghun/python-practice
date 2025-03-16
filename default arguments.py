# default arguments = A default value for certain parameters
#                     default is used when that argument is omitted
#                     make your functions more flexible, reduces number of arguments

# def net_price(list_price, discount, tax):
#     return list_price * (1 - discount) * (1 + tax)
#
# print(net_price(500, 0, 0.05))


# discount, tax는 거의 모든 상황에서 동일하기 때문에 default parameter로 만들 수 있다.
def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

# 인수는 하나만 보내도 된다
print(net_price(500))
# 인수를 두 개 이상 보내면, default parameter 대신 인수를 값으로 계산한다
print(net_price(500, 0.1))
print(net_price(500, 0.1, 0.02))

import time

# default argument는 positional argument(일반 인자) 뒤에 와야 한다
def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Done!!")

count(10)
count(30, 19)