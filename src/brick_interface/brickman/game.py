import pygame
from .map import *
from .player import *

class Brickman:
    name = "BrickMan"
    running = True
    score = 0

    def __init__(self, screen, globals):
        self.screen = screen
        self.globals = globals
        self.map = Map()
        self.player = Player(self.map.player_start[0], self.map.player_start[1])
        self.tilesize = self.globals.WINHEIGHT//self.map.height

    def display_score (self):
        font = pygame.font.SysFont(None, 24)
        score_text = f"{self.score}"
        text_surface = font.render(score_text, True, (255, 0, 0))
        screen_rect = pygame.display.get_surface().get_rect()
        self.screen.blit(text_surface, (self.globals.WINWIDTH/2, self.tilesize/3))

    def render(self):
        self.screen.fill((0,0,0))
        self.map.render(self.screen, self.tilesize)
        self.player.render(self.screen, self.tilesize)
        self.display_score()

        if self.globals.DEBUG_MODE == True:
            # draw debug data to screen
            font = pygame.font.SysFont(None, 24)
            coord_text = f"DEBUG:   X: {self.player.x:.2f} | Y: {self.player.y:.2f} | DIR: {self.player.direction}"
            text_surface = font.render(coord_text, True, (255, 0, 0))
            screen_rect = pygame.display.get_surface().get_rect()
            self.screen.blit(text_surface, (10, screen_rect.height - 30))

        pygame.display.update()

    def update(self):
        self.render()
        self.player.update(self.map, self)