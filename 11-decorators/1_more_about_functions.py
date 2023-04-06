# Decorators


# We know functions can call other functions

def temp1():
    print ("temp1")

def temp2():
    temp1()

temp2()

# We know functions can pass other functions as arguments

def temp1():
    print ("temp1")

def temp2(function):
    function()

temp2(temp1)

# Functions can return other functions

def temp1():
    print ("temp1")

def temp2():
    return temp1

t = temp2()
t()

# Function can contain other functions

def outer_function():
    print ("outer function")
    def inner_function():
        print ("inner function")

outer_function()

# 1. Whose responsibility is it to call inner function
# 2. What happens to parameters passed to functions


def outer_function(x):
    print (f"outer function start, {x}")
    
    def inner_function():
        print (f"inner function start, {x}")
        x += 20
        print (f"inner function end, {x}")
    
    inner_function()
    print (f"outer function end, {x}")

outer_function(10)
