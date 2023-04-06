import math


class Shape:
    def __init__(self, shape_type, *args):
        self.shape_type = shape_type
        self.args = args

    def calculate_area(self):
        try:
            area_func = getattr(self, f"area_{self.shape_type}")
            return area_func(*self.args)
        except AttributeError:
            return f"Error: Invalid shape type - {self.shape_type}"

    def area_circle(self, radius):
        return math.pi * radius**2

    def area_square(self, side):
        return side**2

    def area_rectangle(self, length, width):
        return length * width

    def area_triangle(self, base, height):
        return 0.5 * base * height


shapes = [
    {"name": "circle", "params": [5]},
    {"name": "square", "params": [4]},
    {"name": "rectangle", "params": [5, 3]},
    {"name": "triangle", "params": [4, 6]},
]

for shape in shapes:
    s = Shape(shape["name"], *shape["params"])
    print(f"{shape['name'].capitalize()} area:", s.calculate_area())

