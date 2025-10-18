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
        
        # load images
        self.bunny_images, self.background_image = load_game_images()
        
        # the score
        self.score = 0

        # player
        self.player = Player(PLAYER_ON_LEFT_PLATFORM_X, PLATFORM_INIT_Y - PLAYER_HEIGHT, self.bunny_images)
        
        # timer since start
        self.start_time = pygame.time.get_ticks()
        self.elapsed_time = 0

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
        # draw background
        self.background_image_tinted = self.background_image.copy()
        self.background_image_tinted.fill(TINTS[((max(4, self.score) - 4) // 100) % 5], special_flags=pygame.BLEND_RGBA_MULT)
        self.screen.blit(self.background_image_tinted, (0, 0))

        self.level.update(self.score)
        self.level.draw(self.screen)

        self.player.update(self.level.platforms)
        self.player.draw(self.screen)
        
        # draw score left corner
        score_text = pygame.font.SysFont('Arial', 30).render(f'Score: {self.score}', True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        
        # count time
        self.elapsed_time = (pygame.time.get_ticks() - self.start_time) // 1000
        
        # platforms per second left corner
        self.pps = self.score / max(1, self.elapsed_time)
        pps_text = pygame.font.SysFont('Arial', 30).render(f'Platforms per second: {self.pps:.2f}', True, (255, 255, 255))
        self.screen.blit(pps_text, (10, 40))

        check_player_below_screen(self)
        advance(self)
        
        pygame.display.flip()