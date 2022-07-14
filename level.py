
import pygame
from settings import *
from tile import Tile
from player import Player
from player import *
from debug import debug

from settings import WORLD_MAP

class Level:    
    def __init__(self):

        ##Display surface
        self.display_surface = pygame.display.get_surface()

        #sprites 
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()
        
        ##Actualizar mi sprite
        self.create_map()

    def create_map(self):
        ##Creo el mapa aca
        for row_index,row in enumerate (WORLD_MAP):
            for col_index,col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x,y),[self.visible_sprites,self.obstacles_sprites])
                if col == 'p':
                   self.player =  Player((x,y),[self.visible_sprites])




    def run(self):
        ##Dibujo de el juego aaca
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        debug(self.player.direction)
       