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
         
        
class Map:
    def __init__(self):
        self.width = 10
        self.height = 10
        self.maze = [
            [0,1,0,0,0,1,1,0,0,1],
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

    def render(self, screen, tilesize):
        space = (10,10,10)
        wall = (200,200,200)
        for j in range(0, self.height):
            for i in range(0, self.width):
                color = wall if self.maze[i][j] else space 
                pygame.draw.rect(screen, color, pygame.Rect(j*tilesize, i*tilesize, tilesize, tilesize))






class Brickman:
    name = "BrickMan"
    running = True
    direction = "none"
    
    def __init__(self, screen, globals):
        self.screen = screen
        self.globals = globals
        self.map = Map()
        self.player = Player(self.map.player_start[0], self.map.player_start[1])
        self.tilesize = self.globals.WINHEIGHT//self.map.height

    def render(self):
        self.screen.fill((0,0,0))
        self.map.render(self.screen, self.tilesize)
        self.player.render(self.screen, self.tilesize)
        pygame.display.update()

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
        self.render()