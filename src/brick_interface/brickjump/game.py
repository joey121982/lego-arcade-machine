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
        
        # the scroll
        self.scroll = 0
        
        self.player = Player(LEFT_PLATFORM_X, PLATFORM_INIT_Y + PLATFORM_HEIGHT)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.running = False
                self.glb.return_to_menu = True  # signal to return to menu
            if event.key == pygame.K_a:
                #self.player.move_left()
                self.scroll += SCROLL
                print(self.scroll)
            if event.key == pygame.K_d:
                #self.player.move_right()
                self.scroll += SCROLL

    def update(self):
        self.screen.fill(UNDERGROUND_BROWN)
        self.level.update(self.scroll)
        self.level.draw(self.screen)
        #self.player.update
        #self.player.draw(self.screen)
        pygame.display.flip()