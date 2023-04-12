# OOPS
# object oriented programming system
# Class - Properities/attributes and functions/methods

# Encapsulation - class/object
# Inheritance - parent classes and subclasses 
# polymorphism -
# 1 + 1 # 2
# '1' + '1' # 11
# bar_chart.display()
# line_chart.display()

# abstraction
# Report
    # get_report_name
    # get_data
    # display() # enforce the structure for subclasses


# sales of books 
# Report
    # BarChart
        # display()
    # LineChart
        # display()
    # Histogram
        # display()

# Function programming

class Person:
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        # print (self._age)
        return self._age

    def set_age(self, age):
        
        if age >= 0:
            # print ("setting age", age)
            self._age = age
            # print ("setting age", self._age)
        else:
            raise ValueError("Age must be a positive integer.")

person = Person("Alice", 25)
person.set_age(30)
age_of_alice = person.get_age()
print ("Alice", age_of_alice)

person = Person("Anna", 16)
print ("Anna", person.get_age())

# person = Person("Alice", 25)
# print (person._age)
# print (person._name)

# print(person.get_name())
# print(person.get_age())  

# person.set_name("Bob")
# person.set_age(30)


# print(person.get_name())  # prints "Bob"
# print(person.get_age())  # prints 30


# person._age = -10
# print ("directly assigned -10")
# print(person.get_name())
# print(person.get_age())


# print ("Using set_age to assing -10")
# person.set_age(-10)
