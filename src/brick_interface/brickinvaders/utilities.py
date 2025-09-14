from brick_interface.brickinvaders.explosion import Explosion
import pygame
import math
from .constants import *
from .invader import Invader

def planet_animation(self, spritesheet, spritesheet_index):
    frame_x = (spritesheet_index % PLANET_SPRITESHEET_COLUMNS) * PLANET_FRAME_WIDTH
    frame_y = (spritesheet_index // PLANET_SPRITESHEET_COLUMNS) * PLANET_FRAME_HEIGHT
    frame_surface = pygame.Surface((PLANET_FRAME_WIDTH, PLANET_FRAME_HEIGHT), pygame.SRCALPHA)
    frame_surface.blit(spritesheet, (0, 0), (frame_x, frame_y, PLANET_FRAME_WIDTH, PLANET_FRAME_HEIGHT))

    # Scale the frame to the desired size
    
    scaled_frame = pygame.transform.scale(frame_surface, (1920, 1920))
    return scaled_frame

def spaceship_animation(self, spritesheet, spritesheet_index):
    frame_x = (spritesheet_index % SPACESHIP_SPRITESHEET_COLUMNS) * SPACESHIP_FRAME_WIDTH
    frame_y = (spritesheet_index // SPACESHIP_SPRITESHEET_COLUMNS) * SPACESHIP_FRAME_HEIGHT
    frame_surface = pygame.Surface((SPACESHIP_FRAME_WIDTH, SPACESHIP_FRAME_HEIGHT), pygame.SRCALPHA)
    frame_surface.blit(spritesheet, (0, 0), (frame_x, frame_y, SPACESHIP_FRAME_WIDTH, SPACESHIP_FRAME_HEIGHT))

    # Scale the frame to the desired size

    scaled_frame = pygame.transform.scale(frame_surface, (96, 96))
    return scaled_frame

def invader_animation(self, spritesheet, spritesheet_index):
    frame_x = (spritesheet_index % INVADER_SPRITESHEET_COLUMNS) * INVADER_FRAME_WIDTH
    frame_y = (spritesheet_index // INVADER_SPRITESHEET_COLUMNS) * INVADER_FRAME_HEIGHT
    frame_surface = pygame.Surface((INVADER_FRAME_WIDTH, INVADER_FRAME_HEIGHT), pygame.SRCALPHA)
    frame_surface.blit(spritesheet, (0, 0), (frame_x, frame_y, INVADER_FRAME_WIDTH, INVADER_FRAME_HEIGHT))

    # Scale the frame to the desired size

    scaled_frame = pygame.transform.scale(frame_surface, (INVADER_WIDTH, INVADER_HEIGHT))
    return scaled_frame

def explosion_animation(self, spritesheet, x, y):
    for i in range(EXPLOSION_TOTAL_FRAMES):
        frame_x = (i % EXPLOSION_SPRITESHEET_COLUMNS) * EXPLOSION_FRAME_WIDTH
        frame_y = (i // EXPLOSION_SPRITESHEET_COLUMNS) * EXPLOSION_FRAME_HEIGHT
        frame_surface = pygame.Surface((EXPLOSION_FRAME_WIDTH, EXPLOSION_FRAME_HEIGHT), pygame.SRCALPHA)
        frame_surface.blit(spritesheet, (0, 0), (frame_x, frame_y, EXPLOSION_FRAME_WIDTH, EXPLOSION_FRAME_HEIGHT))
        self.screen.blit(pygame.transform.scale(frame_surface, (EXPLOSION_WIDTH, EXPLOSION_HEIGHT)), (x, y))
        pygame.display.flip()

def setup_level(self, level_data):
    self.invaders.empty()
    rows = level_data["rows"]
    columns = level_data["columns"]
    speed = level_data["invader_speed"]
    pattern = level_data.get("pattern", "default")
    # You can expand pattern logic here if needed

    horizontal_spacing  = (SCREEN_WIDTH - columns * (INVADER_WIDTH * 2)) // 2 + INVADER_WIDTH
    vertical_spacing = INVADER_HEIGHT
    if pattern == "default":
        for row in range(rows):
            for col in range(columns):
                x = horizontal_spacing + col * (INVADER_WIDTH * 2)
                y = vertical_spacing + row * (INVADER_HEIGHT * 2)
                invader = Invader(x, y, self.invaders_spritesheets[row % INVADER_SPRITESHEETS], speed, row % 2)
                self.invaders.add(invader)
    elif pattern == "zigzag":
        for row in range(rows):
            for col in range(columns):
                x = horizontal_spacing + col * (INVADER_WIDTH * 2) + (row % 2) * INVADER_WIDTH
                y = vertical_spacing + row * (INVADER_HEIGHT * 2)
                invader = Invader(x, y, self.invaders_spritesheets[row % INVADER_SPRITESHEETS], speed, row % 2)
                self.invaders.add(invader)
    elif pattern == "dense":
        for row in range(rows):
            for col in range(columns):
                x = horizontal_spacing + col * (INVADER_WIDTH * 1.5)
                y = vertical_spacing + row * (INVADER_HEIGHT * 1.5)
                invader = Invader(x, y, self.invaders_spritesheets[row % INVADER_SPRITESHEETS], speed, row % 2)
                self.invaders.add(invader)
    elif pattern == "semicircle":
        for row in range(rows):
            for col in range(columns):
                if col == 0 or col == columns - 1 or row == 0:
                    x = horizontal_spacing + col * (INVADER_WIDTH * 2)
                    y = vertical_spacing + row * (INVADER_HEIGHT * 2)
                    invader = Invader(x, y, self.invaders_spritesheets[row % INVADER_SPRITESHEETS], speed, row % 2)
                    self.invaders.add(invader)

def check_bullet_invader_collisions(self):
    for bullet in self.bullets:
        if pygame.sprite.spritecollideany(bullet, self.invaders):
            collided_invader = pygame.sprite.spritecollideany(bullet, self.invaders)
            bullet.kill()
            collided_invader.kill()
            explosion = Explosion(collided_invader.rect.x, collided_invader.rect.y, self.explosion_spritesheet)
            self.explosions.add(explosion)

def check_invader_spaceship_collisions(self):
    for invader in self.invaders:
        if invader.rect.colliderect(pygame.Rect(self.spaceship.x, self.spaceship.y, 100, 100)):
            explosion_animation(self, self.explosion_spritesheet, self.spaceship.x, self.spaceship.y)
            self.running = False
            print("Game Over! An invader hit your spaceship.")
            break
            
def animation(self):
    animation_duration = 600  # total frames
    clock = pygame.time.Clock()
    
    center_x = SCREEN_WIDTH // 2 - 50
    start_x = self.spaceship.x
    start_angle = self.spaceship.angle
    target_angle = 0
    move_frames = 120
    
    def ease_in_out_quad(t):
        return 2*t*t if t < 0.5 else -1 + (4 - 2*t)*t
    
    for frame in range(move_frames):
        t = frame / move_frames
        eased_t = ease_in_out_quad(t)
        self.spaceship.x = int(start_x + (center_x - start_x) * eased_t)
        self.spaceship.angle = start_angle + (target_angle - start_angle) * eased_t

        self.screen.blit(self.background, (0, 0 * self.background.get_height()))

        # draw planet
        scaled_surface = planet_animation(self, self.planets[self.level_index], pygame.time.get_ticks() // PLANET_ANIMATION_SLOWDOWN % PLANET_TOTAL_FRAMES)  # Loop through frames
        self.screen.blit(scaled_surface, (self.planet_offset_x, self.planet_offset_y))

        self.spaceship.rect = spaceship_animation(self, self.spaceship.spritesheet, pygame.time.get_ticks() // SPACESHIP_ANIMATION_SLOWDOWN % SPACESHIP_TOTAL_FRAMES)
        rotated_spaceship = pygame.transform.rotozoom(self.spaceship.rect, self.spaceship.angle, 1)
        rotated_rect = rotated_spaceship.get_rect(center=(self.spaceship.x + 50, self.spaceship.y + 50))
        self.screen.blit(rotated_spaceship, rotated_rect.topleft)

        pygame.display.flip()
        clock.tick(60)

    self.spaceship.angle = target_angle
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
            self.screen.blit(self.background, (0, i * self.background.get_height() + background_scroll))

        # draw planet
        scaled_surface = planet_animation(self, self.planets[self.level_index], pygame.time.get_ticks() // PLANET_ANIMATION_SLOWDOWN % PLANET_TOTAL_FRAMES)  # Loop through frames
        self.screen.blit(scaled_surface, (self.planet_offset_x, int(self.planet_offset_y + planet_scroll / 2.0)))

        self.spaceship.rect = spaceship_animation(self, self.spaceship.spritesheet, pygame.time.get_ticks() // SPACESHIP_ANIMATION_SLOWDOWN % SPACESHIP_TOTAL_FRAMES)
        rotated_spaceship = pygame.transform.rotozoom(self.spaceship.rect, self.spaceship.angle, 1)
        rotated_rect = rotated_spaceship.get_rect(center=(self.spaceship.x + 50, self.spaceship.y + 50))
        self.screen.blit(rotated_spaceship, rotated_rect.topleft)

        # --- normal scrolling update for the main phases ---
        background_scroll += scroll

        # first third: accelerate and move planet down
        if frame < animation_duration // 3:
            scroll *= 1.015
            planet_scroll += 7
            a = True

        # middle third: heavy background push and set planet image
        elif frame >= animation_duration // 3 and frame <= 2 * animation_duration // 3:
            if a == True:
                self.level_index += 1
                a = False
                # Adjust offsets for galaxy, star, and blackhole spritesheet
                if self.level_index == 7:
                    self.planet_offset_x = GALAXY_OFFSET_X
                    self.planet_offset_y = GALAXY_OFFSET_Y
                if self.level_index == 8:
                    self.planet_offset_x = STAR_OFFSET_X
                    self.planet_offset_y = STAR_OFFSET_Y
                if self.level_index == 9:
                    self.planet_offset_x /= BLACKHOLE_OFFSET_X
                    self.planet_offset_y /= BLACKHOLE_OFFSET_Y
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
                target_background_scroll = round(start_background_scroll / self.background.get_height()) * self.background.get_height()

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