class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

Circle = Circle(5)
print("Area of circle: ", Circle.area())