import pygame
import math

class Invader(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 2
    
    def update(self):
        pass

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
        self.scroll = 0  # Initialize scroll outside the update method

        # -- Enemy Setup --
        # Grid
        self.invader_rows = 5
        self.invader_columns = 11

        # Calculate and scale spacing based on screen dimensions
        self.horizontal_spacing = self.screen.get_width() // 30  # Adjusted for 1920 width
        self.vertical_spacing = self.screen.get_height() // 17  # Adjusted for 1080 height

        # Calculate and scale invader dimensions based on screen dimensions
        self.invader_width = self.screen.get_width() // 25  # Adjusted for 1920 width
        self.invader_height = self.screen.get_height() // 17  # Adjusted for 1080 height

        # Start position of the grid
        self.invader_start_x = 200
        self.invader_start_y = 50

        # Load invader image and scale it
        self.invader_image = pygame.image.load('./assets/BI_invader.png').convert_alpha()
        self.invader_image = pygame.transform.scale(self.invader_image, (self.invader_width, self.invader_height))

        self.invaders = pygame.sprite.Group()
        for row in range(self.invader_rows):
            for col in range(self.invader_columns):
                x = self.invader_start_x + col * (self.invader_width + self.horizontal_spacing)
                y = self.invader_start_y + row * (self.invader_height + self.vertical_spacing)
                invader = Invader(x, y, self.invader_image)
                self.invaders.add(invader)
    
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

        move_left = keys[pygame.K_a] or keys[pygame.K_LEFT]
        move_right = keys[pygame.K_d] or keys[pygame.K_RIGHT]

        counter_strafe_multiplier = 2

        if move_left:
            if self.spaceship_velocity > 0:
                self.spaceship_velocity -= self.spaceship_acceleration * counter_strafe_multiplier
            else:
                self.spaceship_velocity -= self.spaceship_acceleration
        elif move_right:
            if self.spaceship_velocity < 0:
                self.spaceship_velocity += self.spaceship_acceleration * counter_strafe_multiplier
            else:
                self.spaceship_velocity += self.spaceship_acceleration
        else:
            # No input = normal friction
            if self.spaceship_velocity > 0:
                self.spaceship_velocity -= self.spaceship_friction
                self.spaceship_velocity = max(self.spaceship_velocity, 0)
            elif self.spaceship_velocity < 0:
                self.spaceship_velocity += self.spaceship_friction
                self.spaceship_velocity = min(self.spaceship_velocity, 0)

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
        
        #self.screen.blit(self.background, (0, -1 * self.background_height + self.scroll))
        self.screen.blit(self.background, (0, 0 * self.background_height + self.scroll))

        #self.scroll = (self.scroll + 5) % self.background_height


        # Update and draw invaders
        self.invaders.update()
        self.invaders.draw(self.screen)

        # rotate spaceship logic
        rotated_spaceship = pygame.transform.rotozoom(self.spaceship, self.spaceship_angle, 1)
        rotated_rect = rotated_spaceship.get_rect(center=(self.spaceship_x + 50, self.spaceship_y + 50))

        # draw spaceship
        self.screen.blit(rotated_spaceship, rotated_rect.topleft)

        pygame.display.flip()