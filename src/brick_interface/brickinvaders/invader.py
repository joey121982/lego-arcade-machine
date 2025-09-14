import pygame
import math
import random
from .utilities import *
from .constants import *
from .bullet import Bullet

class Invader(pygame.sprite.Sprite):
    def __init__(self, x, y, spritesheet, speed, starting_frame, shooting_chance, enemy_bullet_image, enemy_bullets):
        super().__init__()
        self.spritesheet = spritesheet
        self.image = self.spritesheet.subsurface((0, 0, INVADER_FRAME_WIDTH, INVADER_FRAME_HEIGHT))
        self.image = pygame.transform.scale(self.image, (INVADER_WIDTH, INVADER_HEIGHT))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.actual_x = x
        self.speed = speed
        self.frame = starting_frame
        self.shooting_chance = shooting_chance
        self.enemy_bullet_image = enemy_bullet_image
        self.enemy_bullets = enemy_bullets

    def shoot(self):
        bullet = Bullet(self.rect.x + INVADER_WIDTH // 2, self.rect.y + INVADER_HEIGHT, self.enemy_bullet_image, speed=INVADER_BULLET_SPEED, angle=90, color=(255, 0, 0))
        self.enemy_bullets.add(bullet)

    def update(self, global_direction, func):
        self.image = func(self, self.spritesheet, self.frame % INVADER_TOTAL_FRAMES)
        if self.speed != 0:
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
        # Shooting logic
        if self.shooting_chance and random.random() < self.shooting_chance:
            self.shoot()