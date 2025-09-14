import pygame
import math

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, image, speed, angle, color):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.angle = angle
        self.color = color

        rad_angle = math.radians(self.angle)
        self.dx = self.speed * math.cos(rad_angle)
        self.dy = self.speed * math.sin(rad_angle)

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Check if the bullet is off-screen
        if self.rect.x < 0 or self.rect.x > pygame.display.get_surface().get_width() or \
              self.rect.y < 0 or self.rect.y > pygame.display.get_surface().get_height():
            self.kill()