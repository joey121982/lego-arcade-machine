import pygame
import math
from .constants import *

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
    def __init__(self, x, y, image, speed):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.actual_x = x
        self.speed = speed

    def update(self, global_direction):
        if global_direction % 2 == 1:
            self.actual_x += self.speed * 1 # This represents the actual live x position of the invader
            if self.actual_x - self.rect.x > self.rect.width:
                self.rect.x = self.actual_x # We move the rect only when the difference is significant to add the clasic effect of the original invader game
        else:
            self.actual_x += self.speed * -1
            if self.rect.x - self.actual_x > self.rect.width:
                self.rect.x = self.actual_x
        

class Brickinvaders:
    name = "Brick Invaders"
    running = True
    
    def setup_level(self, level_data):
        self.invaders.empty()
        rows = level_data["rows"]
        columns = level_data["columns"]
        speed = level_data["invader_speed"]
        pattern = level_data.get("pattern", "default")
        # You can expand pattern logic here if needed
        
        horizontal_spacing  = (SCREEN_WIDTH - columns * (self.invader_width * 2)) // 2 + self.invader_width
        vertical_spacing = self.invader_height
        if pattern == "default":
            for row in range(rows):
                for col in range(columns):
                    x = horizontal_spacing + col * (self.invader_width * 2)
                    y = vertical_spacing + row * (self.invader_height * 2)
                    invader = Invader(x, y, self.invader_image, speed)
                    self.invaders.add(invader)
        elif pattern == "zigzag":
            for row in range(rows):
                for col in range(columns):
                    x = horizontal_spacing + col * (self.invader_width * 2) + (row % 2) * self.invader_width
                    y = vertical_spacing + row * (self.invader_height * 2)
                    invader = Invader(x, y, self.invader_image, speed)
                    self.invaders.add(invader)
        elif pattern == "dense":
            for row in range(rows):
                for col in range(columns):
                    x = horizontal_spacing + col * (self.invader_width * 1.5)
                    y = vertical_spacing + row * (self.invader_height * 1.5)
                    invader = Invader(x, y, self.invader_image, speed)
                    self.invaders.add(invader)
        elif pattern == "semicircle":
            for row in range(rows):
                for col in range(columns):
                    if col == 0 or col == columns - 1 or row == 0:
                        x = horizontal_spacing + col * (self.invader_width * 2)
                        y = vertical_spacing + row * (self.invader_height * 2)
                        invader = Invader(x, y, self.invader_image, speed)
                        self.invaders.add(invader)

    def __init__(self, screen, glb):
        self.running = True
        self.screen = screen
        self.glb = glb

        # -- Spaceship Setup --
        # Initialize spaceship
        self.spaceship = pygame.Surface((100, 100), pygame.SRCALPHA)
        pygame.draw.polygon(self.spaceship, (255, 0, 0), [(50, 0), (100, 100), (0, 100)])

        self.spaceship_x = self.screen.get_width() // 2 - 50
        self.spaceship_y = self.screen.get_height() - 250

        # Spaceship movement variables
        self.spaceship_velocity = 0

        # Spaceship angle
        self.spaceship_angle = 0
        self.spaceship_angle_sign = 0

        # -- Background Setup --
        # Background things
        self.background = pygame.image.load('./assets/images/BI_background.png').convert()
        self.background = pygame.transform.scale(self.background, (self.glb.WINWIDTH, self.glb.WINHEIGHT))
        self.background_width = self.background.get_width()
        self.background_height = self.background.get_height()
        
        # Load multiple planet images into an array
        self.planets = [
            pygame.image.load('./assets/images/BI_planet1.png').convert_alpha(),
            pygame.image.load('./assets/images/BI_planet2.png').convert_alpha(),
            pygame.image.load('./assets/images/BI_planet3.png').convert_alpha()
        ]

        self.current_planet = self.planets[0]
        #self.planet1 = pygame.transform.scale(self.planet1, (self.glb.WINWIDTH, self.glb.WINHEIGHT))

        # -- Enemy Setup --
        # Grid

        # Calculate and scale spacing based on screen dimensions

        # Calculate and scale invader dimensions based on screen dimensions
        self.invader_width = self.screen.get_width() // 25  # Adjusted for 1920 width
        self.invader_height = self.screen.get_height() // 17  # Adjusted for 1080 height

        # Start position of the grid

        # Load invader image and scale it
        self.invader_image = pygame.image.load('./assets/images/BI_invader.png').convert_alpha()
        self.invader_image = pygame.transform.scale(self.invader_image, (self.invader_width, self.invader_height))

        self.invaders = pygame.sprite.Group()
        self.level_index = 0
        self.setup_level(LEVELS[self.level_index])
        self.invader_direction = 1

        # -- Bullet Setup --
        # Initialize bullet

        self.bullet_image = pygame.image.load('./assets/images/BI_bullet.png').convert_alpha()
        self.bullet_image = pygame.transform.scale(self.bullet_image, (BULLET_WIDTH, BULLET_HEIGHT))

        self.bullets = pygame.sprite.Group()
    
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and len(self.bullets) < 3:
                # Shoot bullet
                bullet_x = self.spaceship_x + 50  # Center of the spaceship
                bullet_y = self.spaceship_y  # Center of the spaceship
                bullet_angle = -self.spaceship_angle + 270 # Adjust angle to point downwards
                bullet = Bullet(bullet_x, bullet_y, self.bullet_image, speed=BULLET_SPEED, angle=bullet_angle, color=(255, 255, 0))
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
        
    def check_bullet_invader_collisions(self):
        for bullet in self.bullets:
            if pygame.sprite.spritecollideany(bullet, self.invaders):
                collided_invader = pygame.sprite.spritecollideany(bullet, self.invaders)
                bullet.kill()
                collided_invader.kill()
                # Play explosion sound or show explosion animation
                # explosion_sound = pygame.mixer.Sound('./assets/images/explosion.wav')
                # explosion_sound.play()
    
    def check_invader_spaceship_collisions(self):
        for invader in self.invaders:
            if invader.rect.colliderect(pygame.Rect(self.spaceship_x, self.spaceship_y, 100, 100)):
                # Handle collision (e.g., end game or reduce life)
                self.running = False
                print("Game Over! An invader hit your spaceship.")
                break
            
            
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
            # If it works, it works
            # IMPROVE THE LOGIC HERE LATER
            self.screen.blit(self.background, (0, background_scroll))
            self.screen.blit(self.background, (0, -1 * self.background_height + background_scroll))
            self.screen.blit(self.background, (0, -2 * self.background_height + background_scroll))
            self.screen.blit(self.background, (0, -3 * self.background_height + background_scroll))
            self.screen.blit(self.background, (0, -4 * self.background_height + background_scroll))
            self.screen.blit(self.background, (0, -5 * self.background_height + background_scroll))
            self.screen.blit(self.background, (0, -6 * self.background_height + background_scroll))
            self.screen.blit(self.background, (0, -7 * self.background_height + background_scroll))
            self.screen.blit(self.background, (0, -8 * self.background_height + background_scroll))
            self.screen.blit(self.background, (0, -9 * self.background_height + background_scroll))

            # draw planet
            self.screen.blit(self.current_planet,
                            (PLANET_OFFSET_X, int(PLANET_OFFSET_Y + planet_scroll / 2.0)))

            # rotate spaceship logic (unchanged, but keep int rect for blit)
            rotated_spaceship = pygame.transform.rotozoom(self.spaceship, self.spaceship_angle, 1)
            rotated_rect = rotated_spaceship.get_rect(center=(self.spaceship_x + 50, self.spaceship_y + 50))
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
        self.update_spaceship_position()

        # background
        
        self.screen.blit(self.background, (0, 0 * self.background_height))
        self.screen.blit(self.current_planet, PLANET_OFFSET)

        # Update and draw invaders
        for invader in self.invaders:
            if invader.actual_x < invader.image.get_width() // 2 or invader.actual_x > 1920 - invader.image.get_width() * 2:
                self.invader_direction += 1
                for invader in self.invaders:
                    invader.rect.y += self.invader_direction * invader.image.get_height() // 2
                break
        self.invaders.update(self.invader_direction)
        self.invaders.draw(self.screen)

        self.bullets.update()
        self.bullets.draw(self.screen)

        # Collisions
        self.check_bullet_invader_collisions()
        self.check_invader_spaceship_collisions()
        
        if len(self.invaders) == 0:
            self.level_index += 1
            if self.level_index >= len(LEVELS):
                print("Congratulations! You've completed all levels!")
                self.running = False
            else:
                self.animation()
                self.setup_level(LEVELS[self.level_index])
                self.invader_direction = 1

        # rotate spaceship logic
        rotated_spaceship = pygame.transform.rotozoom(self.spaceship, self.spaceship_angle, 1)
        rotated_rect = rotated_spaceship.get_rect(center=(self.spaceship_x + 50, self.spaceship_y + 50))

        # draw spaceship
        self.screen.blit(rotated_spaceship, rotated_rect.topleft)
        pygame.display.flip()