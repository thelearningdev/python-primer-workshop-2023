# Format string

## Modify the code with format string


def greet(msg):
    return hello + " " + msg


print(greet("Sam"))
print(greet("Ram"))
print(greet("Tam"))


# ----------------------------------------------------------------------------


# Format string with dict values

# Write a for loop to loop through the data,
# use the template string to print for each values

data = [
    {"name": "Ram", "age": 10},
    {"name": "Sam", "age": 12},
    {"name": "Tam", "age": 14},
]
template = "we all know {name} whose age is {age}"


# ----------------------------------------------------------------------------

# Format strings inplace

name = "Tam"
age = 10

print(f"we all know {name} whose age is {age}")


# When to use format inplace format strings vs templated strings

