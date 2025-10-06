# class variables = Shared among all instances(object) of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class

class Student:

    class_year = 2025           # class variable
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

print(Student.num_students)
student1 = Student("yoojanghun", 23)    # 객체 생성
print(Student.num_students)
student2 = Student("Spongebob", 30)     # 객체 생성
print(Student.num_students)
student3 = Student("Squidward", 55)     # 객체 생성
print(Student.num_students)
student4 = Student("Sandy", 27)     # 객체 생성
print(Student.num_students)

print(student1.class_year)      # object로 접근
print(student2.class_year)      # object로 접근
print(Student.class_year)       # class로 접근(추천)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")

print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)