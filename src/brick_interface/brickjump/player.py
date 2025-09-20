import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.velocity_x = 0
        self.velocity_y = 0
        self.on_ground = False
        self.jump_power = -15
        self.gravity = 0.8
        self.speed = 5