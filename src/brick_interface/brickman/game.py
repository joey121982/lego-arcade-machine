import pygame

class Player:
    x = 0
    y = 0

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def render(self, screen, tilesize):
        pass
         
        
class Map:
    def __init__(self):
        self.maze = [
            [0,1,0,0,0,1,1,0,0,1],
            [0,1,0,0,0,1,1,0,0,1],
            [0,1,0,0,0,1,1,0,0,1],
            [0,1,0,0,0,1,1,0,0,1],
            [0,1,0,0,0,1,1,0,0,1],
            [0,1,0,0,0,1,1,0,0,1],
            [0,1,0,0,0,1,1,0,0,1],
            [0,1,0,0,0,1,1,0,0,1],
            [0,1,0,0,0,1,1,0,0,1]
        ]
        self.player_start = [3,3]






class Brickman:
    name = "BrickMan"
    running = True
    direction = "none"
    
    def __init__(self, screen, globals):
        self.screen = screen
        self.globals = globals
        self.map = Map()
        self.player = Player(map.player_start[0], map.player_start[1])

    def controls(self):
        keys=pygame.key.get_pressed()

        state = {
            "w":keys[pygame.K_w],
            "s":keys[pygame.K_s],
            "a":keys[pygame.K_a],
            "d":keys[pygame.K_d]
        }

        if state["w"]:
            self.direction = "up"
        elif state["s"]:
            self.direction = "down"
        elif state["a"]:
            self.direction = "left"
        elif state["d"]:
            self.direction = "right"

    def update(self):
        pass