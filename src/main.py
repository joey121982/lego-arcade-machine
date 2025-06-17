#!/usr/bin/env python3

import pygame
from shell import *

def run():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    shell = Shell()

    while(True):
        shell.parse_events()
        shell.update()
        clock.tick(60)

