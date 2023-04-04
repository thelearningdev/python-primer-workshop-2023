# Try the following in Python Shell


100 + 200 

_ + 100 


# Declaring a variable

a = 100
b = 200

a + b

c = a + b # why doesn't this give a response
print (c)

# Try other operations like /, *, **

type(c)

# --------------------- Getting Help --------------------------=

help(abs)


help(int)


help("for") # why is this enclosed in quotes


help("+")


# --------------------- Comments --------------------------

"""
Multi-line comment, also works as a string, also used as a doc string
"""

a1 = """a
b
c
"""

a2 = "a
b
c"

# What's the difference between a1 and a2? Why don't we print and see?

# --------------------- Boolean --------------------------

True

False

x = True

y = False

x == y

x != y

True == 1

# --------------------- Conditional statements ------------


if x:
    print ("X is true")

# Will this condition pass
if 5:
    print ("5 is true") 



# --------------------- For Loop --------------------------

for i in range(5):
    print(i)
    

# Find what range does? Rember `help`



# Another for loop

for j in [1, 2, 3, 4, 5]:
    print (i)

# --------------------- Lists --------------------------

l = [] # an empty list

l = [1, 2, 3, 4, 5]

for j in l:
    print (i)

l[0]

l[1]

# Access the 4th and 7th element what happens?


# Find the type of `l` variable

# is the following a valid python element
t = 1, 2, 3, 4, 5

# what is the type of t?


# Define a list [50, 80, 100, 20, 30, 29
# find the number of elements with value > 70


# --------------------- Tuples --------------------------

t = ()
t = (1, 2, 3, 4)

# write a for loop to loop through t


# Access the 4th and 7th element what happens?


# So what is the difference between list and a tuple?

# --------------------- String --------------------------

s = 'hello'

# What's the output of this?
s[0] 

# What's the output of this? Does it work? Why not?
s[0] = 'B' 


# Can you do the same for list `l` we defined before?


# Can you do the same for list `t` we defined before?


# What is the output of the following?
# What does this says about the str object?
for i in s:
    print (i)

# --------------------- Find functions of an object --------------------------

# what does this statement do?
dir(s)

# Try these string functions
# 'isdigit', 'islower', 'istitle', 'isupper', 'join', 'replace', 'split', 'startswith', 'strip', 'swapcase', 'title'


# Try the same for `l` what functions do you find?

# --------------------- Recap --------------------------


a = 100 
b = 100.0
c = "I am a string"
d = [1, 2, 3, 4, 5]
e = (1, 3)
f = 1, 3
g = range(1, 3)
x = True
y = False
x == y == False

# a = a + 100
a += 100


