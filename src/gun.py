from constants import *
from direction import Directon
from projectile import Projectile
class Gun:
    def __init__(self):
        self.directon = Directon(BASE_DIR)

    def fire(self, ship_center, ship_angle):
        vec = (ship_angle + self.directon) * 1
        vec.inverse_y()
        vec *= SHIP_SIZE
        return Projectile(ship_center + vec, ship_center)
