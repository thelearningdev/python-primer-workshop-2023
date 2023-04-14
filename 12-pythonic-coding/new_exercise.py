import datetime

def timer(function, *args):
    start_time = datetime.datetime.now()
    result = function(*args)
    end_time = datetime.datetime.now()
    print ("time taken", end_time-start_time)
    return result

def get_even(numbers):
    # result = []
    # for num in numbers:
    #     result.append(num * 2)
    # return result

    return [num*2 for num in numbers]

def combine_string(words):
    # result = ""
    # for word in words:
    #     result += word + " "
    # print(result) # 000219 000013
    return " ".join(words)

timer(get_even, range(100000))
# timer(combine_string, ["hello", "world", "python"] * 100)