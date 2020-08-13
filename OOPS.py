# Creating a Class, object and method Basic OOPS
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
d = Dog("Bulldog", 6)
print(d.get_name())
print(d.get_age())
d1 = Dog("Poodle", 9)
print(d1.get_name())
print(d1.get_age())


