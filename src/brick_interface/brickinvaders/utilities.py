import pygame
import math
from .constants import *
from .invader import Invader

def setup_level(self, level_data):
        self.invaders.empty()
        rows = level_data["rows"]
        columns = level_data["columns"]
        speed = level_data["invader_speed"]
        pattern = level_data.get("pattern", "default")
        # You can expand pattern logic here if needed

        horizontal_spacing  = (SCREEN_WIDTH - columns * (INVADER_WIDTH * 2)) // 2 + INVADER_WIDTH
        vertical_spacing = INVADER_HEIGHT
        if pattern == "default":
            for row in range(rows):
                for col in range(columns):
                    x = horizontal_spacing + col * (INVADER_WIDTH * 2)
                    y = vertical_spacing + row * (INVADER_HEIGHT * 2)
                    invader = Invader(x, y, self.invader_image, speed)
                    self.invaders.add(invader)
        elif pattern == "zigzag":
            for row in range(rows):
                for col in range(columns):
                    x = horizontal_spacing + col * (INVADER_WIDTH * 2) + (row % 2) * INVADER_WIDTH
                    y = vertical_spacing + row * (INVADER_HEIGHT * 2)
                    invader = Invader(x, y, self.invader_image, speed)
                    self.invaders.add(invader)
        elif pattern == "dense":
            for row in range(rows):
                for col in range(columns):
                    x = horizontal_spacing + col * (INVADER_WIDTH * 1.5)
                    y = vertical_spacing + row * (INVADER_HEIGHT * 1.5)
                    invader = Invader(x, y, self.invader_image, speed)
                    self.invaders.add(invader)
        elif pattern == "semicircle":
            for row in range(rows):
                for col in range(columns):
                    if col == 0 or col == columns - 1 or row == 0:
                        x = horizontal_spacing + col * (INVADER_WIDTH * 2)
                        y = vertical_spacing + row * (INVADER_HEIGHT * 2)
                        invader = Invader(x, y, self.invader_image, speed)
                        self.invaders.add(invader)

def check_bullet_invader_collisions(self):
        for bullet in self.bullets:
            if pygame.sprite.spritecollideany(bullet, self.invaders):
                collided_invader = pygame.sprite.spritecollideany(bullet, self.invaders)
                bullet.kill()
                collided_invader.kill()
                # Play explosion sound or show explosion animation
                # explosion_sound = pygame.mixer.Sound('./assets/brickinvaders/images/explosion.wav')
                # explosion_sound.play()

def check_invader_spaceship_collisions(self):
        for invader in self.invaders:
            if invader.rect.colliderect(pygame.Rect(self.spaceship.x, self.spaceship.y, 100, 100)):
                # Handle collision (e.g., end game or reduce life)
                self.running = False
                print("Game Over! An invader hit your spaceship.")
                break                     