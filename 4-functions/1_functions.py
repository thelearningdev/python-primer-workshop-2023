# Defining a function:


def greet(name):
    print("Hello, " + name + "!")


greet("Alice")


# Returning a value from a function:


def add(x, y):
    return x + y


result = add(3, 5)
print(result)

# Using default arguments:


def greet(name, greeting="Hello"):
    print(greeting + ", " + name + "!")


greet("Alice")
greet("Bob", "Hi")


# Using keyword arguments:


def greet(name, greeting="Hello"):
    print(greeting + ", " + name + "!")


greet(greeting="Hi", name="Alice")

# Using arbitrary arguments:


def add(*numbers):
    result = 0
    for number in numbers:
        result += number
    return result


print(add(1, 2, 3, 4))

# Using arbitrary keyword arguments:


def greet(**kwargs):
    for key, value in kwargs.items():
        print(key + ": " + value)


greet(name="Alice", greeting="Hello")

# Using lambda functions:

double = lambda x: x * 2
print(double(5))

# Function can call other functions

def add()
