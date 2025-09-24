import pygame
from .constants import *
from .utilities import *

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill((0, 255, 0))  # Green platform
        self.rect = self.image.get_rect(topleft=(x, y))
        self.touched = False

        self.is_shaking = False
        self.shake_start_time = -1

        self.visual_offset_x = 0
        self.visual_offset_y = 0

        self.shake_duration = (INIT_PLATFORM_SHAKE_DURATION * 10 if y == PLATFORM_INIT_Y else max(MIN_PLATFORM_SHAKE_DURATION, INIT_PLATFORM_SHAKE_DURATION - (abs(y - PLATFORM_INIT_Y) // 10000) * 100))
        self.shake_intensity = SHAKE_INTENSITIY

    def update(self):
        if self.touched and not self.is_shaking:
            self.shake_start_time = pygame.time.get_ticks()
            self.is_shaking = True
            self.touched = False
        if self.is_shaking:
            platform_shake(self)
    
    def draw(self, screen):
        visual_x = self.rect.x + self.visual_offset_x
        visual_y = self.rect.y + self.visual_offset_y
        screen.blit(self.image, (visual_x, visual_y))