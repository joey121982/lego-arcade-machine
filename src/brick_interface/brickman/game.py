# ...existing code...
import pygame
from .map import *
from .player import *

##############################
##############################
##############################
FINAL_MAP_NUMBER = 3
##############################
##############################
##############################

class Brickman:
    name = "Brick Man"
    running = True

    def __init__(self, screen, globals):
        self.screen = screen
        self.globals = globals
        self.map = Map(self.globals)
        self.tilesize = self.globals.WINHEIGHT//self.map.height
        self.player = Player(self.tilesize, self.map.player_start[0], self.map.player_start[1])
        self.score_raw = 0
        self.score_value = 0
        self.font_path = "././assets/fonts/Pixellettersfull-BnJ5.ttf"

        self.start_ticks = pygame.time.get_ticks()
        self.elapsed_seconds = 0.0

    def display_score (self):
        try:
            font = pygame.font.Font(self.font_path, 24)
        except Exception:
            font = pygame.font.SysFont(None, 24)

        # time elapsed
        self.elapsed_seconds = (pygame.time.get_ticks() - self.start_ticks) / 1000.0
        elapsed_int = int(self.elapsed_seconds)
        minutes = elapsed_int // 60
        seconds = elapsed_int % 60
        time_text = f"{minutes:02d}:{seconds:02d}"

        eff = self.score_raw / max(1.0, self.elapsed_seconds)
        eff_text = f"{eff:.2f}"
        
        eff_surface = font.render(f"Score/time: {eff_text}", True, (255, 0, 0))
        self.screen.blit(eff_surface, (self.globals.WINWIDTH/2 - 120, self.tilesize/3))

        raw_surface = font.render(f"Raw: {self.score_raw}", True, (200, 200, 200))
        self.screen.blit(raw_surface, (self.globals.WINWIDTH/2 - 120, self.tilesize/3 + 28))

        time_surface = font.render(f"Time: {time_text}", True, (200, 200, 200))
        self.screen.blit(time_surface, (self.globals.WINWIDTH/2 + 40, self.tilesize/3))

    def render(self):
        self.screen.fill((0,0,0))
        self.map.render(self.screen, self.tilesize)
        self.player.render(self.screen)
        self.display_score()

        if self.globals.DEBUG_MODE == True:
            try:
                font = pygame.font.Font(self.font_path, 24)
            except Exception:
                font = pygame.font.SysFont(None, 24)
            coord_text = f"DEBUG:   X: {self.player.x:.2f} | Y: {self.player.y:.2f} | DIR: {self.player.direction}"
            text_surface = font.render(coord_text, True, (255, 0, 0))
            screen_rect = pygame.display.get_surface().get_rect()
            self.screen.blit(text_surface, (10, screen_rect.height - 30))

        pygame.display.update()

    def next_level(self):
        self.map.level += 1

        if self.map.level == FINAL_MAP_NUMBER:
            elapsed = (pygame.time.get_ticks() - self.start_ticks) / 1000.0
            elapsed = max(1.0, elapsed)
            efficiency = self.score_raw / elapsed
            self.score_value = int(efficiency)

            self.running = False
            self.globals.return_to_menu = True
            return

        self.map.load()
        self.player.x = self.map.player_start[0]
        self.player.y = self.map.player_start[1]

    def update(self):

        self.render()
        self.player.update(self.map, self)

        # if map cleared, advance to next level
        if self.map.points == 0:
            self.next_level()
