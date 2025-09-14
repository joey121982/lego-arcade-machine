import pygame

def controls(self):
    keys = pygame.key.get_pressed()
    state = {
        'w': keys[pygame.K_w],
        'a': keys[pygame.K_a],
        's': keys[pygame.K_s],
        'd': keys[pygame.K_d],
        'space': keys[pygame.K_SPACE]
    }

    if (state['space']):
        print("SPACE PRESSED!")
        