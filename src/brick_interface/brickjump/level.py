import pygame
import math
import random
from .constants import *
from .platform import *
from brick_interface.brickjump.pillar import Pillar

class Level:
    def __init__(self):
        self.platforms = pygame.sprite.Group()
        self.pillars = pygame.sprite.Group()
        
        # Create pillars on both sides
        left_pillar = Pillar(CONTAINER_AREA_TOP_X, CONTAINER_AREA_TOP_Y)
        right_pillar = Pillar(SCREEN_WIDTH - PILLAR_WIDTH - CONTAINER_AREA_TOP_X, CONTAINER_AREA_TOP_Y)
        upper_left_pillar = Pillar(CONTAINER_AREA_TOP_X, CONTAINER_AREA_TOP_Y + PILLAR_HEIGHT)
        upper_right_pillar = Pillar(SCREEN_WIDTH - PILLAR_WIDTH - CONTAINER_AREA_TOP_X, CONTAINER_AREA_TOP_Y + PILLAR_HEIGHT)
        self.pillars.add(left_pillar, right_pillar, upper_left_pillar, upper_right_pillar)

        # Create some random platforms for testing
        for i in range(5):
            y = PLATFORM_INIT_Y - i * 120
            if i % 2 == 0:
                platform = Platform(LEFT_PLATFORM_X, y)
            else:
                platform = Platform(RIGHT_PLATFORM_X, y)
            self.platforms.add(platform)
        
    def draw(self, screen):
        self.pillars.draw(screen)
        self.platforms.draw(screen)
        