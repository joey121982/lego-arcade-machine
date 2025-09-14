#!/usr/bin/env python3

import pygame
from .shell import *
from .globals import *
from .brickinvaders.constants import load_images

def run():
    pygame.init()
    glb = globals()
    screen = pygame.display.set_mode((glb.WINWIDTH, glb.WINHEIGHT))
    pygame.display.set_caption('Brick Box')
    clock = pygame.time.Clock()

    # Preload images for Brick Invaders after display is initialized
    brickinvaders_images = load_images()
    shell = Shell(screen, glb, brickinvaders_images)

    while(True):
        shell.parse_events()
        shell.update()
        clock.tick(60)

