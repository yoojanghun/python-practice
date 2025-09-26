# module = 내 프로그램에 추가하고 싶은 코드가 담긴 파일
#          "import"를 이용하여 module을 추가한다. (python 내장 모듈 or 내가 만든거)
#          큰 프로그램을 나누어 재사용 가능한 별도의 파일로 만들 때 유용함

# print(help("modules")) => 내가 사용할 수 있는 module 검색
# print(help("math"))    => math module 검색

import math             # math module 추가
import math as m        # math를 m으로 대신 쓰겠다
from math import pi     # math module에서 pi만 사용하고 싶다

print(math.pi)          # import math
print(m.pi)             # import math as m
print(pi)               # from math import pi

print()

import module_example               # 내가 만든 모듈(module_example.py 파일)
from module_example import pie      # module_example에서 pie만 가져옴

print(module_example.pie)
print(pie)
print(module_example.circumference(4))
print(module_example.square(3))
print(module_example.cube(3))
print(module_example.area(4))