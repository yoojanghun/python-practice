# 프로그램이 어떤 작업을 수행하기 위해서는 (1)데이터와 (2)데이터를 조작하는 행위,
# 두 가지 요소가 필요하다. 일반적으로 데이터는 변수에 넣어서 사용하고 데이터를 조작하는 일은 함수로
# 구성해서 쉽게 실행할 수 있도록 만들어 놓는다.

# 객체(object, instance)는 서로 연관된 데이터와 그 데이터를 조작하기 위한 함수를
# 하나의 집합에 모아놓은 것을 말한다. 이 때 집합의 원소가 되는 변수나 함수는
# 멤버(member) 또는 속성(attribute)이라고 한다. 특히 객체의 속성인 함수는
# 메서드(method)라고 부른다.

# 객체지향 프로그래밍에서 객체를 만들려면 항상 클래스(class)라는 것을 만든 후에
# 그 클래스를 이용하여 객체를 만들어야 한다.

# 아래 예시에서 Car은 class이다. car1, car2, car3는 class로 만들어진 객체이다.

# class를 생성할 때 cl의ass 블럭 안에 정된 __init__란 함수는
# 생성자(constructor)라고 하며 클래스 정의에서 가장 중요한 함수이다.

# 객체를 생성할 때는 클래스 이름을 함수처럼 호출해야 하는데,
# 이때 실제로는 __init__로 정의된 생성자 함수가 호출된다.
# 생성자 함수 내부에서는 생성자를 호출할 때 넣은 입력 변수,
# 즉 인자의 값을 속성값으로 저장한다.

# object = A "bundle of related attributes (variables) and methods(function)
#          Ex. phone, cup, book
#          You need a "class" to create many objects

# attributes: 대상에 대한 속성. object가 가지고 있는 variables
#             Ex. phone의 속성: cost = 99.9, is_on = True, version_num = 13
#                 cup의 속성  : is_filled = True, temp = 85.3

# methods   : object에 속하는 functions. actions that objects can perform
#             Ex. phone에서 method: def make_call():  def turn_on(): 등
#                 cup에서 method: def fill_cup():     def drink_cup(): 등

# class   = (blueprint) used to design the structure and layout of an object
#           object가 가지고 있는 것이 무엇인지(attributes), 무엇을 할 수 있는 지(methods) 정해야 함.

from car import Car

car1 = Car("BMW", "2025", "red", False)
car2 = Car("SM5", "2024", "green", True)
car3 = Car("Charger", "2023", "blue", True)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)

print(car3.model)
print(car3.year)
print(car3.color)
print(car3.for_sale)

car1.drive()
car2.drive()
car3.drive()

car1.stop()
car2.stop()
car3.stop()

car1.describe()
car2.describe()
car3.describe()