import pygame
from .controls import *
from .map import *
from .entities import *

class Brickfighter:
    name = "BrickFigther"
    running = True
    
    def __init__(self, screen, globals):
        self.screen = screen
        self.glb = globals
        self.player = Player(self.glb)
        self.map = Map(self.glb)
        self.controls = controls # from controls.py


    def render(self):
        # --- todo
        # replace rectangle player with assets later
        # --- joey

        self.screen.fill((0, 0, 0))

        pygame.draw.rect(self.screen, (50, 50, 50), self.map.rect)

        player_width = 100
        player_height = 200

        player_rect = pygame.Rect(
            self.player.position[0],
            self.glb.WINHEIGHT - self.map.floor_height - self.player.position[1] - player_height,
            player_width,
            player_height
        )
        pygame.draw.rect(self.screen, (100, 100, 100), player_rect)

    def update(self):
        self.render()
        self.controls(self)
        pygame.display.update()