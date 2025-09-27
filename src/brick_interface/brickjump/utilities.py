import pygame
import random
from .constants import *

def check_player_below_screen(self):
    if self.player.rect.top >= SCREEN_HEIGHT:
        self.running = False
        self.glb.return_to_menu = True  # signal to return to menu
        print("check_player_below_screen function triggered")
    

def advance(self):
    # the player made a correct jump, advance the game (score, scroll)
    if self.player.on_ground and self.player.prev_y != self.player.rect.y:
        for sprite in self.level.platforms:
            sprite.rect.y += SCROLL
        for sprite in self.level.pillars:
            sprite.rect.y += SCROLL
        self.player.rect.y += SCROLL
        self.player.prev_y = self.player.rect.y
        self.score += 1

def platform_shake(self):
    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - self.shake_start_time

    if elapsed_time < self.shake_duration:
        # shaking effect
        self.visual_offset_x = random.randint(-self.shake_intensity, self.shake_intensity)
        self.visual_offset_y = random.randint(-self.shake_intensity, self.shake_intensity)
    else:
        # duration ended, kill
        self.kill()

def check_player_platform_collisions(self):
    # Reset ground state
    self.player.on_ground = False
    
    # Check for platform collision
    for platform in self.level.platforms:
        if self.player.rect.bottom == platform.rect.top and (self.player.rect.x >= platform.rect.x and self.player.rect.x <= platform.rect.x + PLATFORM_WIDTH):
            self.player.on_ground = True
            self.player.velocity_y = 0
            platform.touched = True
            break
        elif self.player.rect.colliderect(platform.rect):
            platform.touched = True
            # Only handle landing on top of platform when falling
            if self.player.velocity_y > 0:
                self.player.on_ground = True
                self.player.velocity_y = 0
                self.player.rect.bottom = platform.rect.top
                break