# Introducting decorator

# A special function that takes a function as a arg and return a function

import datetime

def timeit(function):
    print ("init message")
    def timer():
        start_time = datetime.datetime.now()
        result = function()
        end_time = datetime.datetime.now()
        print ("time taken", end_time-start_time)
        return result
    return timer

# def time_this_function():
#     import time
#     time.sleep(2)
#     print ("timer stopped")

# # What will this return?
# timeit(time_this_function)


# Fancier way = decorator

# @timeit("init message")
# def time_this_function():
#     import time
#     time.sleep(2)
#     print ("timer stopped")

# time_this_function()

# Complex decorator

# def timeit(init_message):
#     print (init_message)
#     def timer(function):
#         def wrapper():
#             start_time = datetime.datetime.now()
#             result = function()
#             end_time = datetime.datetime.now()
#             print ("time taken", end_time-start_time)
#             return result
#         return wrapper
#     return timer

# @timeit("init message")
# def time_this_function():
#     import time
#     time.sleep(2)
#     print ("timer stopped")

# timeit("init_message")(time_this_function)()