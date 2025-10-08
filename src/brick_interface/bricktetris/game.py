import pygame
from .constants import *
from .screens import *

class Bricktetris:
    name = "Brick Tetris"
    running = True
    
    def __init__(self, screen, globals):
        self.screen = screen
        self.glb = globals
        
        # this will get longer
        self.background_image, self.main_screen_image, self.next_screen_image, self.info_screen_image = load_images()
        
        # screens
        self.info_screen = InfoScreen(self.screen, INFO_SCREEN_X, INFO_SCREEN_Y, self.info_screen_image, 0, 1, 0)
        self.next_screen = NextScreen(self.screen, NEXT_SCREEN_X, NEXT_SCREEN_Y, self.next_screen_image, None)
        
    def handle_events(self):
        pass

    def update(self):
        self.screen.blit(self.background_image, (0, 0))
        self.screen.blit(self.main_screen_image, (MAIN_SCREEN_X, MAIN_SCREEN_Y))
        self.next_screen.draw()
        self.info_screen.draw()
        pygame.display.flip()