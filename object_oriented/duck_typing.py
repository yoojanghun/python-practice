# "Duck typing" = Another way to achieve polymorphism besides Inheritance
#                 Object must have the minimum necessary attributes/methods
#                 "If it looks like a duck and quacks like a duck, it must be a duck."

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Car:

    alive = False

    def speak(self):
        print("HONK!")

animals = [Dog(), Cat(), Car()]

# 자동차는 animal로 불리기 위한 최소한의 조건을 만족한다(speak, alive 가짐)
for animal in animals:
    animal.speak()
    print(animal.alive)