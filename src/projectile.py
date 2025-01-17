from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PROJECTILE_SIZE, PROJECTILE_SPEED
from vector import Vector

class Projectile:
    def __init__(self, center, ship_center):
        self.center = center
        self.size = PROJECTILE_SIZE
        self.speed = center - ship_center
        self.speed *= PROJECTILE_SPEED

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def make_a_step(self):
        self.center += self.speed
        if (self.center.x < -self.size or self.center.x > SCREEN_WIDTH + self.size) or (
                self.center.y < -self.size or self.center.y > SCREEN_HEIGHT + self.size):
            return False
        return True