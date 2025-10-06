# Class methods = Allow operation related to the class itself
#                 Take (cls) as the first parameter, which represents the class itself.

# Instance methods = Best for operations on instances of the class(object)
# Static methods = Best for utility functions that do not need access to class data
# Class methods = Best for class-level data or require access to the class itself

class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # instance method
    def get_info(self):
        return f"{self.name} {self.gpa}"

    # class method
    @classmethod
    def get_count(cls):
        return f"Total number of student: {cls.count}"

    @classmethod
    def get_avg_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.total_gpa / cls.count:.2f}"


student1 = Student("janghun", 3.2)
student2 = Student("Sandy", 4.0)
student3 = Student("patrick", 3.0)

print(Student.get_count())
print(Student.get_avg_gpa())