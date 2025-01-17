import sys
import pygame

class Looker:
    def __init__(self):
        self.mouse = (-1, -1)
        self.last_click = (-1, -1)
        self.actual_keys = {"1": False, "2": False, "3": False, "left": False, "right": False}

    def update(self, wait_click=False):
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.actual_keys["left"] = True
                elif event.key == pygame.K_RIGHT:
                    self.actual_keys["right"] = True
                elif event.key == pygame.K_1:
                    self.actual_keys["1"] = True
                elif event.key == pygame.K_2:
                    self.actual_keys["2"] = True
                elif event.key == pygame.K_3:
                    self.actual_keys["3"] = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.actual_keys["left"] = False
                elif event.key == pygame.K_RIGHT:
                    self.actual_keys["right"] = False
                elif event.key == pygame.K_1:
                    self.actual_keys["1"] = False
                elif event.key == pygame.K_2:
                    self.actual_keys["2"] = False
                elif event.key == pygame.K_3:
                    self.actual_keys["3"] = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.last_click = pygame.mouse.get_pos()
                    click = True
            self.mouse = pygame.mouse.get_pos()
        if wait_click:
            return click

    def update_keys(self):
        self.update()
        return self.actual_keys

    def mouse_pos(self, click):
        if self.update(True):
            return (True, self.last_click)
        return (False, self.mouse)

    def click(self):
        return (self.update(True), self.last_click)

    def get_key(self, key):
        return self.actual_keys[key]