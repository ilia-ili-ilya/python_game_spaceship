from constants import *
from vector import Vector


class Button:
    def __init__(self, left_up, right_down, text):
        self.left_up = Vector(left_up)
        self.right_down = Vector(right_down)
        self.text = text

    def draw(self, artist):
        artist.draw_button(self.left_up, self.right_down, self.text)

    def is_pressed(self, vec):
        return (self.left_up.x < vec.x < self.right_down.x) and (self.left_up.y < vec.y < self.right_down.y)


def get_buttons_engines():
    return [Button((SCREEN_WIDTH - SIZE_OF_BUTTON_X, 0),
                   (SCREEN_WIDTH, SIZE_OF_BUTTON_Y), '1'),
            Button((SCREEN_WIDTH - SIZE_OF_BUTTON_X, SIZE_OF_BUTTON_Y),
                   (SCREEN_WIDTH, SIZE_OF_BUTTON_Y * 2), '2'),
            Button((SCREEN_WIDTH - SIZE_OF_BUTTON_X, SIZE_OF_BUTTON_Y * 2),
                   (SCREEN_WIDTH, SIZE_OF_BUTTON_Y * 3), '3'),
            Button((SCREEN_WIDTH - SIZE_OF_BUTTON_X, SIZE_OF_BUTTON_Y * 3),
                   (SCREEN_WIDTH, SIZE_OF_BUTTON_Y * 4), 'START')]


def get_buttons_technical():
    return [Button((SCREEN_WIDTH - SIZE_OF_BUTTON_X, 0), (SCREEN_WIDTH, SIZE_OF_BUTTON_Y), '<'),
            Button((SCREEN_WIDTH - SIZE_OF_BUTTON_X, SIZE_OF_BUTTON_Y),
                   (SCREEN_WIDTH, SIZE_OF_BUTTON_Y * 2), '>'),
            Button((SCREEN_WIDTH - SIZE_OF_BUTTON_X, SIZE_OF_BUTTON_Y * 2),
                   (SCREEN_WIDTH, SIZE_OF_BUTTON_Y * 3), 'OK'),
            Button((SCREEN_WIDTH - SIZE_OF_BUTTON_X, SIZE_OF_BUTTON_Y * 3),
                   (SCREEN_WIDTH, SIZE_OF_BUTTON_Y * 4), 'delete')]
