# Dictionary

# Try the following string functions in Python shell
# x.function()
# When trying each function also think of a usecase to apply it and write them down

# Create a dictionary with some key-value pairs
my_dict = {"apple": 2.99, "banana": 1.25, "orange": 0.99, "grape": 3.50}


## Accessing list

print(my_dict["banana"])

## Modifying list

my_dict["kiwi"] = 2.50
print(my_dict["kiwi"])

## KeyError

print(my_dict["tomato"])

## Find if key is in 

"tomato" in my_dict
"apple" not in my_dict

## Default Value

print(my_dict.get("pear"))
print(my_dict.get("pear", "Sorry, that key is not in the dictionary."))

# What can be a key?

x = {"x": 0, "y": 0, "z": 0, "a": 10}

x[1] = "a"
x["a"] = 1
x["abc"] = 10
x[my_dict] = 57
x[[1, 2, 3]] = 10
x[(1, 2, 3)] = 11
