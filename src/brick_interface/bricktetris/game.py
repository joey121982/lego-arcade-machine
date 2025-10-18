import pygame
from .constants import *
from .screens import *

class Bricktetris:
    name = "Brick Tetris"
    running = True
    
    def __init__(self, screen, globals):
        self.screen = screen
        self.glb = globals
        self.clock = pygame.time.Clock()
        
        self.background_image, self.main_screen_image, self.next_screen_image, self.info_screen_image = load_images()
        
        # create screen instances
        self.playable_screen = PlayableScreen(self.screen, MAIN_SCREEN_X, MAIN_SCREEN_Y)
        self.info_screen = InfoScreen(self.screen, INFO_SCREEN_X, INFO_SCREEN_Y, self.info_screen_image)
        self.next_screen = NextScreen(self.screen, NEXT_SCREEN_X, NEXT_SCREEN_Y, self.next_screen_image)
        
        # game timer, add falling events
        self.current_level = 1
        self.fall_speed = 500 # ms
        self.FALL_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.FALL_EVENT, self.fall_speed)
        
        # move sideways timers
        self.move_sideways_timer = 0
        self.move_sideways_delay = MOVE_SIDEWAYS_DELAY # ms
        
        # move down timers
        self.move_down_timer = 0
        self.move_down_delay = MOVE_DOWN_DELAY # ms

    def handle_event(self, event):
        if event.type == self.FALL_EVENT:
            self.playable_screen.drop()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.running = False
                if hasattr(self.glb, 'return_to_menu'):
                    self.glb.return_to_menu = True
                return
            
            if event.key == pygame.K_r:
                self.__init__(self.screen, self.glb)
                return

            # if the game is over, we ignore gameplay key presses
            if self.playable_screen.game_over:
                return

            # gameplay controls
            # if event.key == pygame.K_a:
            #     self.playable_screen.move_left()
            # elif event.key == pygame.K_d:
            #     self.playable_screen.move_right()
            # elif event.key == pygame.K_s:
            #     self.playable_screen.drop()
            if event.key == pygame.K_w:
                self.playable_screen.rotate()

    def update(self):
        # hold down key handling
        keys = pygame.key.get_pressed()
        if not self.playable_screen.game_over:
            move_down = keys[pygame.K_s]
            if move_down:
                self.move_down_timer += 1
                if self.move_down_timer > self.move_down_delay:
                    self.move_down_timer = 0
                    self.playable_screen.drop()
            else:
                self.move_down_timer = 0

            move_left = keys[pygame.K_a]
            move_right = keys[pygame.K_d]
            if move_left or move_right:
                self.move_sideways_timer += 1
                if self.move_sideways_timer > self.move_sideways_delay:
                    self.move_sideways_timer = 0
                    if move_left:
                        self.playable_screen.move_left()
                    if move_right:
                        self.playable_screen.move_right()
            else:
                self.move_sideways_timer = 0

        # draw static background elements
        self.screen.blit(self.background_image, (0, 0))
        self.screen.blit(self.main_screen_image, (MAIN_SCREEN_X, MAIN_SCREEN_Y))
        
        # update and draw game state from the playable screen
        self.playable_screen.draw()
        
        # update and draw info/next screens
        self.info_screen.draw(
            self.playable_screen.score, 
            self.playable_screen.level, 
            self.playable_screen.lines_cleared_total
        )
        self.next_screen.draw(self.playable_screen.next_piece_shape)
        
        # difficulty adjustment based on level
        if self.playable_screen.level != self.current_level:
            self.current_level = self.playable_screen.level
            new_fall_speed = max(100, 500 - (self.current_level - 1) * 40)
            self.fall_speed = new_fall_speed
            pygame.time.set_timer(self.FALL_EVENT, self.fall_speed)

        # basic game over display
        if self.playable_screen.game_over:
            font = pygame.font.Font("./assets/bricktetris/fonts/Pixellettersfull-BnJ5.ttf", 100)
            text = font.render('GAME OVER', True, WHITE)
            text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
            self.screen.blit(text, text_rect)

        pygame.display.flip()
        self.clock.tick(60)

