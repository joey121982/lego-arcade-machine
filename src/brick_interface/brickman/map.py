import json
import pygame

class Map:
    def __init__(self):
        self.width = 16
        self.height = 9
        self.points = 0 # map.points counts the amount of tiles with aquirable points left, including fruits.
        self.level = 1 # current map number (starts at 1 for map1.json)
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
        wall = (200,200,200)
        for i in range(0, self.height):
            for j in range(0, self.width):
                # 0 = punct    1 = perete     2 = fruct     -1 = spatiu 
                color = wall if self.maze[i][j] == 1 else space 
                pygame.draw.rect(screen, color, pygame.Rect(j*tilesize, i*tilesize, tilesize, tilesize))

                is_fruit = self.maze[i][j] == 2
                if is_fruit:
                    pygame.draw.circle(screen, (255, 0, 0), (j*tilesize + tilesize//2, i*tilesize + tilesize //2), tilesize//6)
                
                is_coin = self.maze[i][j] == 0 
                if is_coin:
                    pygame.draw.circle(screen, (255, 255, 255), (j*tilesize + tilesize//2, i*tilesize + tilesize //2), tilesize//12)


