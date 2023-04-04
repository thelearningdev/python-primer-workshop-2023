# A simple class


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        Car.num_cars += 1


# Class with methods


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

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


