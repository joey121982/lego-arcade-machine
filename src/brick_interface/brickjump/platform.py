import pygame
from .constants import *

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill((0, 255, 0))  # Green platform
        self.rect = self.image.get_rect(topleft=(x, y))