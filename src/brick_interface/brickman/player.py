import pygame
from math import floor, ceil

# helper function to check if direction and next_direction are opposites
def opposite_check(x, y):
    opposites = {
        "up": "down",
        "down": "up",
        "left": "right",
        "right": "left"
    }
    return opposites.get(x) == y

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
        pygame.draw.rect(screen, color, pygame.Rect(self.x * tilesize, self.y * tilesize, tilesize, tilesize))
    
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

    def update(self, map, super):
        # --- TODO
        # rewrite to reduce code, specifically in the collision checks
        # also, currently in the case of successfully changing direction mid-movement,
        # collision checks are done twice.
        #
        # p.s. este 5 dimineata in momentul in care scriu acest cod, my apologies.
        # --- joey

        self.controls()
        movespeed = round(1 / 12, 1) # 0.1, but leave this as is, so we can change the speed later.

        # ---
        # if next_direction is the opposite of direction, we can safely replace them,
        # as going back from where you just left means there WAS a space there.
        # 
        # warning: this assumes logic applies to videogames.
        # --- joey

        if self.next_direction != "none" and opposite_check(self.direction, self.next_direction):
            self.direction = self.next_direction
            self.next_direction = "none" 

        # ---
        # if we are right on top of a grid element (not skewed in any direction)
        # we can check if next_direction is currently a possible replacement for direction.
        # --- joey

        if self.next_direction != "none" and (self.x == int(self.x) and self.y == int(self.y)):
            dir_x = 0
            dir_y = 0
            if self.next_direction == "right":
                dir_x += 1
            if self.next_direction == "up":
                dir_y -= 1
            if self.next_direction == "down":
                dir_y += 1
            if self.next_direction == "left":
                dir_x -= 1
            if self.direction == "left" or self.direction == "up":
                checked_tile = map.maze[floor(self.y + dir_y)][floor(self.x + dir_x)]
            else:
                checked_tile = map.maze[ceil(self.y + dir_y)][ceil(self.x + dir_x)]
            if checked_tile != 1:
                self.direction = self.next_direction
                self.next_direction = "none"
                
        dir_x = 0
        dir_y = 0
        if self.direction == "right":
            dir_x += 1
        if self.direction == "up":
            dir_y -= 1
        if self.direction == "down":
            dir_y += 1
        if self.direction == "left":
            dir_x -= 1

        # ---
        # we check for collisions on the resulting tile after movement occurs.
        # if movement causes the player to collide with a wall, we stop the movement
        # and reset direction to "none".
        # --- joey

        if self.direction == "left" or self.direction == "up":
            checked_tile = map.maze[floor(self.y + dir_y * 0.01)][floor(self.x + dir_x * 0.01)]
        else:
            checked_tile = map.maze[ceil(self.y + dir_y * 0.01)][ceil(self.x + dir_x * 0.01)]

        if checked_tile != 1:
            self.y = round(self.y + dir_y * movespeed, 2)
            self.x = round(self.x + dir_x * movespeed, 2)
        else:
            self.direction = "none"
        if self.direction == "none" and self.next_direction != "none":
            self.direction = self.next_direction
       
        if (self.x == int(self.x) and self.y == int(self.y)):
            point_score = 5 
            fruit_score = 20

            if map.maze[int(self.y)][int(self.x)] == 0:
                super.score_value += point_score
                map.maze[int(self.y)][int(self.x)] = -1
                map.points -= 1

            if map.maze[int(self.y)][int(self.x)] == 2:
                super.score_value += fruit_score
                map.maze[int(self.y)][int(self.x)] = -1
                map.points -= 1