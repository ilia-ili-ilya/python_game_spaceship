class Vector:
    def __init__(self, point):
        self.x = point[0]
        self.y = point[1]

    def __add__(self, other):
        return Vector((self.x + other.x, self.y + other.y))

    def __sub__(self, other):
        return Vector((self.x - other.x, self.y - other.y))

    def __mul__(self, other):
        return Vector((self.x * other, self.y * other))

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __imul__(self, other):
        self.x *= other
        self.y *= other
        return self

    def make_point(self):
        return (self.x, self.y)

    def lenght(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def find_projection(self, other):
        c = (self.x * other.x + self.y * other.y) / self.lenght()
        return self * c

    def inverse_y(self):
        self.y *= -1