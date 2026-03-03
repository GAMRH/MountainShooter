#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, random
from tkinter.font import Font
from Model.entitymediator import EntityMediator
from Model.enemy import Enemy
from Model.entity import Entity
from Model.entityFactory import EntityFactory
from Model.Const import COLOR_CYAN, COLOR_GREEN, COLOR_WHITE, EVENT_ENEMY, EVENT_TIMEOUT, MENU_OPTION, SPAWN_TIME, TIMEOUT_LEVEL, TIMEOUT_STEP, WIN_HEIGHT
import pygame as pg

from Model.player import Player
class Level:
    def __init__(self, window: pg.Surface, name: str, game_mode: str, player_score: list [int]):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        player = (EntityFactory.get_entity('Player1'))
        player.score = player_score[0]
        self.entity_list.append(player)
        self.timeout = TIMEOUT_LEVEL
        
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            player = (EntityFactory.get_entity('Player2'))
            player.score = player_score[1]
            self.entity_list.append(player)
        pg.time.set_timer(EVENT_ENEMY, SPAWN_TIME)  
        pg.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP) #100ms  
    def run(self, player_score: list [int]):
        pg.mixer_music.load(f'./asset/{self.name}.mp3')
        pg.mixer_music.play(-1)
        clock = pg.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance (ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.name == 'Player1':
                    self.level_text(14, f'Player1 - Health: {ent.health} | Score {ent.score}', COLOR_GREEN, (10,25))
                if ent.name == 'Player2':
                    self.level_text(14, f'Player2 - Health: {ent.health} | Score {ent.score}', COLOR_CYAN, (10,45))
                    
            for event in pg.event.get():
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.name == 'Player2':
                                player_score[1] = ent.score
                        return True
                found_player = False
                for ent in self.entity_list:
                    if isinstance (ent, Player):
                        found_player = True
                if not found_player:
                    return False
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', COLOR_WHITE, (10,5))
            self.level_text(14, f'FPS: {clock.get_fps() :.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'Entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))
            pg.display.flip()
            # Collisions
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
        pass
    
    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pg.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: pg.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pg.Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
