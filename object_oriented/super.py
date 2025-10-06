# super() = Function used in a child class to call methods from a parent class (superclass).
#           Allows you to extend the functionality of the inherited methods
#           python의 메서드 탐색 순서에 따라 메서드를 호출하는 함수

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {"filled" if self.is_filled else "not filled"}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius ** 2}cm^2")      # child에도 describe method 있으면 부모가 아닌 child의 method 사용
        super().describe()          # 메서드 확장
        
class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

circle = Circle(color="red", is_filled=True, radius=5)
square = Square(color="green", is_filled=False, width=6)
triangle = Triangle(color="yellow", is_filled=True, width=7, height=8)

circle.describe()
square.describe()
triangle.describe()

print()

# D는 메서드 탐색 순서에 따라 super() 메소드를 실행한다
# D의 메서드 탐색 순서: D -> B -> C -> A
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")
        super().show()

class C(A):
    def show(self):
        print("C")
        super().show()

class D(B, C):
    def show(self):
        print("D")
        super().show()

d = D()
d.show()
print(D.__mro__)

# 직관적으로는 super() 메소드를 사용하면 바로 부모 클래스의 메소드로 간다고 생각하기 쉬운데,
# 정확히는 다중 상속 상황에서 메서드 탐색 순서의 다음 클래스로 간다는 뜻