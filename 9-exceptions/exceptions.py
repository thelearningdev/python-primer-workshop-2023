# x = input("no1")
# y = input("no2")

def add(x, y):
    print ("add function called")
    if isinstance(x, int):
        print ("x is an integer")
    else:
        raise ValueError("x is not an integer")
    if isinstance(y, int):
        print ("y is an integer")
    else:
        raise ValueError("y is not an integer")

    return x + y

try:
    print (int(x) / int(y))
except ZeroDivisionError:
    print ("no2 cannot be zero")
    no2 = input()
    add(no1, no2)
except ValueError:
    print ("both the values should be integer")
except Exception as e:
    print ("error occurred") 
    print (e)
finally: 
    print ("final block")


class RenieException(Exception):
    pass

class JielException(Exception):
    pass

def custom_function():
    print ("hello")
    print ("hey")
    1 + 2
    raise JielException("a customized exception occured")


try:
    custom_function()
except JielException:
    print ("jeil exception occurred")
except RenieException:
    print ("handled gracefully")