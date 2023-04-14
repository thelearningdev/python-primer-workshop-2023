# # Let's learn IDs

# x = 10
# id(x)

# y = x
# id(y)

# # Everything is a reference

# x = [1, 2, 3]
# y = {"value": x}
# y["value"].append(10)
# print(x)

# # Some weird cases


# def my_function(arg1, arg2=None):
#     if arg2 is None:
#         arg2 = {}

#     arg2[arg1] = 10
#     return arg2


# print(my_function(1))
# print(my_function(2))

# def my_function(a=[], arg2=[]):
#     a.append("10")
#     arg2.append("new item")
#     return (a, arg2)

# # ---------------------- passing functions around ----------------------


# def other_temp_function(other_function):
#     other_function()


# def temp_function(other_function):
#     other_temp_function(other_function)


# def passed_function():
#     print("I'm being passed around")


# temp_function(passed_function)


# # --------------Passing around classes --------------


# class Temp:
#     def print_temp(self):
#         print("test")


# def function_demo(ClassRef):
#     ClassRef().print_temp()


# function_demo(Temp)

# import datetime

# def timer(function):
#     start_time = datetime.datetime.now()
#     result = function()
#     end_time = datetime.datetime.now()
#     print ("time taken", end_time-start_time)
#     return result

class Apple:
    pass

class Mango:
    pass

class Orange:
    pass

d = {"apple": Apple, "orange": Orange, "mango": Mango}

fruit = input() # apple
try:
    class_ref = d[fruit] # d["apple"]
    obj = class_ref()
    print (class_ref, obj)
except KeyError:
    print (fruit, "not available")
