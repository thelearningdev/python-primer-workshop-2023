for i in range(0, 10):
    print(i)

# How to iterate
# What is range(0, 10)?


numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

# Syntax

"""
for element in sequence:
    operation1
    operation2
"""

# Most common for loop mistake

numbers = [1, 2, 3, 4, 5]
l = len(numbers)

for i in range(0, l):
    print(numbers[i])

# Zipping two lists

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(name, age)


# Looping over dict

ages = {"Alice": 25, "Bob": 30, "Charlie": 35}
for name in ages:
    print(name, ages[name])

# Alice, bob, charlie
# Alice,25 ... bob, 30,...