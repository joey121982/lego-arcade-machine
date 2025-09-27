import pygame
import random
from .constants import *

def death_screen(self):
    # Display death screen for a short duration
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    overlay.set_alpha(180)
    overlay.fill((0, 0, 0))
    self.screen.blit(overlay, (0, 0))

    font = pygame.font.SysFont(None, 64)
    score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
    gameover_text = font.render("Game Over", True, (255, 0, 0))

    self.screen.blit(gameover_text, (SCREEN_WIDTH // 2 - gameover_text.get_width() // 2, SCREEN_HEIGHT // 2 - 80))
    self.screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2))

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                self.glb.return_to_menu = True
            elif event.type == pygame.KEYDOWN:
                waiting = False
                self.glb.return_to_menu = True

def check_player_below_screen(self):
    if self.player.rect.top >= SCREEN_HEIGHT:
        death_screen(self)
        #add a slight delay to avoid instant restart
        pygame.time.delay(150)

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

def check_player_platform_collisions(player, platforms):
    # Reset ground state
    player.on_ground = False

    for platform in platforms:
        # Check for collision: player is close enough to land on top of platform
        if abs(player.rect.bottom - platform.rect.top) <= GROUND_FORGIVENESS and \
        player.rect.x >= platform.rect.x and \
        player.rect.x <= platform.rect.x + PLATFORM_WIDTH and \
        player.velocity_y >= 0:
            player.on_ground = True
            player.velocity_y = 0
            platform.touched = True
            # Optionally snap player to platform
            player.rect.bottom = platform.rect.top
            break
        elif player.rect.colliderect(platform.rect):
            platform.touched = True
            if player.velocity_y > 0:
                player.on_ground = True
                player.velocity_y = 0
                player.rect.bottom = platform.rect.top
                break