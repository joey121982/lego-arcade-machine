import pygame

class Menu:
    name = "Menu"
    new_game = "None"
    background = None
    screen = None
    glb = None

    def __init__(self, new_screen, new_globals):
        self.screen = new_screen
        self.glb = new_globals
        self.background = pygame.image.load("assets/bg.png")
        self.background = pygame.transform.scale(self.background, (self.glb.WINWIDTH, self.glb.WINHEIGHT))

    def update(self):
        if not self.screen:
            print("No screen at Menu.update()... Check for errors.")
            return
        
        if not self.background:
            print("Background not loaded at Menu.update()... Check for errors.")
            return
        
        self.screen.blit(self.background, (0, 0))
        pygame.display.update()