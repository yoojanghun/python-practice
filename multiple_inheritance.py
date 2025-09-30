# multiple inheritance = inherit from more than one parent class
#                        C(A, B)

# multilevel inheritance = inherit from a parent which inherits from another parent
#                          C(B) <- B(A) <- A

# class 안 생성자 함수(__init__)을 두는 가장 큰 이유는
# 객체가 만들어질 때 객체가 가질 속성과 초기 상태를 정의하기 위해서이다

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.eat()        # method from grandparents
rabbit.sleep()      # method from grandparents
rabbit.flee()       # method from parents
hawk.hunt()
fish.flee()
fish.hunt()

# python의 메서드 탐색 순서
# class Fish에서 Fish 객체를 만들면
# Fish → Prey → Predator → Animal 순서로 생성자 함수를 한번만 실행
# 예를 들어 Prey에 생성자 함수가 있으면 Animal의 생성자 함수는 실행 X