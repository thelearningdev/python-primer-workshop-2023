class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age >= 0:
            self._age = age
        else:
            raise ValueError("Age must be a positive integer.")


person = Person("Alice", 25)

print(person.get_name())
print(person.get_age())  

person.set_name("Bob")
person.set_age(30)


print(person.get_name())  # prints "Bob"
print(person.get_age())  # prints 30


person.set_age(-10)
