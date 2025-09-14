import pygame    

class Map:
    def __init__(self, globals):
        self.glb = globals
        self.floor_height = 300 # pixels
        self.rect = pygame.Rect(0, self.glb.WINHEIGHT - self.floor_height, self.glb.WINWIDTH, self.floor_height)