import json
import pygame

class Map:
    def __init__(self):
        self.width = 16
        self.height = 9
        self.maze = [[0 for _ in range(self.width)] for _ in range(self.height)]
        with open("./assets/test.json", "r") as file:
            data = json.load(file)
            file.close()
        for i, row in enumerate(data["maze"]):
            for j, el in enumerate(row):
                self.maze[i][j] = int(el)
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


