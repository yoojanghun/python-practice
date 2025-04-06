# 디폴트 매개변수 (default parameter) = 함수에서 고정된 매개변수(parameter)
# 매개변수 값이 일정한 경우가 많을 때, 굳이 인자에 값을 쓰지 않고 고정된 매개변수를 정한다.
# 디폴트 매개변수는 위치 매개변수(positional parameter) 뒤에 위치한다.

import time

def timer(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Done!!!")

# timer(10)
timer(10, 3)

def net_price(net_list, tax=0.05, discount=0):
    return net_list * (1 - discount) * (1 + tax)

print(net_price(500))