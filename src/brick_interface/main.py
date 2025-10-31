#!/usr/bin/env python3

import pygame
import RPi.GPIO
from .shell import *
from .globals import *

def run():

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    pins = [1, 2, 3]
    for pin in pins:
        GPIO.setup(pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

    pygame.init()
    glb = globals()
    screen = pygame.display.set_mode((glb.WINWIDTH, glb.WINHEIGHT))
    pygame.display.set_caption('Brick Box')
    clock = pygame.time.Clock()
    shell = Shell(screen, glb)

    while(True):
        shell.parse_events()
        shell.update()
        clock.tick(60)

