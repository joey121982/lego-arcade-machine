#!/usr/bin/env python3

import pygame
from .shell import *
from .globals import *

def run():
    pygame.init()
    glb = globals()
    screen = pygame.display.set_mode((glb.WINWIDTH, glb.WINHEIGHT))
    clock = pygame.time.Clock()
    shell = Shell(screen, glb)

    while(True):
        shell.parse_events()
        shell.update()
        clock.tick(60)

