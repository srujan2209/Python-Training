# inheritance and using super class

class Pet:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("I don't know what to speak")

    def show(self):
        print(f"I am {self.name} and my age is {self.age}")

class Dog(Pet):

    def __init__(self, name, age, color):
            super().__init__(name, age)    # imp
            self.color = color

    def speak(self):
        print("bark")

    def show(self):
        print(f"I am {self.name} and my age is {self.age} and my color is {self.color}")


class Cat(Pet):
    def speak(self):
        print("Meow")


x = Dog("kim", 25, "brown")
x.speak()
x.show()

y = Cat("Jim", 27)
print(y.name)
print(y.age)
y.speak()
y.show()

