import pygame
from .constants import *
from .player import *
from .level import *
from .utilities import *

class Brickjump():
    name = "Brick Jump"
    running = True

    def __init__(self, screen, glb):
        self.screen = screen
        self.running = True
        self.level = Level()
        self.glb = glb
        
        # the score
        self.score = 0

        # player
        self.player = Player(PLAYER_ON_LEFT_PLATFORM_X, PLATFORM_INIT_Y - PLAYER_HEIGHT)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.running = False
                self.glb.return_to_menu = True  # signal to return to menu
            if event.key == pygame.K_a and self.player.on_ground:
                if self.player.rect.x == PLAYER_ON_LEFT_PLATFORM_X:
                    self.player.move_up()
                else:
                    self.player.move_left()
            if event.key == pygame.K_d and self.player.on_ground:
                if self.player.rect.x == PLAYER_ON_RIGHT_PLATFORM_X:
                    self.player.move_up()
                else:
                    self.player.move_right()
                
    def update(self):
        self.screen.fill(UNDERGROUND_BROWN)


        self.level.update()
        self.level.draw(self.screen)

        self.player.update(self.level.platforms)
        self.player.draw(self.screen)

        check_player_platform_collisions(self)
        check_player_below_screen(self)
        advance(self)

        for platform in self.level.platforms:
            print(platform.touched, platform.is_shaking)
        
        pygame.display.flip()