# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

def func1():
    x = 1           # func1의 지역변수
    print(x)        # func2의 x를 print할 수 없음

def func2():
    x = 2           # func2의 지역변수
    print(x)        # func1의 x를 print할 수 없음

func1()     # 1 출력
func2()     # 2 출력

print()

# Enclosed 스코프는 중첩 함수(nested function) 안에서 등장
# inner함수 내에서 지역변수 x가 없음 => enclosed된 범위 내애서 x 사용
def outer():
    x = "enclosed scope"

    def inner():
        # x = "local variable"
        print(x)

    inner()

outer()     # "enclosed scope" 출력

print()

# Global
x = 3
def func3():
    # x = 1
    print(x)

def func4():
    # x = 2
    print(x)

func3()         # 3 출력
func4()         # 3 출력

print()

# built-in
from math import e

# e = 3  (주석 해제하면 3이 출력됨)
def func5():
    print(e)

func5()     # 2.718281828459045 출력