import pygame
from .constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.velocity_x = 0
        self.velocity_y = 0
        self.on_ground = False
        self.jump_power = -15
        self.gravity = 0.8
        self.speed = 5
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT

        self.rect = pygame.Rect(x, y, self.width, self.height)

        self.prev_y = PLATFORM_INIT_Y - PLAYER_HEIGHT

    def update(self, platforms):
        # Apply gravity
        if not self.on_ground:
            self.velocity_y += self.gravity

        # Update position
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

        # Reset ground state
        self.on_ground = False
        
        # Check for platform collision
        for platform in platforms:
            if self.rect.bottom == platform.rect.top:
                self.on_ground = True
                self.velocity_y = 0
                break
            elif self.rect.colliderect(platform.rect):
                # Only handle landing on top of platform when falling
                if self.velocity_y > 0:  # Player is falling down
                    self.on_ground = True
                    self.velocity_y = 0
                    self.rect.bottom = platform.rect.top
                    break  # Stop checking once we find a collision
                
    def move_up(self):
        self.prev_y = self.rect.y
        self.rect.y -= HOVER + SCROLL

    def move_left(self):
        self.prev_y = self.rect.y
        self.rect.y -= HOVER + SCROLL
        self.rect.x = LEFT_PLATFORM_X + PLATFORM_WIDTH // 2 - PLAYER_WIDTH // 2

    def move_right(self):
        self.prev_y = self.rect.y
        self.rect.y -= HOVER + SCROLL
        self.rect.x = RIGHT_PLATFORM_X + PLATFORM_WIDTH // 2 - PLAYER_WIDTH // 2

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), self.rect)
