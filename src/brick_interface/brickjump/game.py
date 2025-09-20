import pygame
from .constants import *
from .player import *
from .level import *

class Brickjump():
    name = "Brick Jump"
    running = True

    def __init__(self, screen, glb):
        self.screen = screen
        self.running = True
        self.level = Level()
        self.glb = glb
        
        self.player = Player(LEFT_PLATFORM_X, PLATFORM_INIT_Y + PLATFORM_HEIGHT)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    self.glb.return_to_menu = True  # signal to return to menu
                if event.key == pygame.K_a:
                    self.player.move_left()
                if event.key == pygame.K_d:
                    self.player.move_right()

    def update(self):
        self.screen.fill(UNDERGROUND_BROWN)
        self.handle_events()
        self.level.draw(self.screen)
        #self.player.update
        #self.player.draw(self.screen)
        pygame.display.flip()