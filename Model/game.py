#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame as pg
from Model.menu import Menu
class Game:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode(size=(600, 480))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass
            # Check for all events
            # for event in pg.event.get():
            #     if event.type == pg.QUIT:
            #         pg.quit() # Close Window
            #         quit() # End PyGame