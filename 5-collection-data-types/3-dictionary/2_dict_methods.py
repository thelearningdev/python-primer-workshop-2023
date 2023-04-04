# Dict methods

## Clear

my_dict = {"a": 1, "b": 2, "c": 3}
my_dict.clear()

## Creating dict

new_dict = dict.fromkeys(["x", "y", "z"], 0)
new_dict = dict([(1, "a"), (2, "b"), (3, "c")])
value = new_dict.get(4, "d")
print(value)

## Updating dict

new_dict.setdefault("a", 10)
new_dict.update({"b": 20, "c": 30})

print(new_dict)

# remove a key-value pair using pop()
value = new_dict.pop("x", 0)
key, value = new_dict.popitem()
keys = new_dict.keys()
values = new_dict.values()

# get a list of key-value pairs
items = new_dict.items()
