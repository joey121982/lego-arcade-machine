import pygame
from .constants import *

class Screen:
    def __init__(self, screen, x, y, image):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = image
        self.font_text = pygame.font.Font("./assets/bricktetris/fonts/Pixellettersfull-BnJ5.ttf", 36)

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

class PlayableScreen(Screen):
    def __init__(self, screen, x, y, image):
        super().__init__(screen, x, y, image)
        
class NextScreen(Screen):
    def __init__(self, screen, x, y, image, next_piece):
        super().__init__(screen, x, y, image)
        self.next_piece = next_piece
        self.font_text = pygame.font.Font("./assets/bricktetris/fonts/Pixellettersfull-BnJ5.ttf", 54)

    def draw(self):
        super().draw()
        # Draw the text "Next" on screen
        next_text = self.font_text.render("Next", True, WHITE)
        self.screen.blit(next_text, (self.x + TEXT_X_OFFSET, self.y + TEXT_Y_OFFSET))

class InfoScreen(Screen):
    def __init__(self, screen, x, y, image, score, level, lines):
        super().__init__(screen, x, y, image)
        self.score = score
        self.level = level
        self.lines = lines
        
    def draw(self):
        super().draw()
        # Draw score, level, lines on the screen
        score_text = self.font_text.render(f"Score", True, WHITE)
        score_info = self.font_text.render(f"{self.score}", True, WHITE)
        level_text = self.font_text.render(f"Level", True, WHITE)
        level_info = self.font_text.render(f"{self.level}", True, WHITE)
        lines_text = self.font_text.render(f"Lines", True, WHITE)
        lines_info = self.font_text.render(f"{self.lines}", True, WHITE)
        self.screen.blit(score_text, (self.x + TOP_TEXT_X_OFFSET, self.y + TOP_TEXT_Y_OFFSET))
        self.screen.blit(score_info, (self.x + TOP_INFO_X_OFFSET, self.y + TOP_INFO_Y_OFFSET))
        self.screen.blit(level_text, (self.x + MIDDLE_TEXT_X_OFFSET, self.y + MIDDLE_TEXT_Y_OFFSET))
        self.screen.blit(level_info, (self.x + MIDDLE_INFO_X_OFFSET, self.y + MIDDLE_INFO_Y_OFFSET))
        self.screen.blit(lines_text, (self.x + BOTTOM_TEXT_X_OFFSET, self.y + BOTTOM_TEXT_Y_OFFSET))
        self.screen.blit(lines_info, (self.x + BOTTOM_INFO_X_OFFSET, self.y + BOTTOM_INFO_Y_OFFSET))
