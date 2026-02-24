#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
from Model.background import Background
from Model.Const import WIN_HEIGHT, WIN_WIDTH
from Model.enemy import Enemy
from Model.player import Player
class EntityFactory:
    
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name: 
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1',(10, WIN_HEIGHT/2 - 30))
            case 'Player2':
                return Player('Player2',(10, WIN_HEIGHT/2 + 30))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(30, WIN_WIDTH - 20)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(30, WIN_WIDTH - 20)))
