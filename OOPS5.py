# inheritance (Attribute to a class) self to instance method

# Class Attributes

class Person:
    number_of_people = 0
    GRAVITY = -9.8

    def __init__(self,name):
        self.name = name
        Person.number_of_people += 1

p1 = Person("tim")
print(Person.number_of_people)
p2 = Person("John")
print(Person.number_of_people)


