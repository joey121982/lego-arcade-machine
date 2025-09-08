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
        self.bullet_image, self.invader_image, self.planets = load_images()

        # -- Spaceship Setup --
        # Initialize spaceship
        spaceship_x = SCREEN_WIDTH // 2 - 50
        spaceship_y = SCREEN_HEIGHT - 250
        self.spaceship = Spaceship(spaceship_x, spaceship_y, None, SPACESHIP_SPEED, SPACESHIP_ACCELERATION, SPACESHIP_FRICTION, SPACESHIP_VELOCITY_LIMIT, SPACESHIP_COUNTER_STRAFE_MULTIPLIER, SPACESHIP_ANGLE_INCREMENT)
        pygame.draw.polygon(self.spaceship.rect, (255, 0, 0), [(50, 0), (100, 100), (0, 100)])

        # -- Background Setup --
        self.background = pygame.transform.scale(pygame.image.load('./assets/brickinvaders/images/BI_background.png').convert(), (self.glb.WINWIDTH, self.glb.WINHEIGHT))
        self.background_width = self.background.get_width()
        self.background_height = self.background.get_height()

        # -- Planet Images --
        self.current_planet = self.planets[0]
        
        # -- Sprite Groups --
        self.invaders = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        
        self.level_index = 0
        setup_level(self, LEVELS[self.level_index])
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
  
    def animation(self):
        animation_duration = 600  # total frames
        clock = pygame.time.Clock()
        
        # If you really want to understand what i did here, its called linear interpolation and easing functions
        # The main animation loop is divided into phases: acceleration, constant speed, deceleration,
        # and a final easing phase to smoothly settle the background and planet into their final positions.
        # Easing functions are used to create a more natural and visually appealing transition, especially at
        # the start and end of movements. The ease_out_cubic function provides a smooth deceleration effect.
        # The lerp function is a simple linear interpolation utility that helps in calculating intermediate
        # values between a start and end point based on a parameter t (0 to 1).
        
        # I'll give you my Numerical Methods Manual that i studied at the Faculty of Automatic Control that inspired this solution:
        # https://faculty.ksu.edu.sa/sites/default/files/numerical_analysis_9th.pdf

        background_scroll = 0.0
        planet_scroll = 0.0
        scroll = 1.0

        # final easing configuration
        final_total = 50                      # total frames used for the final easing
        final_soft = 49                       # soft ease duration
        final_snap = final_total - final_soft  # small quick snap toward the end
        final_started = False
        ease_start_frame = None
        start_planet_scroll = 0.0
        start_background_scroll = 0.0
        target_background_scroll = 0.0

        def lerp(a, b, t):
            return a + (b - a) * t

        def ease_out_cubic(t):
            return 1 - (1 - t) ** 3
        

        for frame in range(animation_duration):
            for i in range(0, -9, -1):
                self.screen.blit(self.background, (0, i * self.background_height + background_scroll))

            # draw planet
            self.screen.blit(self.current_planet,
                            (PLANET_OFFSET_X, int(PLANET_OFFSET_Y + planet_scroll / 2.0)))

            # rotate spaceship logic (unchanged, but keep int rect for blit)
            rotated_spaceship = pygame.transform.rotozoom(self.spaceship.rect, self.spaceship.angle, 1)
            rotated_rect = rotated_spaceship.get_rect(center=(self.spaceship.x + 50, self.spaceship.y + 50))
            self.screen.blit(rotated_spaceship, rotated_rect.topleft)

            # --- normal scrolling update for the main phases ---
            background_scroll += scroll

            # first third: accelerate and move planet up
            if frame < animation_duration // 3:
                scroll *= 1.015
                planet_scroll += 6.0

            # middle third: heavy background push and set planet image
            elif frame >= animation_duration // 3 and frame <= 2 * animation_duration // 3:
                background_scroll += 9.0
                self.current_planet = self.planets[self.level_index]

            # deceleration phase before final easing
            elif frame > 2 * animation_duration // 3 and frame < animation_duration - final_total:
                scroll *= 0.99
                planet_scroll -= 7.5

            
            elif frame >= animation_duration - final_total:
                if not final_started:
                    # capture starting values only once at start of final easing
                    final_started = True
                    ease_start_frame = frame
                    start_planet_scroll = float(planet_scroll)
                    start_background_scroll = float(background_scroll)
                    # choose target as nearest multiple of background_height
                    target_background_scroll = round(start_background_scroll / self.background_height) * self.background_height

                # how far into the soft easing we are (0..1)
                eased_frame = frame - ease_start_frame

                # soft easing portion
                if eased_frame < final_soft:
                    t = eased_frame / float(final_soft)        # 0..1
                    e = ease_out_cubic(t)                     # smooth ease-out
                    # lerp both planet and background toward their targets
                    planet_scroll = lerp(start_planet_scroll, 0.0, e)
                    background_scroll = lerp(start_background_scroll, target_background_scroll, e)

                # quick snap portion near the end to finish nicely
                else:
                    # map snap portion to 0..1
                    t_snap = (eased_frame - final_soft) / max(1, final_snap)
                    # use a faster ease (quadratic)
                    e2 = 1 - (1 - t_snap) ** 2
                    planet_scroll = lerp(planet_scroll, 0.0, e2)
                    background_scroll = lerp(background_scroll, target_background_scroll, e2)

            # ensure exact snap at the very last frame
            if frame == animation_duration - 1:
                planet_scroll = 0.0
                # force to exact target multiple of background_height
                # background_scroll = round(background_scroll / self.background_height) * self.background_height
                background_scroll = 0

            # debugging output
            # if frame % 10 == 0:  # print every 10 frames (optional)
            #     print(frame, round(background_scroll, 2), round(planet_scroll, 2))

            pygame.display.flip()
            clock.tick(60)


    def update(self):
        
        # move spaceship
        self.spaceship.update()

        # background
        self.screen.blit(self.background, (0, 0 * self.background_height))
        self.screen.blit(self.current_planet, PLANET_OFFSET)

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
            self.level_index += 1
            if self.level_index >= len(LEVELS):
                print("Congratulations! You've completed all levels!")
                self.running = False
            else:
                self.animation()
                setup_level(self, LEVELS[self.level_index])
                self.global_direction = 1

        # rotate spaceship logic
        rotated_spaceship = pygame.transform.rotozoom(self.spaceship.rect, self.spaceship.angle, 1)
        rotated_rect = rotated_spaceship.get_rect(center=(self.spaceship.x + 50, self.spaceship.y + 50))

        # draw spaceship
        self.screen.blit(rotated_spaceship, rotated_rect.topleft)
        pygame.display.flip()