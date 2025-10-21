import json
import pygame

class Map:
    def __init__(self, glb):
        self.width = 16
        self.height = 9
        self.points = 0 # map.points counts the amount of tiles with aquirable points left, including fruits.
        self.level = 1 # current map number (starts at 1 for map1.json)
        self.globals = glb
        self.tilesize = self.globals.WINHEIGHT // self.height
        self.wall_texture = pygame.image.load("./assets/brickman/wall.png")
        self.back_texture = pygame.image.load("./assets/brickman/wall.png")
        self.back_texture = pygame.transform.scale(self.back_texture, (self.tilesize, self.tilesize))
        self.wall_texture = pygame.transform.scale(self.wall_texture, (self.tilesize, self.tilesize))
        self.load()

    def load(self):
        map_name = "map" + str(self.level)
        self.maze = [[0 for _ in range(self.width)] for _ in range(self.height)]
        with open("./assets/brickman-maps/" + map_name + ".json", "r") as file:
            data = json.load(file)
            file.close()
        for i, row in enumerate(data["maze"]):
            for j, el in enumerate(row):
                self.maze[i][j] = int(el)
                if int(el) == 0 or int(el) == 2:
                    self.points += 1
        self.player_start = data["player_start"]

    def render(self, screen, tilesize):
        space = (10,10,10)
        # wall = (200,200,200)

        for i in range(0, self.height):
            for j in range(0, self.width):
                # 0 = punct    1 = perete     2 = fruct     -1 = spatiu
                 
                # color = wall if self.maze[i][j] == 1 else space 
                # pygame.draw.rect(screen, color, pygame.Rect(j*tilesize, i*tilesize, tilesize, tilesize))
                self.back_texture.set_alpha(50)

                if self.maze[i][j] == -1:
                    # pygame.draw.rect(screen, space, pygame.Rect(j*tilesize, i*tilesize, tilesize, tilesize))
                    screen.blit(self.back_texture, (j * tilesize, i * tilesize))

                if self.maze[i][j] == 1:
                    screen.blit(self.wall_texture, (j * tilesize, i * tilesize))

                is_fruit = self.maze[i][j] == 2
                if is_fruit:
                    screen.blit(self.back_texture, (j * tilesize, i * tilesize))
                    pygame.draw.circle(screen, (255, 0, 0), (j*tilesize + tilesize//2, i*tilesize + tilesize //2), tilesize//6)
                
                is_coin = self.maze[i][j] == 0 
                if is_coin:
                    screen.blit(self.back_texture, (j * tilesize, i * tilesize))
                    pygame.draw.circle(screen, (255, 255, 255), (j*tilesize + tilesize//2, i*tilesize + tilesize //2), tilesize//12)