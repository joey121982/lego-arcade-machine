import pygame
from .constants import *
from .screens import *
from .tetromino import Tetromino
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
        self.tetromino_t = Tetromino(self.screen, TETROMINO_START_X - 2 * TS, TETROMINO_START_Y + TS, 'T')
        self.tetromino_i = Tetromino(self.screen, TETROMINO_START_X - 2 * TS, TETROMINO_START_Y + 3 * TS, 'I')
        self.tetromino_o = Tetromino(self.screen, TETROMINO_START_X - 1 * TS, TETROMINO_START_Y + 3 * TS, 'O')
        self.tetromino_z = Tetromino(self.screen, TETROMINO_START_X - 1 * TS, TETROMINO_START_Y + TS, 'Z')
        self.tetromino_j = Tetromino(self.screen, TETROMINO_START_X + 2 * TS, TETROMINO_START_Y + 5 * TS, 'J')
        self.tetromino_l = Tetromino(self.screen, TETROMINO_START_X + 2 * TS, TETROMINO_START_Y + 15 * TS, 'L')
        self.tetromino_s = Tetromino(self.screen, TETROMINO_START_X + 2 * TS, TETROMINO_START_Y + 10 * TS, 'S')
        # self.tetromino_z = Tetromino(self.screen, TETROMINO_START_X, TETROMINO_START_Y + TETROMINO_SIZE, 'Z')
        
        
    def handle_events(self):
        pass

    def update(self):
        self.screen.blit(self.background_image, (0, 0))
        self.screen.blit(self.main_screen_image, (MAIN_SCREEN_X, MAIN_SCREEN_Y))
        self.next_screen.draw()
        self.info_screen.draw()
        self.tetromino_t.draw()
        self.tetromino_i.draw()
        self.tetromino_o.draw()
        self.tetromino_z.draw()
        self.tetromino_j.draw()
        self.tetromino_s.draw()
        self.tetromino_l.draw()
        # self.tetromino_t.draw()
        # self.tetromino_o.draw()

        pygame.display.flip()