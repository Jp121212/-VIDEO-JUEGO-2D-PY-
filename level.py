
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
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        
        ##Actualizar mi sprite
        self.create_map()

    def create_map(self):
        ##Creo el mapa aca
        for row_index,row in enumerate (WORLD_MAP):
            for col_index,col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 'p':
                   self.player =  Player((x,y),[self.visible_sprites],self.obstacle_sprites)




    def run(self):
        ##Dibujo de el juego aaca
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        debug(self.player.direction)

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        
        ##Inicializar el grupo
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2(100,200) ##posicio camara 


    def custom_draw(self, player):

        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
            ##Dibujar el grupo
        #for sprite in self.sprites():
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_poss = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_poss)


