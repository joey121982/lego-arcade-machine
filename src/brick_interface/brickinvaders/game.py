import pygame
import math
from .constants import (
    SPACESHIP_SPEED, SPACESHIP_ACCELERATION, SPACESHIP_FRICTION, SPACESHIP_VELOCITY_LIMIT,
    SPACESHIP_COUNTER_STRAFE_MULTIPLIER, SPACESHIP_ANGLE_INCREMENT,
    BULLET_SPEED, BULLET_WIDTH, BULLET_HEIGHT, BULLET_COLOR,
    INVADER_ROWS, INVADER_COLUMNS, INVADER_START_X, INVADER_START_Y, INVADER_SPEED,
    COLOR_RED, COLOR_YELLOW, COLOR_WHITE, LEVELS
)

class Bullet (pygame.sprite.Sprite):
    def __init__(self, x, y, image, speed, angle, color):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.angle = angle
        self.color = color

        rad_angle = math.radians(self.angle)
        self.dx = self.speed * math.cos(rad_angle)
        self.dy = self.speed * math.sin(rad_angle)

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Check if the bullet is off-screen
        if self.rect.x < 0 or self.rect.x > pygame.display.get_surface().get_width() or \
              self.rect.y < 0 or self.rect.y > pygame.display.get_surface().get_height():
                self.kill()

class Invader(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
    
    def update(self):
        pass

class Brickinvaders:
    def setup_level(self, level_data):
        self.invaders.empty()
        rows = level_data["rows"]
        columns = level_data["columns"]
        speed = level_data["invader_speed"]
        pattern = level_data.get("pattern", "default")
        # You can expand pattern logic here if needed
        for row in range(rows):
            for col in range(columns):
                x = INVADER_START_X + col * (self.invader_width + self.horizontal_spacing)
                y = INVADER_START_Y + row * (self.invader_height + self.vertical_spacing)
                invader = Invader(x, y, self.invader_image)
                invader.speed = speed
                self.invaders.add(invader)
    name = "Brick Invaders"
    running = True
    
    def __init__(self, screen, glb):
        self.running = True
        self.screen = screen
        self.glb = glb

        # -- Spaceship Setup --
        # Initialize spaceship
        self.spaceship = pygame.Surface((100, 100), pygame.SRCALPHA)
        pygame.draw.polygon(self.spaceship, COLOR_RED, [(50, 0), (100, 100), (0, 100)])

        self.spaceship_x = self.screen.get_width() // 2 - 50
        self.spaceship_y = self.screen.get_height() - 250

        # Spaceship movement variables
        self.spaceship_velocity = 0

        # Spaceship angle
        self.spaceship_angle = 0
        self.spaceship_angle_sign = 0

        # -- Background Setup --
        # Background things
        self.background = pygame.image.load('./assets/BI_background.png').convert()
        self.background = pygame.transform.scale(self.background, (self.glb.WINWIDTH, self.glb.WINHEIGHT))
        self.background_width = self.background.get_width()
        self.background_height = self.background.get_height()
        self.scroll = 0  # Initialize scroll outside the update method

        # -- Enemy Setup --
        # Level Index
        self.level_index = 0

        # Calculate and scale spacing based on screen dimensions
        self.horizontal_spacing = self.screen.get_width() // 30  # Adjusted for 1920 width
        self.vertical_spacing = self.screen.get_height() // 17  # Adjusted for 1080 height

        # Calculate and scale invader dimensions based on screen dimensions
        self.invader_width = self.screen.get_width() // 25  # Adjusted for 1920 width
        self.invader_height = self.screen.get_height() // 17  # Adjusted for 1080 height

        # Load invader image and scale it
        self.invader_image = pygame.image.load('./assets/BI_invader.png').convert_alpha()
        self.invader_image = pygame.transform.scale(self.invader_image, (self.invader_width, self.invader_height))

        self.invaders = pygame.sprite.Group()
        self.setup_level(LEVELS[self.level_index])

        # -- Bullet Setup --
        # Initialize bullet
        self.bullet_speed = BULLET_SPEED
        self.bullet_image = pygame.image.load('./assets/BI_bullet.png').convert_alpha()
        self.bullet_image = pygame.transform.scale(self.bullet_image, (BULLET_WIDTH, BULLET_HEIGHT))

        self.bullets = pygame.sprite.Group()
    
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Shoot bullet
                bullet_x = self.spaceship_x + 50  # Center of the spaceship
                bullet_y = self.spaceship_y  # Center of the spaceship
                bullet_angle = -self.spaceship_angle + 270 # Adjust angle to point downwards
                bullet = Bullet(bullet_x, bullet_y, self.bullet_image, speed=10, angle=bullet_angle, color=(255, 255, 0))
                self.bullets.add(bullet)

            if event.key == pygame.K_ESCAPE:
                self.running = False
                self.glb.return_to_menu = True  # Signal to return to menu

    def update_spaceship_position(self):
        keys = pygame.key.get_pressed()

        move_left = keys[pygame.K_a] or keys[pygame.K_LEFT]
        move_right = keys[pygame.K_d] or keys[pygame.K_RIGHT]

    
        if move_left:
            if self.spaceship_velocity > 0:
                self.spaceship_velocity -= SPACESHIP_ACCELERATION * SPACESHIP_COUNTER_STRAFE_MULTIPLIER 
            else:
                self.spaceship_velocity -= SPACESHIP_ACCELERATION   
        elif move_right:
            if self.spaceship_velocity < 0:
                self.spaceship_velocity += SPACESHIP_ACCELERATION * SPACESHIP_COUNTER_STRAFE_MULTIPLIER
            else:
                self.spaceship_velocity += SPACESHIP_ACCELERATION
        else:
            # No input = normal friction
            if self.spaceship_velocity > 0:
                self.spaceship_velocity -= SPACESHIP_FRICTION
                self.spaceship_velocity = max(self.spaceship_velocity, 0)
            elif self.spaceship_velocity < 0:
                self.spaceship_velocity += SPACESHIP_FRICTION
                self.spaceship_velocity = min(self.spaceship_velocity, 0)

        self.spaceship_velocity = max(-SPACESHIP_VELOCITY_LIMIT, min(self.spaceship_velocity, SPACESHIP_VELOCITY_LIMIT))
        self.spaceship_x += self.spaceship_velocity
        if self.spaceship_x < 50:
            self.spaceship_x = 50
            self.spaceship_velocity = 0
        elif self.spaceship_x > self.screen.get_width() - 150:
            self.spaceship_x = self.screen.get_width() - 150
            self.spaceship_velocity = 0

        self.spaceship_angle = (self.spaceship_velocity // 5) * SPACESHIP_ANGLE_INCREMENT * -1
  
    def update(self):
        # move spaceship
        self.update_spaceship_position()

        # background
        self.screen.blit(self.background, (0, 0 * self.background_height + self.scroll))

        # Check for level completion
        if len(self.invaders) == 0:
            self.level_index += 1
            if self.level_index < len(LEVELS):
                self.setup_level(LEVELS[self.level_index])
            else:
                # Game completed, show win screen or restart
                print("You win!")
                self.running = False
                return

        # Update and draw invaders
        self.invaders.update()
        self.invaders.draw(self.screen)

        self.bullets.update()
        self.bullets.draw(self.screen)

        # rotate spaceship logic
        rotated_spaceship = pygame.transform.rotozoom(self.spaceship, self.spaceship_angle, 1)
        rotated_rect = rotated_spaceship.get_rect(center=(self.spaceship_x + 50, self.spaceship_y + 50))

        # draw spaceship
        self.screen.blit(rotated_spaceship, rotated_rect.topleft)
        pygame.display.flip()