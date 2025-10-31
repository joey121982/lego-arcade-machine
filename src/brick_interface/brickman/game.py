import pygame
from .map import *
from .player import *

FINAL_MAP_NUMBER = 10

class Brickman:
    name = "BrickMan"
    running = True

    def __init__(self, screen, globals):
        self.screen = screen
        self.globals = globals
        self.map = Map(self.globals)
        self.tilesize = self.globals.WINHEIGHT//self.map.height
        self.player = Player(self.tilesize, self.map.player_start[0], self.map.player_start[1])
        self.time = 0
        self.score_value = 0
        self.font_path = "././assets/fonts/Pixellettersfull-BnJ5.ttf"

    def display_score (self):
        font = pygame.font.Font(self.font_path, 24)

        score_text = f"{self.score_value}"
        text_surface = font.render(score_text, True, (255, 0, 0))
        self.screen.blit(text_surface, (self.globals.WINWIDTH/2 - 40, self.tilesize/3))

        time_text = f"{int(self.time)}"
        text_surface = font.render(time_text, True, (255, 0, 0))
        self.screen.blit(text_surface, (self.globals.WINWIDTH/2 + 40, self.tilesize/3))

    def render(self):
        self.screen.fill((0,0,0))
        self.map.render(self.screen, self.tilesize)
        self.player.render(self.screen)
        self.display_score()

        if self.globals.DEBUG_MODE == True:
            # draw debug data to screen
            font = pygame.font.Font(self.font_path, 24)
            coord_text = f"DEBUG:   X: {self.player.x:.2f} | Y: {self.player.y:.2f} | DIR: {self.player.direction}"
            text_surface = font.render(coord_text, True, (255, 0, 0))
            screen_rect = pygame.display.get_surface().get_rect()
            self.screen.blit(text_surface, (10, screen_rect.height - 30))

        pygame.display.update()

    def next_level(self):
        self.map.level += 1

        if self.map.level == FINAL_MAP_NUMBER:
            # !TODO: show winning screen
            return

        self.map.load()
        self.player.x = self.map.player_start[0]
        self.player.y = self.map.player_start[1]

    def update(self):
        self.render()
        self.player.update(self.map, self)
        if self.map.points == 0:
            self.next_level()
        self.time += 1/60