import math
import pygame
from .utilities import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.velocity_x = 0
        self.velocity_y = 0
        self.on_ground = False
        self.jump_power = -15
        self.gravity = 0.8
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT

        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.prev_y = PLATFORM_INIT_Y - PLAYER_HEIGHT

        # Animation variables
        self.is_moving = False
        self.move_start_time = 0
        self.move_duration = 500  # Increased duration for smoother arc
        self.start_x = x
        self.start_y = y
        self.target_x = x
        self.target_y = y
        
        # Arc trajectory variables
        self.arc_height = 100  # How high the arc goes above the start/end points

    def ease_out_cubic(self, t):
        """Smooth easing function for animations"""
        return 1 - (1 - t) ** 3

    def calculate_arc_position(self, t):
        """Calculate position along a parabolic arc"""
        # Linear interpolation for X
        x = self.start_x + (self.target_x - self.start_x) * t
        
        # Parabolic arc for Y (creates semicircle-like trajectory)
        # y = start_y + (target_y - start_y) * t - arc_height * sin(π * t)
        linear_y = self.start_y + (self.target_y - self.start_y) * t
        arc_offset = self.arc_height * math.sin(math.pi * t)
        y = linear_y - arc_offset
        
        return x, y

    def update(self, platforms):
        # Handle movement animation
        if self.is_moving:
            current_time = pygame.time.get_ticks()
            elapsed = current_time - self.move_start_time
            t = min(elapsed / self.move_duration, 1.0)  # Normalize to 0-1
            
            # Calculate arc position
            x, y = self.calculate_arc_position(t)
            self.rect.x = int(x)
            self.rect.y = int(y)
            
            # Check if animation is complete
            if t >= 1.0:
                self.is_moving = False
                self.rect.x = self.target_x
                self.rect.y = self.target_y
        else:
            # Apply gravity only when not animating movement
            if not self.on_ground:
                self.velocity_y += self.gravity

            # Update position with physics
            self.rect.x += self.velocity_x
            self.rect.y += self.velocity_y

        # Update x, y for compatibility
        self.x = self.rect.x
        self.y = self.rect.y

        # Check for platform collisions (your existing collision logic)
        check_player_platform_collisions(self)

    def start_move_animation(self, target_x, target_y):
        """Start an animated movement to target position with arc trajectory"""
        if not self.is_moving:  # Don't interrupt ongoing animation
            self.is_moving = True
            self.move_start_time = pygame.time.get_ticks()
            self.start_x = self.rect.x
            self.start_y = self.rect.y
            self.target_x = target_x
            self.target_y = target_y
            self.prev_y = self.rect.y
            
            # Adjust arc height based on horizontal distance
            horizontal_distance = abs(target_x - self.start_x)
            self.arc_height = max(50, horizontal_distance * 0.3)  # Dynamic arc height

    def move_up(self):
        target_y = self.rect.y - (HOVER + SCROLL)
        self.start_move_animation(self.rect.x, target_y)

    def move_left(self):
        target_x = LEFT_PLATFORM_X + PLATFORM_WIDTH // 2 - PLAYER_WIDTH // 2
        target_y = self.rect.y - (HOVER + SCROLL)
        self.start_move_animation(target_x, target_y)

    def move_right(self):
        target_x = RIGHT_PLATFORM_X + PLATFORM_WIDTH // 2 - PLAYER_WIDTH // 2
        target_y = self.rect.y - (HOVER + SCROLL)
        self.start_move_animation(target_x, target_y)

    def draw(self, screen):
        # Add a subtle visual effect during movement
        color = (0, 150, 255) if self.is_moving else (0, 0, 255)
        pygame.draw.rect(screen, color, self.rect)
        
        # Optional: Add a trail effect during movement
        if self.is_moving:
            trail_rect = pygame.Rect(self.rect.x + 2, self.rect.y + 2, 
                                   self.width - 4, self.height - 4)
            pygame.draw.rect(screen, (100, 100, 255), trail_rect)