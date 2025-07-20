import pygame
import json
from .map import *
from .player import *

class Brickman:
    name = "BrickMan"
    running = True
    direction = "none"
    
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

    def controls(self):
        keys=pygame.key.get_pressed()

        state = {
            "w":keys[pygame.K_w],
            "s":keys[pygame.K_s],
            "a":keys[pygame.K_a],
            "d":keys[pygame.K_d]
        }

        if state["w"]:
            self.direction = "up"
        elif state["s"]:
            self.direction = "down"
        elif state["a"]:
            self.direction = "left"
        elif state["d"]:
            self.direction = "right"

    def update(self):
        self.render()