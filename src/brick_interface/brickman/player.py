import pygame
from math import floor

class Player:
    direction = "none"
    next_direction = "none"
    x = 0
    y = 0

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def render(self, screen, tilesize):
        color = (255,0,0)
        pygame.draw.rect(screen, color, pygame.Rect(self.x*tilesize, self.y*tilesize, tilesize, tilesize))
    
    def controls(self):
        keys=pygame.key.get_pressed()

        state = {
            "w":keys[pygame.K_w],
            "s":keys[pygame.K_s],
            "a":keys[pygame.K_a],
            "d":keys[pygame.K_d]
        }

        if state["w"]:
            self.next_direction = "up"
        elif state["s"]:
            self.next_direction = "down"
        elif state["a"]:
            self.next_direction = "left"
        elif state["d"]:
            self.next_direction = "right"
         
    def update(self, map):
        self.controls()
        dir_x = 0
        dir_y = 0
        movespeed = 1/12
        if self.direction == "right":
            dir_x += 1 
        if self.direction == "up":
            dir_y -= 1 
        if self.direction == "down":
            dir_y += 1 
        if self.direction == "left":
            dir_x -= 1 
        print(floor(self.x) + dir_x)
        if map.maze[floor(self.y) + dir_y][floor(self.x) + dir_x] != 1 :
            self.x += dir_x * movespeed
            self.y += dir_y * movespeed
        if self.direction == "none" and self.next_direction != "none":
            self.direction = self.next_direction
        