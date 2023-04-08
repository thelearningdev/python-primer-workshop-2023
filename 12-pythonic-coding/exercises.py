# No of exercises = 6

# Hint :: for loops

cities = ["Nairobi", "Kampala", "Lagos"]
index = 0
while index < len(cities):
    print(cities[index])
    index += 1


# Hint: Use list comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []
for num in numbers:
    if num % 2 == 0:
        result.append(num)


# Hint: Use `enumerate`
fruits = ["apple", "banana", "orange"]
index = 0
for fruit in fruits:
    print(index, fruit)
    index += 1


# Hint: Use the right data type

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for i in range(len(names)):
    print(names[i], ages[i])


# Hint: use one of the string methods

words = ["hello", "world", "python"]
result = ""
for word in words:
    result += word + " "
print(result)


# Hint :: You can return expressions


def check_equal(x, y):
    result = False

    if x == y:
        result = True
    return result


#  Hint :: Use one of the dict methods


def get_token(payload):
    auth = None
    if "auth_token" in payload:
        auth = payload["auth_token"]
    else:
        auth = "Unauthorized"
