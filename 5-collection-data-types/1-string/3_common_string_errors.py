# The String Errors

""" 
The goal of this section is to get yourself familiar with the kind of errors you see in Python
By seeing the error, understand why it happens and how to overcome it
"""


y = 1 + "2"

print(y)

s = "azb"

s[1] = z

# The following is an anti-pattern not an error
# 1. Understand what the code does

x = ""

for item in ["apples", "oranges", "mango"]:
    x += item + ","

x = x.strip(",")
print(x)

# 2. What do you think is the problem with other code


# 3. What string method can we use to make this better?
