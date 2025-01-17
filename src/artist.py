from random import random, randint, choice

import pygame

from constants import *
from direction import Directon
from engine import Engine


class Artist:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def draw_sreen(self, color=SCREEN_COLOR):
        self.screen.fill(color)

    def draw_cell(self, vec, cell, on_off=False):
        self.draw_engine(vec + cell.direc * cell.dist, cell.body, on_off)

    def draw_engine(self, vec, eng, on_off=False):
        pygame.draw.line(self.screen, ENGINE_TURBINE_COLOR, (vec + eng.direc * ENGINE_SIZE).make_point(),
                         (vec - eng.direc * ENGINE_SIZE).make_point(), 7)
        if on_off:
            pygame.draw.circle(self.screen, (randint(0, 255), randint(127, 255), randint(0, 255)),
                               (vec - eng.direc * ENGINE_SIZE).make_point(), ENGINE_CORE_SIZE_ON)
            pygame.draw.circle(self.screen, (randint(0, 255), randint(127, 255), randint(0, 255)),
                               (vec - eng.direc * ENGINE_SIZE).make_point(), ENGINE_CORE_SIZE)
        else:
            if eng.e_type == 1:
                pygame.draw.circle(self.screen, GREEN, (vec - eng.direc * ENGINE_SIZE).make_point(), ENGINE_CORE_SIZE)

            if eng.e_type == 2:
                pygame.draw.circle(self.screen, RED, (vec - eng.direc * ENGINE_SIZE).make_point(), ENGINE_CORE_SIZE)

            if eng.e_type == 3:
                pygame.draw.circle(self.screen, BLUE, (vec - eng.direc * ENGINE_SIZE).make_point(), ENGINE_CORE_SIZE)

    def draw_ship(self, ship, actual_types=[False] * COUNT_OF_TYPES):
        self.draw_gun(ship, ship.gun)
        pygame.draw.circle(self.screen, SHIP_COLOR, (ship.center.make_point()), SHIP_SIZE)
        for cell in ship.cells:
            self.draw_cell(ship.center, cell, actual_types[cell.get_type()])

    def draw_hater(self, hater):
        pygame.draw.circle(self.screen, HATER_COLOR, (hater.center.make_point()), hater.size)
    def draw_cartridge(self, cartridge):
        pygame.draw.circle(self.screen, CARTRIDGE_COLOR, (cartridge.center.make_point()), cartridge.size)
        pygame.draw.circle(self.screen, (randint(0, 255), randint(0, 255), randint(0, 255)), (cartridge.center.make_point()), cartridge.size / 2)

    def draw_projectile(self, projectile):
        pygame.draw.circle(self.screen, PROJECTILE_COLOR, (projectile.center.make_point()), projectile.size)

    def draw_gun(self, ship, gun):
        vec = (ship.angle + gun.directon) * 1
        vec.inverse_y()
        pygame.draw.line(self.screen, GUN_COLOR, ship.center.make_point(), (ship.center + vec*(SHIP_SIZE + GUN_THINKNESS)).make_point(), GUN_THINKNESS)
    def update_screen(self):
        pygame.time.wait(FPS)
        pygame.display.update()

    def draw_button(self, button):
        pygame.draw.rect(self.screen, BUTTON_COLOR2,
                         (button.left_up.x + 2, button.left_up.y + 2, button.right_down.x - button.left_up.x - 4,
                          button.right_down.y - button.left_up.y - 4))
        pygame.draw.rect(self.screen, BUTTON_COLOR,
                         (button.left_up.x + 2, button.left_up.y + 2, button.right_down.x - button.left_up.x - 4,
                          button.right_down.y - button.left_up.y - 4), 8)
        if button.text in ['1', '2', '3']:
            self.draw_engine((button.left_up + button.right_down) * 0.5, Engine(int(button.text), Directon(BASE_DIR)),
                             True)  # лучше и False
        else:
            self.draw_text((button.left_up + button.right_down) * 0.5, button.text)

    def draw_text(self, vec, text):
        self.screen.blit(pygame.font.Font(None, 36).render(text, 1, TEXT_COLOR), (
            pygame.font.Font(None, 36).render(text, 1, TEXT_COLOR).get_rect(
                center=(vec).make_point())))
