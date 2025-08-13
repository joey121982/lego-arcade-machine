import pygame
import json
from .map import *
from .player import *

class Brickman:
    name = "BrickMan"
    running = True
    
    def __init__(self, screen, globals):
        self.screen = screen
        self.globals = globals
        self.map = Map()
        self.player = Player(self.map.player_start[0], self.map.player_start[1])
        self.tilesize = self.globals.WINHEIGHT//self.map.height

    def render(self):
        self.screen.fill((0,0,0))
        self.map.render(self.screen, self.tilesize)
        self.player.render(self.screen, self.tilesize)
        pygame.display.update()

   

    def update(self):
        self.render()
        self.player.update(self.map)