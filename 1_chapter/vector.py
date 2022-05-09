from math import hypot


class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self.x + self.y))

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


# v1 = Vector(2, 5)
# v2 = Vector(4, 7)
# print(v1)
# print(v1 + v2)
# print(abs(v1))
# print(bool(v1))
# print(v2 * 2)
#

