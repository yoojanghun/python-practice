# Polymorphism = Greek word that means to "have many forms or faces"
#                Poly = Many
#                Morphe = Form

#                TWO WAYS TO ACHIEVE POLYMORPHISM
#                1. Inheritance = An object could be treated of the same type as a parent class
#                2. "Duck typing" = Object must have necessary attributes/methods

# ABC (Abstract Base Class)
# 추상 클래스(abstract class) 를 정의할 때 쓰는 기반 클래스(Base Class)
# 직접 객체 생성 불가
# 목적: "이 클래스를 상속받는 애들은 반드시 특정 메서드를 구현해야 한다"라는 규칙을 만드는 것

# @abstractmethod
# 추상 클래스 안에 구현을 강제할 메서드를 표시하는 데 사용
# 추상 메서드는 선언만 하고 내용이 없음 → 자식 클래스가 반드시 재정의해야 함
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):         # Shape를 상속받은 클래스는 반드시 area() 메서드를 구현해야 함
        pass                # 만약 구현 안 하면, 그 자식 클래스도 추상 클래스 취급 → 객체 생성 불가

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5

class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping

# 각각은 shape로도 인식된다. Pizza는 shape로도, circle로도 볼 수 있다
shapes = [Circle(4), Square(5), Triangle(6,7), Pizza("pepperoni", 15)]

for shape in shapes:
    print(f"{shape.area()}cm²")