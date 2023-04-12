# Polymorphism in data structures







# Custom polymorphism

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def __add__(self, new_animal):
        return self.speak() + new_animal.speak()

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Bird(Animal):
    def speak(self):
        return "Chirp!"

class Dinosor(Animal):
    def speak(self):
        return "Dead can't speak"

my_dog = Dog("Fido")
my_cat = Cat("Whiskers")
my_bird = Bird("Tweety")
dino = Dinosor("dino")

print (my_dog + my_cat)

# animals = [my_dog, my_cat, my_bird, dino]

# for animal in animals:
#     print(animal.name + " says " + animal.speak())


# Python's internals of + 

class Int:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return str(self.number)

    def __add__(self, num_object):
        return self.number + num_object.number

class Str:
    def __init__(self, string):
        self.string = string
    
    def __str__(self):
        return self.string

    def __add__(self, str_object):
        return self.string + str_object.string

class List:
    def __init__(self, l):
        self.l = l

    def __str__(self):
        return str(self.l)


x = Int(10)
print (x)

print (Int(10) + Int(20))
print (Str("abc") + Str("123"))

x = Str("abc")
print (x)

x = List([1, 2, 3])
print (x)



__len__