# function :: shape(no_of_sides, angle) # square, hexagon, pentagon, triangle

# Report
# x-axis
# y-axis
# scale
    # Bar
        # display()
    # Line
        # display()
    # Histogram
        # display()
    # Pie
        # display()

# Vechicle - start, stop, num_of_wheels, drive
    # Bike - 
    # Car - 
    # Truck - load

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print(f"{self.make} {self.model} is starting.")

    def stop(self):
        print(f"{self.make} {self.model} is stopping.")


class Bike(Vehicle):
    # overriding
    def start(self):
        super().start()
        print ("bike is starting specially")
        
    pass

b = Bike("Dio", 'Rz1', 2022)
b.start()
b.stop()

class Car(Vehicle):
    # num_wheels - add new properties to subclas
    # drivable - add new functions

    def __init__(self, make, model, year, num_wheels):
        super().__init__(make, model, year)
        self.num_wheels = num_wheels

    def drivable(self):
        print ("yes drivable")

c = Car("Honda", "celtos", 2022, 4)
c.drivable()
c.start()
c.stop()




# class Truck(Vehicle):
#     def __init__(self, make, model, year, payload_capacity):
#         super().__init__(make, model, year)
#         self.payload_capacity = payload_capacity

#     def load(self, cargo):
#         print(
#             f"{cargo} is loaded onto the {self.make} {self.model} with payload capacity of {self.payload_capacity} lbs."
#         )


# class Motorcycle(Vehicle):
#     def __init__(self, make, model, year, num_wheels):
#         super().__init__(make, model, year)
#         self.num_wheels = num_wheels

#     def wheelie(self):
#         print(
#             f"{self.make} {self.model} pops a wheelie on its {self.num_wheels} wheels."
#         )


# my_car = Car("Toyota", "Camry", 2020, 4)
# my_car.start()  # prints "Toyota Camry is starting."
# my_car.drive()  # prints "Toyota Camry is driving on 4 wheels."

# my_truck = Truck("Ford", "F-150", 2022, 2000)
# my_truck.start()  # prints "Ford F-150 is starting."
# my_truck.load(
#     "Boxes"
# )  # prints "Boxes is loaded onto the Ford F-150 with payload capacity of 2000 lbs."

# my_bike = Motorcycle("Honda", "CBR1000RR", 2021, 2)
# my_bike.start()  # prints "Honda CBR1000RR is starting."
# my_bike.wheelie()  # prints "Honda CBR1000RR pops a wheelie on its 2 wheels."
