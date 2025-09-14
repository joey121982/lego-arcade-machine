import pygame
import math
from .utilities import *
from .constants import *

class Invader(pygame.sprite.Sprite):
    def __init__(self, x, y, spritesheet, speed, starting_frame):
        super().__init__()
        self.spritesheet = spritesheet
        self.image = self.spritesheet.subsurface((0, 0, INVADER_FRAME_WIDTH, INVADER_FRAME_HEIGHT))
        self.image = pygame.transform.scale(self.image, (INVADER_WIDTH, INVADER_HEIGHT))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.actual_x = x
        self.speed = speed
        self.frame = starting_frame

    def update(self, global_direction, func):
        self.image = func(self, self.spritesheet, self.frame % INVADER_TOTAL_FRAMES)
        if global_direction % 2 == 1:
            self.actual_x += self.speed * 1
            if self.actual_x - self.rect.x > self.rect.width:
                self.rect.x = self.actual_x
                self.frame += 1
        else:
            self.actual_x += self.speed * -1
            if self.rect.x - self.actual_x > self.rect.width:
                self.rect.x = self.actual_x
                self.frame += 1