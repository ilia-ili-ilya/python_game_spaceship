from constants import BASE_DIR
from vector import Vector

class Directon:
    def __init__(self, point=BASE_DIR):
        self.x = point[0]
        self.y = point[1]

    def __add__(self, other):
        return Directon((self.x * other.x - self.y * other.y, self.x * other.y + self.y * other.x))

    def __iadd__(self, other):
        self.x, self.y = self.x * other.x - self.y * other.y, self.x * other.y + self.y * other.x
        self.make_ok()
        return self

    def __sub__(self, other):
        return Directon((self.x * other.x + self.y * other.y, - self.x * other.y + self.y * other.x))

    def __isub__(self, other):
        self.x, self.y = self.x * other.x + self.y * other.y, - self.x * other.y + self.y * other.x
        self.make_ok()
        return self

    def __mul__(self, other):
        return Vector((self.x * other, self.y * other))

    def make_ok(self):
        l = (self.x * self.x + self.y * self.y) ** 0.5
        self.x *= 1 / l
        self.y *= 1 / l