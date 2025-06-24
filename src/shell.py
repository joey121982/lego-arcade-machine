# --- info
# shell-ul e doar un fel de "wrapper" pentru restul jocurilor
# fiecare joc deschis se afla in interiorul shellului
# ca sa putem trece usor de la meniu la unul din jocuri si inapoi.
# --- joey

import pygame

from menu.menu import *
from brickjump.game import *
from brickinvaders.game import *
from brickman.game import *
from brickfighter.game import *

# --- info
# "|" este operatorul bitwise or si aici doar creaza un "union" type de mai multe type-uri
# un union este un tip de data care spune ca obiectul poate fi mai de mai multe forme
# de ex boolint x = 10; boolint x = false;
#               ^ int           ^ boolean
# in cazul asta boolint este un union de "bool | int"
# --- joey
GameType = Brickjump | Brickinvaders | Brickfighter | Brickman | Menu | None

class Shell:
    screen = None
    glb = None
    game: GameType = None

    def parse_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def __init__(self, new_screen, new_globals):
        self.screen = new_screen
        self.glb = new_globals
        self.game = Menu(self.screen, self.glb)

    def update(self):
        if not self.game:
            return
        
        if self.game.running:
            self.game.update()
            
        if isinstance(self.game, Menu) and self.game.new_game != "None":
            ngame = self.game.new_game
            if ngame == "Brick Invaders":
                # self.game = Brickinvaders(self.screen)
                return
            if ngame == "Brick Jump":
                # self.game = Brickjump(self.screen)
                return
            if ngame == "Brick Man":
                # self.game = Brickman(self.screen)
                return
            if ngame == "Brick Fighter":
                # self.game = Brickfighter(self.screen)
                return
