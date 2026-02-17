#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame as pg
from Model.menu import Menu
from Model.level import Level
from Model.Const import WIN_WIDTH, WIN_HEIGHT
from Model.menu import MENU_OPTION
class Game:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()
            
            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.window, 'Level1', menu_return)
                level_return = Level.run()
            elif menu_return == MENU_OPTION[4]:
                pg.quit()
                quit()
            else:
                pass