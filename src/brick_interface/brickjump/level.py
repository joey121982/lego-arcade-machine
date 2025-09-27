import pygame
import math
import random
from .constants import *
from .platform import *
from brick_interface.brickjump.pillar import Pillar

class Level:
    def __init__(self):
        # groups for platforms and pillars
        self.platforms = pygame.sprite.Group()
        self.pillars = pygame.sprite.Group()


        self.create_initial_elements()
        
    def create_initial_elements(self):
        # create pillars on both sides
        lower_left_pillar = Pillar(CONTAINER_AREA_TOP_X, CONTAINER_AREA_TOP_Y + PILLAR_HEIGHT)
        lower_right_pillar = Pillar(SCREEN_WIDTH - PILLAR_WIDTH - CONTAINER_AREA_TOP_X, CONTAINER_AREA_TOP_Y + PILLAR_HEIGHT)
        left_pillar = Pillar(CONTAINER_AREA_TOP_X, CONTAINER_AREA_TOP_Y)
        right_pillar = Pillar(SCREEN_WIDTH - PILLAR_WIDTH - CONTAINER_AREA_TOP_X, CONTAINER_AREA_TOP_Y)
        upper_left_pillar = Pillar(CONTAINER_AREA_TOP_X, CONTAINER_AREA_TOP_Y - PILLAR_HEIGHT)
        upper_right_pillar = Pillar(SCREEN_WIDTH - PILLAR_WIDTH - CONTAINER_AREA_TOP_X, CONTAINER_AREA_TOP_Y - PILLAR_HEIGHT)
        self.pillars.add(lower_left_pillar, lower_right_pillar, left_pillar, right_pillar, upper_left_pillar, upper_right_pillar)

        # create some random platforms for testing
        platform = Platform(LEFT_PLATFORM_X, PLATFORM_INIT_Y)
        self.platforms.add(platform)
        for i in range(1, 5):
            y = PLATFORM_INIT_Y - i * PLATFORM_Y_GAP
            x = random.choice([LEFT_PLATFORM_X, RIGHT_PLATFORM_X])
            platform = Platform(x, y)
            self.platforms.add(platform)
    
    def update(self):
        # recycle platforms that go off screen
        for i in range(1, ON_SCREEN_NUMBER_OF_PLATFORMS):
            y = PLATFORM_INIT_Y - i * SCROLL
            y_platform_exists = False
            for platform in self.platforms:
                if platform.rect.y == y:
                    y_platform_exists = True
            if not y_platform_exists:
                x = random.choice([LEFT_PLATFORM_X, RIGHT_PLATFORM_X])
                new_platform = Platform(x, y)
                self.platforms.add(new_platform)
        # recycle pillars that go off screen
        for pillar in self.pillars:
            if pillar.rect.y > SCREEN_HEIGHT + SCROLL:
                y = pillar.rect.y
                pillar.kill()
                new_pillar = Pillar(pillar.rect.x, y - 3 * PILLAR_HEIGHT)
                self.pillars.add(new_pillar)
        
    def draw(self, screen):
        self.pillars.draw(screen)

        self.platforms.update()
        for platform in self.platforms:
            platform.draw(screen)
        