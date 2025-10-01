# Static methods = A method that belong to a class rather than any object from that class (instance)
#                  Usually used for general utility functions

# Instance methods = Best for operations on instances of the class(object)
# Static methods = Best for utility functions that do not need access to class data

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    # 아래는 static methods. object에 속하지 않고, class 안에만 속함
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions

employee1 = Employee("Eugune", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("Spongebob", "cook")

# instance methods
print(employee1.get_info())

# object가 아닌 class로 호출 가능
print(Employee.is_valid_position("Cook"))