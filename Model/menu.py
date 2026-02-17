#!/usr/bin/python
# -*- coding: utf-8 -*-
from Model.Const import WIN_WIDTH,COLOR_YELLOW, COLOR_WHITE, COLOR_BROWN, MENU_OPTION
import pygame as pg
from pygame import Surface, Rect
from pygame.font import Font
class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pg.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pg.mixer_music.load('./asset/MenuSound.mp3')
        pg.mixer_music.play(-1)
        while True:
            # DRAW IMAGES
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(40, "Mountain", (COLOR_BROWN), ((WIN_WIDTH / 2,70)))
            self.menu_text(40, "Shooter", (COLOR_BROWN), ((WIN_WIDTH / 2,120)))
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_YELLOW, ((WIN_WIDTH / 2), 180 + 30 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 180 + 30 * i))
            pg.display.flip()
            
            # Check for all events
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit() # Close Window
                    quit() # End PyGame
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pg.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pg.K_RETURN: # ENTER
                        return MENU_OPTION[menu_option]
                    
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pg.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
