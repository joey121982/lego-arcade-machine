import pygame
import math

class Brickinvaders:
    name = "Brick Invaders"
    running = True
    
    def __init__(self, screen, glb):
        self.running = True
        self.screen = screen
        self.glb = glb

        # Initialize spaceship
        self.spaceship = pygame.Surface((100, 100), pygame.SRCALPHA)
        pygame.draw.polygon(self.spaceship, (255, 0, 0), [(50, 0), (100, 100), (0, 100)])

        self.spaceship_x = self.screen.get_width() // 2 - 50
        self.spaceship_y = self.screen.get_height() - 250

        # Spaceship movement variables
        self.spaceship_velocity = 0
        self.spaceship_acceleration = 0.5
        self.spaceship_friction = 0.5
        self.spaceship_velocity_limit = 15

        # Spaceship angle
        self.spaceship_angle = 0
        self.spaceship_angle_sign = 0
        self.spaceship_angle_increment = 5

        # Background things
        self.background = pygame.image.load('./assets/BI_background.png').convert()
        self.background = pygame.transform.scale(self.background, (self.glb.WINWIDTH, self.glb.WINHEIGHT))
        self.background_width = self.background.get_width()
        self.background_height = self.background.get_height()
    
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Space key pressed in Brick Invaders!")
                self.spaceship.fill((0, 255, 0)) 
            if event.key == pygame.K_ESCAPE:
                print("Escape key pressed in Brick Invaders! Returning to menu...")
                self.running = False
                self.glb.return_to_menu = True  # Signal to return to menu

    def update_spaceship_position(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.spaceship_velocity -= self.spaceship_acceleration
            #self.spaceship_angle_sign = 1
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.spaceship_velocity += self.spaceship_acceleration
            #self.spaceship_angle_sign = -1
        else:
            if self.spaceship_velocity > 0:
                self.spaceship_velocity -= self.spaceship_friction
            elif self.spaceship_velocity < 0:
                self.spaceship_velocity += self.spaceship_friction

        self.spaceship_velocity = max(-self.spaceship_velocity_limit, min(self.spaceship_velocity, self.spaceship_velocity_limit))
        self.spaceship_x += self.spaceship_velocity
        if self.spaceship_x < 50:
            self.spaceship_x = 50
            self.spaceship_velocity = 0
        elif self.spaceship_x > self.screen.get_width() - 150:
            self.spaceship_x = self.screen.get_width() - 150
            self.spaceship_velocity = 0

        self.spaceship_angle = (self.spaceship_velocity // 5) * self.spaceship_angle_increment * -1
        
    
    def update(self):
        
        # move spaceship
        self.update_spaceship_position()

        # background
        self.tiles = math.ceil(self.screen.get_width() / self.background_width) + 1
        self.screen.blit(self.background, (0, 0))

        # rotate spaceship logic
        rotated_spaceship = pygame.transform.rotozoom(self.spaceship, self.spaceship_angle, 1)
        rotated_rect = rotated_spaceship.get_rect(center=(self.spaceship_x + 50, self.spaceship_y + 50))

        # draw spaceship
        self.screen.blit(rotated_spaceship, rotated_rect.topleft)

        pygame.display.flip()