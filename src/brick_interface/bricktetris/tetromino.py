import pygame
from .constants import *

class Tetromino:
    def __init__(self, screen, x, y, shape):
        self.screen = screen
        self.actual_x = x
        self.actual_y = y
        self.draw_x = x
        self.draw_y = y
        self.shape = shape
        
    def rotate(self):
        pass

    def update(self):
        pass
    
    
    # the python.draw.polygon function draws the border half outisde the shape and half inside the shape, so we adjusts our draw coords accordingly by
    # subtracting half the border size from the top-left corner everywhere. (TBSH)
    # the magic numbers come from the inconsistencies that come with the border feature of pygame.draw.polygon.
    # for some reason, sometimes the function draws the border one pixel outside the shape, sometimes it draws it perfectly aligned with the shape, and sometimes it draws it one pixel inside the shape.
    # to counter this, we add or subtract one pixel from the coordinates of the points we give to the function.
    # this way, the border is always drawn inside the shape, and the shape is always the correct size.
    # this is a hacky solution, but it works
    def draw_I(self):
        x = self.draw_x + TBSH
        y = self.draw_y + TBSH
        p1 = (x - 1, y - 1)
        p2 = (x - 1, y + 4 * TS - TBS - 1)
        p3 = (x + TS - TBS - 1, y + 4 * TS - TBS - 1)
        p4 = (x + TS - TBS - 1, y - 1)
        p = [p1, p2, p3, p4]
        # draw the shape
        pygame.draw.polygon(self.screen, GRAY, p)
        pygame.draw.polygon(self.screen, SHAPE_COLORS['I'], p, TBS)

    def draw_O(self):
        x = self.draw_x + TBSH
        y = self.draw_y + TBSH
        p1 = (x - 1, y - 1)
        p2 = (x - 1, y + 2 * TS - TBS - 1)
        p3 = (x + 2 * TS - TBS - 1, y + 2 * TS - TBS - 1)
        p4 = (x + 2 * TS - TBS - 1, y - 1)
        p = [p1, p2, p3, p4]
        # draw the shape
        pygame.draw.polygon(self.screen, GRAY, p)
        pygame.draw.polygon(self.screen, SHAPE_COLORS['O'], p, TBS)

    def draw_T(self):
        x = self.draw_x + TBSH
        y = self.draw_y + TBSH
        p1 = (x - 1, y - 1)
        p2 = (x - 1, y + TS - 1)
        p3 = (x - TS - 1, y + TS - 1)
        p4 = (x - TS - 1, y + 2 * TS - TBS - 1)
        p5 = (x + 2 * TS - TBS - 1, y + 2 * TS - TBS - 1)
        p6 = (x + 2 * TS - TBS - 1, y + TS - 1)
        p7 = (x + TS - TBS - 1, y + TS - 1)
        p8 = (x + TS - TBS - 1, y - 1)
        p = [p1, p2, p3, p4, p5, p6, p7, p8] 
        # draw the shape
        pygame.draw.polygon(self.screen, GRAY, p)
        pygame.draw.polygon(self.screen, SHAPE_COLORS['T'], p, TBS)

    def draw_Z(self):
        x = self.draw_x + TBSH
        y = self.draw_y + TBSH
        p1 = (x - 1, y - 1)
        p2 = (x - 1, y + TS - TBS - 1)
        p3 = (x - 1 + TS, y + TS - TBS - 1)
        p4 = (x - 1 + TS, y + 2 * TS - TBS - 1)
        p5 = (x + 3 * TS - TBS - 1, y + 2 * TS - TBS - 1)
        p6 = (x + 3 * TS - TBS - 1, y + TS)
        p7 = (x + 2 * TS - TBS - 1, y + TS)
        p8 = (x + 2 * TS - TBS - 1, y - 1)
        p = [p1, p2, p3, p4, p5, p6, p7, p8]
        # draw the shape
        pygame.draw.polygon(self.screen, GRAY, p)
        pygame.draw.polygon(self.screen, SHAPE_COLORS['Z'], p, TBS)
        
    def draw_S(self):
        x = self.draw_x + TBSH
        y = self.draw_y + TBSH
        p1 = (x - 1, y - 1)
        p2 = (x - 1, y + TS - 1)
        p3 = (x - TS - 1, y + TS - 1)
        p4 = (x - TS - 1, y + 2 * TS - TBS - 1)
        p5 = (x + TS - TBS - 1, y + 2 * TS - TBS - 1)
        p6 = (x + TS - TBS - 1, y + TS - TBS - 1)
        p7 = (x + 2 * TS - TBS - 1, y + TS - TBS - 1)
        p8 = (x + 2 * TS - TBS - 1, y - 1)
        p = [p1, p2, p3, p4, p5, p6, p7, p8]
        # draw the shape
        pygame.draw.polygon(self.screen, GRAY, p)
        pygame.draw.polygon(self.screen, SHAPE_COLORS['S'], p, TBS)
        
    def draw_L(self):
        x = self.draw_x + TBSH
        y = self.draw_y + TBSH
        p1 = (x - 1, y - 1)
        p2 = (x - 1, y + 2 * TS - TBS - 1)
        p3 = (x + 3 * TS - TBS - 1, y + 2 * TS - TBS - 1)
        p4 = (x + 3 * TS - TBS - 1, y + 1 * TS - 1)
        p5 = (x + TS - TBS - 1, y + 1 * TS - 1)
        p6 = (x + TS - TBS - 1, y - 1)
        p = [p1, p2, p3, p4, p5, p6]
        # draw the shape
        pygame.draw.polygon(self.screen, GRAY, p)
        pygame.draw.polygon(self.screen, SHAPE_COLORS['L'], p, TBS)
    
    def draw_J(self):
        x = self.draw_x + TBSH
        y = self.draw_y + TBSH
        p1 = (x - 1, y - 1)
        p2 = (x - 1, y + TS - 1)
        p3 = (x - 2 * TS - 1, y + TS - 1)
        p4 = (x - 2 * TS - 1, y + 2 * TS - TBS - 1)
        p5 = (x + TS - TBS - 1, y + 2 * TS - TBS - 1)
        p6 = (x + TS - TBS - 1, y - 1)
        p = [p1, p2, p3, p4, p5, p6]
        # draw the shape
        pygame.draw.polygon(self.screen, GRAY, p)
        pygame.draw.polygon(self.screen, SHAPE_COLORS['J'], p, TBS)

    def draw(self):
        if self.shape == 'I':
            self.draw_I()
        elif self.shape == 'O':
            self.draw_O()
        elif self.shape == 'T':
            self.draw_T()
        elif self.shape == 'S':
            self.draw_S()
        elif self.shape == 'Z':
            self.draw_Z()
        elif self.shape == 'J':
            self.draw_J()
        elif self.shape == 'L':
            self.draw_L()
