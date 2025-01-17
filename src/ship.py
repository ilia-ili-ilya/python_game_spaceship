from constants import *
from vector import Vector
from direction import Directon
from gun import Gun

class Ship:

    def __init__(self):
        self.center = Vector(SHIP_START_POS)
        self.angle = Directon(BASE_DIR)
        self.cells = []
        self.speed = Vector((0, 0))
        self.spin = Directon(BASE_DIR)
        self.count_of_cartridge = 0
        self.gun = Gun()
    def add_cell(self, new_cell):
        self.cells.append(new_cell)

    def del_cell(self, ind):
        self.cells.pop(ind)

    def ind_of_cell(self, point):
        for i in range(len(self.cells)):
            if (self.cells[i].get_pos(self.center) - point).lenght() <= REAL_RAD_CELL:
                return i
        return -1

    def make_a_step(self, actual_types):
        self.speed += Vector(ATTRACTION)
        self.angle -= self.spin
        for cell in self.cells:
            cell.turn(self.spin)

        for cell in self.cells:
            if actual_types[cell.get_type()]:
                pulse = cell.give_power()
                pulse *= ((1 / pulse.lenght()) * POWER_OF_ENGINE)
                pr = (cell.direc * ((cell.dist + SHIP_SIZE) / 2)).find_projection(pulse)
                self.speed += pulse * ENGINE_POWER
                sp = (cell.direc * ((cell.dist + SHIP_SIZE) / 2)) + (pulse - pr) * ENGINE_POWER
                sp *= 1 / sp.lenght()
                self.spin += (Directon(sp.make_point()) - cell.direc)
        self.center += self.speed

    def does_touch_haters(self, haters):
        for hater in haters:
            if (self.center - hater.get_center()).lenght() < SHIP_SIZE + hater.get_size():
                return True
        return False
    def take_catridge(self, catridges):
        new_catridges = []
        for catridge in catridges:
            if (self.center - catridge.get_center()).lenght() < SHIP_SIZE + catridge.get_size():
                self.count_of_cartridge += 1
            else:
                new_catridges.append(catridge)
        return new_catridges

    def is_in_screen(self):
        return (0 + SHIP_SIZE <= self.center.x <= SCREEN_WIDTH - SHIP_SIZE) and (
                0 + SHIP_SIZE <= self.center.y <= SCREEN_HEIGHT - SHIP_SIZE)

    def default_settings(self):
        for cell in self.cells:
            cell.turn(self.angle)
        self.center = Vector(SHIP_START_POS)
        self.angle = Directon(BASE_DIR)
        self.speed = Vector((0, 0))
        self.spin = Directon(BASE_DIR)
        self.count_of_cartridge = 0

    def in_ship(self, ind):
        return (self.center - ind).lenght() <= SHIP_SIZE