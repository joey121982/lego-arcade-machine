import pygame
import collections
import random
from .constants import *

class Screen:
    def __init__(self, screen, x, y, image):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = image
        self.font_text = pygame.font.Font("./assets/fonts/Pixellettersfull-BnJ5.ttf", 36)

    def draw(self):
        if self.image and not isinstance(self, PlayableScreen):
             self.screen.blit(self.image, (self.x, self.y))

class PlayableScreen(Screen):
    def __init__(self, screen, x, y):
        super().__init__(screen, x, y, None) 
        self.rows = ROWS
        self.cols = COLS
        self.matrix = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        
        self.score = 0
        self.level = 1
        self.lines_cleared_total = 0
        self.game_over = False

        self.current_piece = None
        self.next_piece_shape = random.choice(list(TETROMINOES.keys()))
        self.spawn_piece()

    def spawn_piece(self):
        shape_name = self.next_piece_shape
        self.current_piece = {
            'name': shape_name,
            'shape': TETROMINOES[shape_name]['shape'],
            'id': TETROMINOES[shape_name]['id'],
            'row': 0,
            'col': self.cols // 2 - len(TETROMINOES[shape_name]['shape'][0]) // 2
        }
        self.next_piece_shape = random.choice(list(TETROMINOES.keys()))

        if not self.is_valid_position():
            self.game_over = True

    def is_valid_position(self, piece=None, offset_r=0, offset_c=0):
        p = piece or self.current_piece
        for row, row_data in enumerate(p['shape']):
            for col, cell_val in enumerate(row_data):
                if cell_val != 0:
                    board_r, board_c = p['row'] + row + offset_r, p['col'] + col + offset_c
                    if not (0 <= board_r < self.rows and 0 <= board_c < self.cols):
                        return False
                    if self.matrix[board_r][board_c] != 0:
                        return False
        return True

    def lock_piece(self):
        p = self.current_piece
        for row, row_data in enumerate(p['shape']):
            for col, cell_val in enumerate(row_data):
                if cell_val != 0:
                    self.matrix[p['row'] + row][p['col'] + col] = p['id']
        self.clear_lines()
        self.spawn_piece()

    def clear_lines(self):
        new_matrix = [row for row in self.matrix if not all(cell != 0 for cell in row)]
        lines_cleared = self.rows - len(new_matrix)
        self.lines_cleared_total += lines_cleared
        self.score += lines_cleared * 100 * self.level
        self.level = 1 + (self.lines_cleared_total // 10)
        for _ in range(lines_cleared):
            new_matrix.insert(0, [0 for _ in range(self.cols)])
        self.matrix = new_matrix

    def move_left(self):
        if self.is_valid_position(offset_c=-1): self.current_piece['col'] -= 1
    def move_right(self):
        if self.is_valid_position(offset_c=1): self.current_piece['col'] += 1
    def drop(self):
        if not self.game_over:
            if self.is_valid_position(offset_r=1): self.current_piece['row'] += 1
            else: self.lock_piece()

    def rotate(self):
        p = self.current_piece
        original_shape = p['shape']
        transposed = list(zip(*original_shape))
        p['shape'] = [list(row) for row in transposed[::-1]]
        if not self.is_valid_position():
            p['shape'] = original_shape

    def draw(self):
        # --- draw locked pieces with correct shared borders ---
        for row in range(self.rows):
            for col in range(self.cols):
                color_id = self.matrix[row][col]
                if color_id == 0:
                    continue

                draw_color = SHAPE_COLORS.get(color_id, WHITE)

                # get neighbor colors, treating out-of-bounds as empty (0)
                top_color_id = self.matrix[row - 1][col] if row > 0 else 0
                bottom_color_id = self.matrix[row + 1][col] if row + 1 < self.rows else 0
                left_color_id = self.matrix[row][col - 1] if col > 0 else 0
                right_color_id = self.matrix[row][col + 1] if col + 1 < self.cols else 0

                # pixel coordinates for the current block's corners
                tl = (self.x + col * TS + MAIN_SCREEN_SIDE_MARGIN, self.y + row * TS + MAIN_SCREEN_TOP_DOWN_BORDER_SIZE)
                tr = (self.x + (col + 1) * TS + MAIN_SCREEN_SIDE_MARGIN, self.y + row * TS + MAIN_SCREEN_TOP_DOWN_BORDER_SIZE)
                bl = (self.x + col * TS + MAIN_SCREEN_SIDE_MARGIN, self.y + (row + 1) * TS + MAIN_SCREEN_TOP_DOWN_BORDER_SIZE)
                br = (self.x + (col + 1) * TS + MAIN_SCREEN_SIDE_MARGIN, self.y + (row + 1) * TS + MAIN_SCREEN_TOP_DOWN_BORDER_SIZE)

                # draw border lines only if the neighbor is a different color
                if color_id != top_color_id:
                    pygame.draw.line(self.screen, draw_color, tl, tr, TBS)
                if color_id != bottom_color_id:
                    pygame.draw.line(self.screen, draw_color, bl, br, TBS)
                if color_id != left_color_id:
                    pygame.draw.line(self.screen, draw_color, tl, bl, TBS)
                if color_id != right_color_id:
                    pygame.draw.line(self.screen, draw_color, tr, br, TBS)

        # draw the currently falling piece with the same perimeter logic
        if self.current_piece and not self.game_over:
            p = self.current_piece
            shape = p['shape']
            draw_color = SHAPE_COLORS.get(p['id'], WHITE)
            
            shape_rows = len(shape)
            shape_cols = len(shape[0])

            for row_idx, row_data in enumerate(shape):
                for col_idx, cell_val in enumerate(row_data):
                    if cell_val != 0:
                        # get neighbor values from within the piece's own shape matrix
                        top_val = shape[row_idx - 1][col_idx] if row_idx > 0 else 0
                        bottom_val = shape[row_idx + 1][col_idx] if row_idx + 1 < shape_rows else 0
                        left_val = shape[row_idx][col_idx - 1] if col_idx > 0 else 0
                        right_val = shape[row_idx][col_idx + 1] if col_idx + 1 < shape_cols else 0

                        # calculate absolute pixel coordinates for the block's corners
                        abs_r, abs_c = p['row'] + row_idx, p['col'] + col_idx
                        tl = (self.x + abs_c * TS + MAIN_SCREEN_SIDE_MARGIN, self.y + abs_r * TS + MAIN_SCREEN_TOP_DOWN_BORDER_SIZE)
                        tr = (self.x + (abs_c + 1) * TS + MAIN_SCREEN_SIDE_MARGIN, self.y + abs_r * TS + MAIN_SCREEN_TOP_DOWN_BORDER_SIZE)
                        bl = (self.x + abs_c * TS + MAIN_SCREEN_SIDE_MARGIN, self.y + (abs_r + 1) * TS + MAIN_SCREEN_TOP_DOWN_BORDER_SIZE)
                        br = (self.x + (abs_c + 1) * TS + MAIN_SCREEN_SIDE_MARGIN, self.y + (abs_r + 1) * TS + MAIN_SCREEN_TOP_DOWN_BORDER_SIZE)

                        # draw border lines only if the neighbor is empty (0)
                        if top_val == 0:
                            pygame.draw.line(self.screen, draw_color, tl, tr, TBS)
                        if bottom_val == 0:
                            pygame.draw.line(self.screen, draw_color, bl, br, TBS )
                        if left_val == 0:
                            pygame.draw.line(self.screen, draw_color, tl, bl, TBS)
                        if right_val == 0:
                            pygame.draw.line(self.screen, draw_color, tr, br, TBS)

class NextScreen(Screen):
    def __init__(self, screen, x, y, image):
        super().__init__(screen, x, y, image)
        self.font_text = pygame.font.Font("./assets/bricktetris/fonts/Pixellettersfull-BnJ5.ttf", 54)

    def draw(self, next_piece_shape_name):
        super().draw()
        next_text = self.font_text.render("Next", True, WHITE)
        self.screen.blit(next_text, (self.x + TEXT_X_OFFSET, self.y + TEXT_Y_OFFSET))

        if next_piece_shape_name:
            piece = TETROMINOES[next_piece_shape_name]
            shape = piece['shape']
            color = SHAPE_COLORS.get(piece['id'], WHITE)
            
            start_x = self.x + (self.image.get_width() / 2) - ((len(shape[0]) * TS) / 2)
            start_y = self.y + (self.image.get_height() / 2) - ((len(shape) * TS) / 2)

            shape_rows = len(shape)
            shape_cols = len(shape[0])

            for r_idx, row_data in enumerate(shape):
                for c_idx, cell_val in enumerate(row_data):
                    if cell_val != 0:
                        # Get neighbor values from within the piece's own shape matrix
                        top_val = shape[r_idx - 1][c_idx] if r_idx > 0 else 0
                        bottom_val = shape[r_idx + 1][c_idx] if r_idx + 1 < shape_rows else 0
                        left_val = shape[r_idx][c_idx - 1] if c_idx > 0 else 0
                        right_val = shape[r_idx][c_idx + 1] if c_idx + 1 < shape_cols else 0
                        
                        # Calculate absolute pixel coordinates for the block's corners
                        tl = (start_x + c_idx * TS, start_y + r_idx * TS)
                        tr = (start_x + (c_idx + 1) * TS, start_y + r_idx * TS)
                        bl = (start_x + c_idx * TS, start_y + (r_idx + 1) * TS)
                        br = (start_x + (c_idx + 1) * TS, start_y + (r_idx + 1) * TS)

                        # Draw border lines only if the neighbor is empty (0)
                        if top_val == 0:
                            pygame.draw.line(self.screen, color, tl, tr, TBS)
                        if bottom_val == 0:
                            pygame.draw.line(self.screen, color, bl, br, TBS)
                        if left_val == 0:
                            pygame.draw.line(self.screen, color, tl, bl, TBS)
                        if right_val == 0:
                            pygame.draw.line(self.screen, color, tr, br, TBS)

class InfoScreen(Screen):
    def __init__(self, screen, x, y, image):
        super().__init__(screen, x, y, image)
    
    def draw(self, score, level, lines):
        super().draw()
        score_text = self.font_text.render("Score", True, WHITE)
        score_info = self.font_text.render(f"{score}", True, WHITE)
        level_text = self.font_text.render("Level", True, WHITE)
        level_info = self.font_text.render(f"{level}", True, WHITE)
        lines_text = self.font_text.render("Lines", True, WHITE)
        lines_info = self.font_text.render(f"{lines}", True, WHITE)
        
        self.screen.blit(score_text, (self.x + TOP_TEXT_X_OFFSET, self.y + TOP_TEXT_Y_OFFSET))
        self.screen.blit(score_info, (self.x + TOP_INFO_X_OFFSET, self.y + TOP_INFO_Y_OFFSET))
        self.screen.blit(level_text, (self.x + MIDDLE_TEXT_X_OFFSET, self.y + MIDDLE_TEXT_Y_OFFSET))
        self.screen.blit(level_info, (self.x + MIDDLE_INFO_X_OFFSET, self.y + MIDDLE_INFO_Y_OFFSET))
        self.screen.blit(lines_text, (self.x + BOTTOM_TEXT_X_OFFSET, self.y + BOTTOM_TEXT_Y_OFFSET))
        self.screen.blit(lines_info, (self.x + BOTTOM_INFO_X_OFFSET, self.y + BOTTOM_INFO_Y_OFFSET))

