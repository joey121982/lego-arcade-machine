import pygame

from menu import *
from brickjump.game import *
from brickinvaders.game import *
from brickman.game import *
from brickfighter.game import *

GameType = Brickjump | Brickinvaders | Brickfighter | Brickman | Menu

class Shell:
    game: GameType = Menu()

    def parse_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def update(self):
        self.game.update()
        if isinstance(self.game, Menu) and self.game.new_game != "None":
            ngame = self.game.new_game
            if ngame == "Brick Invaders":
                self.game = Brickinvaders()
                return
            if ngame == "Brick Jump":
                self.game = Brickjump()
                return
            if ngame == "BrickMan":
                self.game = Brickman()
                return
            if ngame == "Brick Fighter":
                self.game = Brickfighter()
                return
