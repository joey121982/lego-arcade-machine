import pygame

class Invader(pygame.sprite.Sprite):
    def __init__(self, x, y, image, speed):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.actual_x = x
        self.speed = speed

    def update(self, global_direction):
        if global_direction % 2 == 1:
            self.actual_x += self.speed * 1
            if self.actual_x - self.rect.x > self.rect.width:
                self.rect.x = self.actual_x
        else:
            self.actual_x += self.speed * -1
            if self.rect.x - self.actual_x > self.rect.width:
                self.rect.x = self.actual_x