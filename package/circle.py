from modules.m1 import PI


class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return PI * self.radius**2

    def circumference(self):
        return 2 * PI * self.radius
