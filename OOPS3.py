# OOPS Basic inheritance

class Pet:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("I don't know what to say")

class Dog(Pet):

    def speak(self):
        print("Bark")

class Cat(Pet):

    def speak(self):
        print("Meow")

class Fish(Pet):
    pass



x = Dog("sam",28)
x.speak()

y = Cat("tom", 30)
y.speak()

z = Fish("stuck", 30)
z.speak()