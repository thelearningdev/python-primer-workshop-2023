# Go through the file and fill it with code
# Run the file `python 4-functions/2_exercises.py`
# When there is an error trace the line number and fix it

INVALID_INPUT = "Invalid Input"


def area_of_square():
    # takes `length` as input
    # returns area of square
    # return INVALID_INPUT :: for improper input

    # pass is used when you want to leave a block as empty and fill in later
    # using pass will not raise an error
    pass


def area_of_circle():
    pass


def calculate_area_of_square_with_list():
    # add func param `lengths`
    # Loop through `lenghts`, find area and return a list
    # Modify the code to get `lengths` as a param
    pass


def area():
    # modify this function which takes two params `(shape, length)` and returns area of the shape.
    # possible values for shape is square & circle alone
    # return INVALID_INPUT :: for improper input
    # think if you can re-use a function from before
    pass


def calculate_area_with_list():
    # get an input param `shapes` with list of [(`shape_type, length`)]
    # Loop through find area and return a list
    # Modify the code to get `shapes` as a param
    # return INVALID_INPUT :: for improper input
    pass


assert area_of_square(4) == 16
assert area_of_square(0) == 0
assert area_of_square("abs") == INVALID_INPUT
assert calculate_area_of_square_with_list([4, 0, "abs", None]) == [
    16,
    0,
    INVALID_INPUT,
    INVALID_INPUT,
]


assert area("square", 4) == 16
assert area("circle", 4) == 50  # just use int
assert area("rectangle", 4) == INVALID_INPUT
assert area("rectangle", 0) == INVALID_INPUT

shapes = [
    ("square", 4),
    ("circle", 4),
    ("rectangle", 4),
    ("square", 0),
    ("sqaure", None),
]
assert calculate_area_with_list(shapes) == [16, 50, INVALID_INPUT, 0, INVALID_INPUT]
