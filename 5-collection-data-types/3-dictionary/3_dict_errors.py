# What error will this raise?

d = {"a": 1, "b": 2, "c": 3}
print(d["d"])

# Will this raise an error

d = {"a": 1, "b": 2, "c": 3}
print(
    d["a"] + "hello"
)  # raises TypeError as you can't concatenate a string with an integer
