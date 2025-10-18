import pygame
import collections # deque

def load_images():
    background_image = pygame.image.load('./assets/bricktetris/images/tetris_background.jpg').convert()
    main_screen_image = pygame.image.load('./assets/bricktetris/images/main_screen.png').convert_alpha()
    next_screen_image = pygame.image.load('./assets/bricktetris/images/next_screen.png').convert_alpha()
    info_screen_image = pygame.image.load('./assets/bricktetris/images/info_screen.png').convert_alpha()
    return background_image, main_screen_image, next_screen_image, info_screen_image

TETROMINOES = {
    'I': {'shape': [[1, 1, 1, 1]], 'id': 1},
    'O': {'shape': [[2, 2], [2, 2]], 'id': 2},
    'T': {'shape': [[0, 3, 0], [3, 3, 3]], 'id': 3},
    'S': {'shape': [[0, 4, 4], [4, 4, 0]], 'id': 4},
    'Z': {'shape': [[5, 5, 0], [0, 5, 5]], 'id': 5},
    'J': {'shape': [[6, 0, 0], [6, 6, 6]], 'id': 6},
    'L': {'shape': [[0, 0, 7], [7, 7, 7]], 'id': 7}
}

# colors
GRAY = (30, 30, 30)
WHITE = (255, 255, 255)

# enum type dict
SHAPE_COLORS = {
    1: (0, 255, 255),      # Cyan for 'I'
    2: (255, 255, 0),      # Yellow for 'O'
    3: (160, 0, 255),      # Purple for 'T'
    4: (0, 255, 0),        # Green for 'S'
    5: (255, 0, 0),        # Red for 'Z'
    6: (0, 0, 255),        # Blue for 'J'
    7: (255, 165, 0)       # Orange for 'L'
}

# --- screen positioning ---
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
LEFT_RIGHT_MARGIN = 150
MAIN_SCREEN_TOP_DOWN_MARGIN = 40
MAIN_SCREEN_TOP_DOWN_BORDER_SIZE = 16
BETWEEN_SCREENS_MARGIN = 100
MAIN_SCREEN_WIDTH = SCREEN_WIDTH // 3
MAIN_SCREEN_HEIGHT = SCREEN_HEIGHT - 2 * MAIN_SCREEN_TOP_DOWN_MARGIN + 2 * MAIN_SCREEN_TOP_DOWN_BORDER_SIZE # 1008
NEXT_SCREEN_TOP_MARGIN = MAIN_SCREEN_TOP_DOWN_MARGIN + 50
INFO_SCREEN_DOWN_MARGIN = MAIN_SCREEN_TOP_DOWN_MARGIN + 50
MAIN_SCREEN_Y = MAIN_SCREEN_TOP_DOWN_MARGIN
NEXT_SCREEN_Y = NEXT_SCREEN_TOP_MARGIN
INFO_SCREEN_HEIGHT = SCREEN_HEIGHT // 2 - INFO_SCREEN_DOWN_MARGIN
INFO_SCREEN_Y = SCREEN_HEIGHT - INFO_SCREEN_DOWN_MARGIN - INFO_SCREEN_HEIGHT
INFO_SCREEN_WIDTH = MAIN_SCREEN_WIDTH - LEFT_RIGHT_MARGIN - BETWEEN_SCREENS_MARGIN
NEXT_SCREEN_WIDTH = INFO_SCREEN_WIDTH
NEXT_SCREEN_HEIGHT = INFO_SCREEN_HEIGHT
MAIN_SCREEN_X = SCREEN_WIDTH // 3
INFO_SCREEN_X = LEFT_RIGHT_MARGIN
NEXT_SCREEN_X = SCREEN_WIDTH - LEFT_RIGHT_MARGIN - NEXT_SCREEN_WIDTH
MAIN_SCREEN_SIDE_MARGIN = 70

# --- info screen text positioning ---
TOP_TEXT_Y_OFFSET = 25
TOP_TEXT_X_OFFSET = INFO_SCREEN_WIDTH // 2 - 40
TOP_INFO_Y_OFFSET = 80
TOP_INFO_X_OFFSET = INFO_SCREEN_WIDTH // 2 - 10
MIDDLE_TEXT_Y_OFFSET = 143
MIDDLE_TEXT_X_OFFSET = INFO_SCREEN_WIDTH // 2 - 40
MIDDLE_INFO_Y_OFFSET = 210
MIDDLE_INFO_X_OFFSET = INFO_SCREEN_WIDTH // 2 - 10
BOTTOM_TEXT_Y_OFFSET = 275
BOTTOM_TEXT_X_OFFSET = INFO_SCREEN_WIDTH // 2 - 40
BOTTOM_INFO_Y_OFFSET = 340
BOTTOM_INFO_X_OFFSET = INFO_SCREEN_WIDTH // 2 - 10

# --- next screen text positioning ---
TEXT_Y_OFFSET = 37
TEXT_X_OFFSET = NEXT_SCREEN_WIDTH // 2 - 40

# --- tetromino && grid ---
ROWS = 20
COLS = 10
BLOCK_SIZE = 48 
LINE_THICKNESS = 4
TS = 50 # TETROMINO_SIZE
TBS = 4 # TETROMINO_BORDER_SIZE
TBSH = TBS // 2 # TETROMINO_BORDER_SIZE_HALF
TETROMINO_START_Y = MAIN_SCREEN_TOP_DOWN_MARGIN + MAIN_SCREEN_TOP_DOWN_BORDER_SIZE
TETROMINO_START_X = MAIN_SCREEN_X + MAIN_SCREEN_SIDE_MARGIN + 4 * TS

# --- controls ---
MOVE_DOWN_DELAY = 5 # ms
MOVE_SIDEWAYS_DELAY = 5 # ms
