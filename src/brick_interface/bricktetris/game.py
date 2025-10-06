import pygame
from .constants import *

class Bricktetris:
    name = "Brick Tetris"
    running = True
    
    def __init__(self, screen, globals):
        self.screen = screen
        self.glb = globals
        
    def handle_events(self):
        pass

    def update(self):
        self.screen.fill(LIGHT_BLUE)
        main_screen = pygame.Rect(MAIN_SCREEN_X, MAIN_SCREEN_Y, MAIN_SCREEN_WIDTH, MAIN_SCREEN_HEIGHT)
        next_screen = pygame.Rect(NEXT_SCREEN_X, NEXT_SCREEN_Y, NEXT_SCREEN_WIDTH, NEXT_SCREEN_HEIGHT)
        info_screen = pygame.Rect(INFO_SCREEN_X, INFO_SCREEN_Y, INFO_SCREEN_WIDTH, INFO_SCREEN_HEIGHT)
        pygame.draw.rect(self.screen, DARK_BLUE, main_screen)
        pygame.draw.rect(self.screen, DARK_BLUE, next_screen)
        pygame.draw.rect(self.screen, DARK_BLUE, info_screen)
        pygame.display.flip()