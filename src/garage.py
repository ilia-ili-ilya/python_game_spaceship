from time import sleep
from random import choice

from constants import *
from vector import Vector
from direction import Directon
from artist import Artist
from looker import Looker
from engine import Engine
from cell import Cell
from ship import Ship
from game import Game
from button import *


class Garage:
    def __init__(self):
        self.ship = Ship()
        self.artist = Artist()
        self.looker = Looker()
        self.buttons_engines = get_buttons_engines()
        self.buttons_technical = get_buttons_technical()

    def one_game(self):
        game = Game(self.ship, self.artist, self.looker)
        while True:
            game.update_types()
            game.one_step()
            if not game.check():
                self.ship.default_settings()
                return game.result + game.ship.count_of_cartridge * 70
            game.draw()

    def follow_mouse(self, e_type):
        while True:
            click, cursor = self.looker.mouse_pos(True)
            if click:
                if self.ship.in_ship(Vector(cursor)):
                    self.ship.add_cell(Cell(Directon(((Vector(cursor) - self.ship.center) * (
                            1 / (Vector(cursor) - self.ship.center).lenght())).make_point()),
                                            (Vector(cursor) - self.ship.center).lenght(),
                                            Engine(int(e_type), Directon(BASE_DIR))))
                return
            else:
                self.artist.draw_sreen()
                self.artist.draw_ship(self.ship)

                self.artist.draw_engine(Vector(cursor), Engine(int(e_type), Directon(BASE_DIR)))

                self.artist.update_screen()

    def technical_support_engine(self, ind):
        while True:
            click, cursor = self.looker.mouse_pos(True)
            if click:
                for button in self.buttons_technical:
                    if button.is_pressed(Vector(cursor)):
                        if button.text == '>':
                            self.ship.cells[ind].body.turn(Directon(SMALL_ANGLE))
                        elif button.text == '<':
                            self.ship.cells[ind].body.turn(Directon(SMALL_ANTI_ANGLE))
                        elif button.text == 'delete':
                            self.ship.del_cell(ind)
                            return
                        elif button.text == 'OK':
                            return
            self.artist.draw_sreen()
            self.artist.draw_ship(self.ship)
            for button in self.buttons_technical:
                self.artist.draw_button(button)
            self.artist.update_screen()

    def show_results(self, result):
        with open(RECORDS, "r") as f:
            records = [int(line.strip()) for line in f.readlines()]
        records.append(result)
        with open(RECORDS, "w") as f:
            for record in records:
                f.write("{}\n".format(record))
        self.artist.draw_sreen(SCREEN_COLOR)

        with open(CONGRATULATIONS, "r") as con:
            congratulation = choice([(line.strip()) for line in con.readlines()])
        self.artist.draw_text(Vector((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)), str(result))
        self.artist.draw_text(Vector((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)), congratulation)
        self.artist.update_screen()
        sleep(3)

    def menu(self):
        while True:
            click, cursor = self.looker.mouse_pos(True)
            if click:
                ind = self.ship.ind_of_cell(Vector(cursor))
                if ind != -1:
                    self.technical_support_engine(ind)
                else:
                    for button in self.buttons_engines:
                        if button.is_pressed(Vector(cursor)):
                            if button.text != 'START':
                                self.follow_mouse(button.text)
                            else:
                                self.show_results(self.one_game())
            self.artist.draw_sreen()
            self.artist.draw_ship(self.ship)
            for button in self.buttons_engines:
                self.artist.draw_button(button)
            self.artist.update_screen()