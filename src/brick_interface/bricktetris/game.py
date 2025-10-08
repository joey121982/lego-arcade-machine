import pygame
from .constants import *

class Bricktetris:
    name = "Brick Tetris"
    running = True
    
    def __init__(self, screen, globals):
        self.screen = screen
        self.glb = globals
        
        # this will get longer
        self.background_image, self.main_screen_image, self.next_screen_image, self.info_screen_image = load_images()
        
    def handle_events(self):
        pass

    def update(self):
        self.screen.blit(self.background_image, (0, 0))
        self.screen.blit(self.main_screen_image, (MAIN_SCREEN_X, MAIN_SCREEN_Y))
        self.screen.blit(self.next_screen_image, (NEXT_SCREEN_X, NEXT_SCREEN_Y))
        self.screen.blit(self.info_screen_image, (INFO_SCREEN_X, INFO_SCREEN_Y))
        pygame.display.flip()