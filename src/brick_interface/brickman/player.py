import pygame

class Player:
    x = 0
    y = 0

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def render(self, screen, tilesize):
        color = (255,0,0)
        pygame.draw.rect(screen, color, pygame.Rect(self.x*tilesize, self.y*tilesize, tilesize, tilesize))
    
    #def update(self)
         