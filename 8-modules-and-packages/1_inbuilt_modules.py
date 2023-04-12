# Inbuilt modules

# split
# strip
# len
# count

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


# library(folder)
    # books
        # books.py
    # bookshelf
        # shelf.py

    # library.py


from books.books import get_function
get_function

from books import books
book.get_function

from book_shelf import shelf
