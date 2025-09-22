import pygame
from .constants import *

def check_player_below_screen(self):
    if self.player.rect.top > SCREEN_HEIGHT:
        self.running = False
        self.glb.return_to_menu = True  # signal to return to menu
        print("check_player_below_screen function triggered")
    

def advance(self):
    if self.player.on_ground and self.player.prev_y != self.player.rect.y:
        for sprite in self.level.platforms:
            sprite.rect.y += SCROLL
        for sprite in self.level.pillars:
            sprite.rect.y += SCROLL
        self.scroll += SCROLL
        self.player.rect.y += SCROLL
        self.player.prev_y = self.player.rect.y