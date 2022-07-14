from pickletools import pystring
import pygame, sys
from debug import debug
from settings import *

class Game:
    def _init_(self):
        #General Setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Holy Rescue')
        self.clock = pygame.time.Clock()
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.screen.fill('Black')
            debug('hello :)')
            pygame.display.update()
            self.clock.tick(FPS)

if  __name__ == '__juego__':
    game = Game()
    game.run()
    
