class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("John", 30)

# Use getattr to dynamically access attributes

print(getattr(person, "name"))
print(getattr(person, "age"))


setattr(person, "name", "Alice")
setattr(person, "age", 25)


print(getattr(person, "name"))
print(getattr(person, "age"))


import math

getattr(math, "sqrt")
getattr(math, "pi")
