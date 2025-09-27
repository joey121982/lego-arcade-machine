import pygame
import math
from .constants import *

class Pillar(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((PILLAR_WIDTH, PILLAR_HEIGHT))
        self.image.fill((128, 0, 128))  # purple pillar
        self.rect = self.image.get_rect(topleft=(x, y))