from random import random, randint, choice

from constants import COUNT_OF_TYPES, SCREEN_WIDTH, SCREEN_HEIGHT
from hater import Hater
from cartridge import Cartridge

class Game:
    def __init__(self, ship, artist, looker):
        self.ship = ship
        self.haters = []
        self.cartridges = []
        self.artist = artist
        self.looker = looker
        self.actual_types = [False] * COUNT_OF_TYPES
        self.result = 0
        self.projectles = []

    def update_types(self):
        self.looker.update_keys()
        self.actual_types[1] = self.looker.get_key('1')
        self.actual_types[2] = self.looker.get_key('2')
        self.actual_types[3] = self.looker.get_key('3')

    def check(self):
        if not self.ship.is_in_screen():
            return False
        if self.ship.does_touch_haters(self.haters):
            return False
        return True

    def resalt(self):
        return self.result

    def one_step(self):
        self.ship.make_a_step(self.actual_types)
        self.cartridges = self.ship.take_catridge(self.cartridges)
        new_projectiles = []
        for projectile in self.projectles:
            if projectile.make_a_step():
                new_projectiles.append(projectile)
        self.projectles = new_projectiles
        new_haters = []
        for i in range(len(self.haters)):
            if self.haters[i].make_a_step():
                if not self.haters[i].does_touch_proj(self.projectles):
                   new_haters.append(self.haters[i])
        self.haters = new_haters
        new_cartridges = []
        for cartridge in self.cartridges:
            if cartridge.make_a_step():
                new_cartridges.append(cartridge)
        self.cartridges = new_cartridges
        self.result += 1
        if randint(0, max(50 - self.result // 30, 0)) == 0:
            self.add_hater(choice([True, False]))
            self.add_cartridge(choice([True, False]))
        if self.result % 5 == 0:
            self.projectles.append(self.ship.gun.fire(self.ship.center, self.ship.angle))



    def draw(self):
        self.artist.draw_sreen()
        self.artist.draw_ship(self.ship, self.actual_types)
        for hater in self.haters:
            self.artist.draw_hater(hater)
        for cartrige in self.cartridges:
            self.artist.draw_cartridge(cartrige)
        for projectile in self.projectles:
            self.artist.draw_projectile(projectile)
        self.artist.update_screen()

    def add_hater(self, horizontal_or_vertical):
        if horizontal_or_vertical:
            self.haters.append(
                Hater((choice([0, SCREEN_WIDTH]), randint(0, SCREEN_HEIGHT)), self.ship.center.make_point()))
        else:
            self.haters.append(
                Hater((randint(0, SCREEN_WIDTH), choice([0, SCREEN_HEIGHT])), self.ship.center.make_point()))

    def add_cartridge(self, horizontal_or_vertical):
        if horizontal_or_vertical:
            self.cartridges.append(
                Cartridge((choice([0, SCREEN_WIDTH]), randint(0, SCREEN_HEIGHT)), self.ship.center.make_point()))
        else:
            self.cartridges.append(
                Cartridge((randint(0, SCREEN_WIDTH), choice([0, SCREEN_HEIGHT])), self.ship.center.make_point()))