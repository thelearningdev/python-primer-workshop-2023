# A simple class


class Car:
    num_cars = 0
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        Car.num_cars += 1


# Class with methods


class Car:
    num_cars = 0
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        Car.num_cars += 1 

    def start(self):
        print("The car is starting.")

    def stop(self):
        print("The car is stopping.")


# Class objects

car1 = Car("Toyota", "Corolla", 2021)
car2 = Car("Kia", "Celtos", 2022)

print(car1.make)
print(car1.model)

# Modifying object values

car1.make = "Tata"
print(car1.make)


# What is self?

car1.start()

# Implicit and explicit object

Car.start(car1)


# classes are custom data types
# properties and functions/behavior

class Notebook:
    def __init__(self, no_of_pages, dimensions, bound_type, has_lines):
        self.no_of_pages = no_of_pages
        self.dimensions = dimensions
        self.bound_type = bound_type
        self.has_lines = has_lines
        self.content = None

    def clear(self):
        self.content = None
    def add_content(self, content):
        self.content = content


nb1.add_content("abc")

# Notebook.add_content(nb1, "abc")


# x = 1
# x = int(1)

nb1 = Notebook(100, [100, 100], 'paperback', True)
nb2 = Notebook(150, [100, 100], 'hardcover', False)
nb3 = Notebook(200, [134, 156], 'paperback', True)

nbdict_1 = {
    "no_of_pages":100,
    "dimensions": [100, 100],
    "bound_type": "paperback",
    "has_lines": True
}
nbdict_1['no_of_pages']

nb1.no_of_pages
nb1.dimensions

nb2.bound_type
nb2.has_lines

nb2.has_lines = False

