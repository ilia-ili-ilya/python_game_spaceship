from constants import *
from direction import Directon

class Engine:
    def __init__(self, e_type, direc=Directon(BASE_DIR)):
        self.e_type = e_type
        self.direc = direc

    def turn(self, direc):
        self.direc += direc

    #def draw(self, vec, artist, on_off=False):
    #    artist.draw_engine(vec, self.direc, self.e_type, on_off)

    def turn_a_little(self, clockwise):
        if clockwise:
            self.turn(Directon(SMALL_ANGLE))
        else:
            self.turn(Directon(SMALL_ANTI_ANGLE))

    def give_power(self):
        return self.direc * ENGINE_POWER