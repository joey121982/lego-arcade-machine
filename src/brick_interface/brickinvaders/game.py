import pygame
import math
from .utilities import *
from .constants import *
from .bullet import Bullet
from .invader import Invader
from .spaceship import Spaceship

class Brickinvaders:
    name = "Brick Invaders"
    running = True

    def __init__(self, screen, glb):
        self.running = True
        self.screen = screen
        self.glb = glb
        
        # Load Images
        self.bullet_image, self.invader_image, self.planets = load_images()
        self.planet_offset_x = PLANET_OFFSET_X
        self.planet_offset_y = PLANET_OFFSET_Y

        # -- Spaceship Setup --
        # Initialize spaceship
        spaceship_x = SCREEN_WIDTH // 2 - 50
        spaceship_y = SCREEN_HEIGHT - 250
        self.spaceship = Spaceship(spaceship_x, spaceship_y, None, SPACESHIP_SPEED, SPACESHIP_ACCELERATION, SPACESHIP_FRICTION, SPACESHIP_VELOCITY_LIMIT, SPACESHIP_COUNTER_STRAFE_MULTIPLIER, SPACESHIP_ANGLE_INCREMENT)
        pygame.draw.polygon(self.spaceship.rect, (255, 0, 0), [(50, 0), (100, 100), (0, 100)])

        # -- Background Setup --
        self.background = pygame.transform.scale(pygame.image.load('./assets/brickinvaders/images/BI_background.png').convert(), (self.glb.WINWIDTH, self.glb.WINHEIGHT))
        
        # -- Sprite Groups --
        self.invaders = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        
        # -- Level Setup --
        self.level_index = 0
        setup_level(self, LEVELS[self.level_index])
        
        # -- Planet --
        self.current_planet = self.planets[self.level_index]
        
        # Invader movement
        self.global_direction = 1

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and len(self.bullets) < 3:
                # Shoot bullet
                bullet_x = self.spaceship.x + 50  # Center of the spaceship
                bullet_y = self.spaceship.y  # Center of the spaceship
                bullet_angle = -self.spaceship.angle + 270 # Adjust angle to point downwards
                bullet = Bullet(bullet_x, bullet_y, self.bullet_image, speed=BULLET_SPEED, angle=bullet_angle, color=(255, 255, 0))
                self.bullets.add(bullet)

            if event.key == pygame.K_ESCAPE:
                self.running = False
                self.glb.return_to_menu = True  # Signal to return to menu
  
    def update(self):
        self.spaceship.update()
        

        # background
        self.screen.blit(self.background, (0, 0 * self.background.get_height()))
        scaled_planet = planet_animation(self, self.planets[self.level_index], pygame.time.get_ticks() // ANIMATION_SLOWDOWN % PLANET_TOTAL_FRAMES)
        self.screen.blit(scaled_planet, (self.planet_offset_x, self.planet_offset_y))

        # Update and draw invaders
        for invader in self.invaders:
            if invader.actual_x < invader.image.get_width() // 2 or invader.actual_x > 1920 - invader.image.get_width() * 2:
                self.global_direction += 1
                for invader in self.invaders:
                    invader.rect.y += self.global_direction * invader.image.get_height() // 2
                break
        self.invaders.update(self.global_direction)
        self.invaders.draw(self.screen)

        self.bullets.update()
        self.bullets.draw(self.screen)

        # Collisions
        check_bullet_invader_collisions(self)
        check_invader_spaceship_collisions(self)

        if len(self.invaders) == 0:
            if self.level_index >= len(LEVELS):
                print("Congratulations! You've completed all levels!")
                self.running = False
            else:
                animation(self)
                setup_level(self, LEVELS[self.level_index])
                self.global_direction = 1

        self.spaceship.draw(self.screen)
        pygame.display.flip()