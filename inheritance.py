# Inheritance = Allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               class Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):          # Dog class는 Animal class로부터 속성과 메소드를 물려받음
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Mouse(Animal):
    pass

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Jerry")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()
dog.speak()