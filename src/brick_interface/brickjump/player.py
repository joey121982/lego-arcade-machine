import math
import pygame
from .utilities import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, images):
        super().__init__()
        self.velocity_x = 0
        self.velocity_y = 0
        self.on_ground = False
        self.jump_power = -15
        self.images = images
        self.image = self.images[0]  # default image
        self.gravity = 0.8
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT

        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.prev_y = PLATFORM_INIT_Y - PLAYER_HEIGHT

        # visual animation coordinates
        self.anim_x = x
        self.anim_y = y

        # animation variables
        self.is_moving = False
        self.move_start_time = 0
        self.move_duration = 25  # increase duration for smoother arc
        self.start_x = x
        self.start_y = y
        self.target_x = x
        self.target_y = y
        self.arc_height = 0

    def ease_out_cubic(self, t):
        return 1 - (1 - t) ** 3

    def calculate_arc_position(self, t):
        # linear interpolation for X
        x = self.start_x + (self.target_x - self.start_x) * t

        # gentle arc for Y (use cosine for less overshoot)
        linear_y = self.start_y + (self.target_y - self.start_y) * t
        arc_offset = self.arc_height * (1 - math.cos(math.pi * t)) / 2
        y = linear_y - arc_offset

        return x, y

    def update(self, platforms):
        if self.is_moving:
            current_time = pygame.time.get_ticks()
            elapsed = current_time - self.move_start_time
            t = min(elapsed / self.move_duration, 1.0)  # normalize to 0-1
            
            x, y = self.calculate_arc_position(t)
            self.anim_x = int(x)
            self.anim_y = int(y)

            # check if animation is complete
            if t >= 0.95:
                self.is_moving = False
                self.rect.x = self.target_x
                self.rect.y = self.target_y
                self.anim_x = self.target_x
                self.anim_y = self.target_y
        else:
            # apply gravity only when not animating movement
            if not self.on_ground:
                self.velocity_y += self.gravity

            # update position with physics
            self.rect.x += self.velocity_x
            self.rect.y += self.velocity_y
            self.anim_x = self.rect.x
            self.anim_y = self.rect.y

        # check for platform collisions
        check_player_platform_collisions(self, platforms)

    def start_move_animation(self, target_x, target_y):
        if not self.is_moving:  # don't interrupt ongoing animation
            self.is_moving = True
            self.move_start_time = pygame.time.get_ticks()
            self.start_x = self.rect.x
            self.start_y = self.rect.y
            self.target_x = target_x
            self.target_y = target_y
            self.prev_y = self.rect.y
            
            horizontal_distance = abs(target_x - self.start_x)
            self.arc_height = max(10, horizontal_distance * 0.1)  # lower minimum and multiplier

    def move_up(self):
        target_y = self.rect.y - (HOVER + SCROLL)
        self.start_move_animation(self.rect.x, target_y)

    def move_left(self):
        target_x = PLAYER_ON_LEFT_PLATFORM_X
        target_y = self.rect.y - (HOVER + SCROLL)
        self.image = self.images[2]  # crouch left image
        self.start_move_animation(target_x, target_y)
        self.image = self.images[0]  # reset to left image after move

    def move_right(self):
        target_x = PLAYER_ON_RIGHT_PLATFORM_X
        target_y = self.rect.y - (HOVER + SCROLL)
        self.image = self.images[3]  # crouch right image
        self.start_move_animation(target_x, target_y)
        self.image = self.images[1]  # reset to right image after move

    def draw(self, screen):
        # use anim_x, anim_y for drawing if animating, else use rect
        draw_x = self.anim_x if self.is_moving else self.rect.x
        draw_y = self.anim_y if self.is_moving else self.rect.y
        screen.blit(self.image, (draw_x, draw_y))
