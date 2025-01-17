from random import randint

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, CARTRIDGE_SIZE
from vector import Vector

class Cartridge:
    def __init__(self, center, ship_center):
        self.center = Vector(center)
        self.size = CARTRIDGE_SIZE
        self.speed = (Vector(ship_center) - Vector(center))
        self.speed *= (5 / self.speed.lenght())

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def make_a_step(self):
        self.speed += Vector((randint(-1, 1), randint(-1, 1))) * (1 / 3)
        self.center += self.speed
        if (self.center.x < -self.size or self.center.x > SCREEN_WIDTH + self.size) or (
                self.center.y < -self.size or self.center.y > SCREEN_HEIGHT + self.size):
            return False
        return True