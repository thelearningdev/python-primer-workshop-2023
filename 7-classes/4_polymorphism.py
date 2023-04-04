class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Bird(Animal):
    def speak(self):
        return "Chirp!"

my_dog = Dog("Fido")
my_cat = Cat("Whiskers")
my_bird = Bird("Tweety")

animals = [my_dog, my_cat, my_bird]

for animal in animals:
    print(animal.name + " says " + animal.speak())
