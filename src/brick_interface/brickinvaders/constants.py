import pygame
# Constants for Brick Invaders game

# Screen settings
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
FPS = 60

# Animation settings
PLANET_OFFSET_X = -1000 # Lower is left
PLANET_OFFSET_Y = 400 # Lower is higher

GALAXY_OFFSET_X = -750
GALAXY_OFFSET_Y = -100

STAR_OFFSET_X = -900
STAR_OFFSET_Y = 100

# FIX BLACKHOLE Y OFFSET
BLACKHOLE_OFFSET_X = -250
BLACKHOLE_OFFSET_Y = 100

ANIMATION_SLOWDOWN = 50  # Higher is slower
PLANET_FRAME_WIDTH = 480
PLANET_FRAME_HEIGHT = 480
PLANET_SPRITESHEET_COLUMNS = 32
PLANET_SPRITESHEET_ROWS = 32
PLANET_TOTAL_FRAMES = PLANET_SPRITESHEET_COLUMNS * PLANET_SPRITESHEET_ROWS

# Spaceship settings
SPACESHIP_SPEED = 10
SPACESHIP_ACCELERATION = 0.6
SPACESHIP_FRICTION = 0.4
SPACESHIP_VELOCITY_LIMIT = 15
SPACESHIP_COUNTER_STRAFE_MULTIPLIER = 2
SPACESHIP_ANGLE_INCREMENT = 5
SPACESHIP_FRAME_WIDTH = 48
SPACESHIP_FRAME_HEIGHT = 48
SPACESHIP_SPRITESHEET_COLUMNS = 2
SPACESHIP_SPRITESHEET_ROWS = 2
SPACESHIP_TOTAL_FRAMES = SPACESHIP_SPRITESHEET_COLUMNS * SPACESHIP_SPRITESHEET_ROWS

# Bullet settings
BULLET_SPEED = 30
BULLET_WIDTH = 20
BULLET_HEIGHT = 20
BULLET_COLOR = (255, 255, 0)

# Invader settings
INVADER_ROWS = 5
INVADER_COLUMNS = 11
INVADER_START_X = 200
INVADER_START_Y = 50
INVADER_SPEED = 2
INVADER_DOWN = 30
INVADER_WIDTH = SCREEN_WIDTH // 25
INVADER_HEIGHT = SCREEN_HEIGHT // 17

# Colors
COLOR_RED = (255, 0, 0)
COLOR_YELLOW = (255, 255, 0)
COLOR_WHITE = (255, 255, 255)

def load_images():
    bullet_image = pygame.transform.scale(
        pygame.image.load('./assets/brickinvaders/images/BI_bullet.png').convert_alpha(),
        (BULLET_WIDTH, BULLET_HEIGHT)
    )
    invader_image = pygame.transform.scale(
        pygame.image.load('./assets/brickinvaders/images/BI_invader.png').convert_alpha(),
        (INVADER_WIDTH, INVADER_HEIGHT)
    )
    planets = [
        pygame.image.load('./assets/brickinvaders/images/planet1_spritesheet.png').convert_alpha(),
        pygame.image.load('./assets/brickinvaders/images/planet2_spritesheet.png').convert_alpha(),
        pygame.image.load('./assets/brickinvaders/images/planet3_spritesheet.png').convert_alpha(),
        pygame.image.load('./assets/brickinvaders/images/planet4_spritesheet.png').convert_alpha(),
        pygame.image.load('./assets/brickinvaders/images/planet5_spritesheet.png').convert_alpha(),
        pygame.image.load('./assets/brickinvaders/images/planet6_spritesheet.png').convert_alpha(),
        pygame.image.load('./assets/brickinvaders/images/planet7_spritesheet.png').convert_alpha(),
        pygame.image.load('./assets/brickinvaders/images/galaxy_spritesheet.png').convert_alpha(),
        pygame.image.load('./assets/brickinvaders/images/star_spritesheet.png').convert_alpha(),
        pygame.image.load('./assets/brickinvaders/images/blackhole_spritesheet.png').convert_alpha(),
    ]
    return bullet_image, invader_image, planets

# Level definitions
LEVELS = [
    {
        "rows": 5, #5
        "columns": 9, #9
        "invader_speed": 2, #2
        "pattern": "default"
    },
    {
        "rows": 4, #4
        "columns": 9, #9
         "invader_speed": 3,
        "pattern": "zigzag"
    },
    {
        "rows": 7, #7
        "columns": 13, #13
        "invader_speed": 1.2,
        "pattern": "dense"
    },
    {
        "rows": 6, #6
        "columns": 11, #11
        "invader_speed": 2.5,
        "pattern": "semicircle"
    },
    {
        "rows": 8,
        "columns": 14,
        "invader_speed": 2.8,
        "pattern": "checker"
    },
    {
        "rows": 5,
        "columns": 15,
        "invader_speed": 3.2,
        "pattern": "wave"
    },
    {
        "rows": 9,
        "columns": 12,
        "invader_speed": 3.5,
        "pattern": "spiral"
    },
    # Especially difficult levels
    {
        "rows": 10,
        "columns": 16,
        "invader_speed": 4.5,
        "pattern": "chaos"
    },
    {
        "rows": 12,
        "columns": 18,
        "invader_speed": 5.5,
        "pattern": "wall"
    },
    {
        "rows": 15,
        "columns": 20,
        "invader_speed": 7,
        "pattern": "onslaught"
    }
    
]
