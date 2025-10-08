import pygame

def load_images():
    background_image = pygame.image.load('./assets/bricktetris/images/tetris_background.jpg').convert()
    main_screen_image = pygame.image.load('./assets/bricktetris/images/main_screen.png').convert_alpha()
    next_screen_image = pygame.image.load('./assets/bricktetris/images/next_screen.png').convert_alpha()
    info_screen_image = pygame.image.load('./assets/bricktetris/images/info_screen.png').convert_alpha()
    return background_image, main_screen_image, next_screen_image, info_screen_image

SHAPES = {
    'I': [[1, 1, 1, 1]],
    'O': [[1, 1],
          [1, 1]],
    'T': [[0, 1, 0],
          [1, 1, 1]],
    'S': [[0, 1, 1],
          [1, 1, 0]],
    'Z': [[1, 1, 0],
          [0, 1, 1]],
    'J': [[0, 0, 1],
          [1, 1, 1]],
    'L': [[1, 0, 0],
          [1, 1, 1]]
}

# colors
GRAY = (30, 30, 30)

LIGHT_BLUE = (137, 207, 240)
DARK_BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)

SHAPE_COLORS = {
    'I': CYAN ,
    'O': YELLOW,
    'T': PURPLE,
    'S': GREEN,
    'Z': RED,
    'J': BLUE,
    'L': ORANGE
}

# screen positioning
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

# info screen positioning
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

# next screen positioning
TEXT_Y_OFFSET = 37
TEXT_X_OFFSET = NEXT_SCREEN_WIDTH // 2 - 40

# tetromino
TS = 50 # TETROMINO_SIZE
TBS = 4 # TETROMINO_BORDER_SIZE
TBSH = TBS // 2 # TETROMINO_BORDER_SIZE_HALF
TETROMINO_START_Y = MAIN_SCREEN_TOP_DOWN_MARGIN + MAIN_SCREEN_TOP_DOWN_BORDER_SIZE
TETROMINO_START_X = MAIN_SCREEN_X + 70 + 4 * TS