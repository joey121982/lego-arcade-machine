import pygame

class Screen:
    def __init__(self, screen, x, y, image)
        self.screen = screen
        self.x = x
        self.y = y
        self.image = image

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

class PlayableScreen(Screen):
    def __init__(self, screen, x, y, image):
        super().__init__(screen, x, y, image)

class InfoScreen(Screen):
    def __init__(self, screen, x, y, image, score, level, lines):
        super().__init__(screen, x, y, image)
        self.score = score
        self.level = level
        self.lines = lines
        
    def draw(self):
        super().draw()
        # Draw score, level, lines on the screen
        
    