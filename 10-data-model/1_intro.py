class Int:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return str(self.number)

    def __add__(self, num_object):
        return self.number + num_object.number

class Str:
    def __init__(self, string):
        self.string = string
    
    def __str__(self):
        return self.string

    def __add__(self, str_object):
        return self.string + str_object.string

class List:
    def __init__(self, l):
        self.l = l

    def __str__(self):
        return str(self.l)


x = Int(10)
print (x)

print (Int(10) + Int(20))
print (Str("abc") + Str("123"))

x = Str("abc")
print (x)

x = List([1, 2, 3])
print (x)

class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

# Can we make our classes behave like Python objects

my_list = MyList([1, 2, 3])
print(len(my_list))  # Output: 3
