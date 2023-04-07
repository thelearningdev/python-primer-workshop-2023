# Inbuilt modules


import math

print(math.pi)
print(math.sqrt(100))


import random

x = random.randint(1, 10)
print(x)

# Importing specific function

from random import randint

x = randint(1, 10)
print(x)

# Importing all function into current module

from random import *

x = random()
print(x)

# Renaming imported values

from random import randint as random_integer

x = random_integer(1, 10)
print(x)


