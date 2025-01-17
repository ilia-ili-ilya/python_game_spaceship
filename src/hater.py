from random import randint

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from vector import Vector

class Hater:
    def __init__(self, center, ship_center):
        self.center = Vector(center)
        self.size = 10
        self.speed = (Vector(ship_center) - Vector(center))
        self.speed *= (3 / self.speed.lenght())

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def make_a_step(self):
        self.speed += Vector((randint(-1, 1), randint(-1, 1))) * (1 / 10)
        self.center += self.speed
        if (self.center.x < -self.size or self.center.x > SCREEN_WIDTH + self.size) or (
                self.center.y < -self.size or self.center.y > SCREEN_HEIGHT + self.size):
            return False
        return True

    def does_touch_proj(self, projectiles):
        for projectile in projectiles:
            if self.size + projectile.get_size() > (self.center - projectile.get_center()).lenght():
                return True
        return False