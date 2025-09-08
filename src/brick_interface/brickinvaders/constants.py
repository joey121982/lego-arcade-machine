import pygame
# Constants for Brick Invaders game

# Screen settings
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
FPS = 60
PLANET_OFFSET = (-750, 500)
PLANET_OFFSET_X = -750
PLANET_OFFSET_Y = 500

# Spaceship settings
SPACESHIP_SPEED = 10
SPACESHIP_ACCELERATION = 0.6
SPACESHIP_FRICTION = 0.4
SPACESHIP_VELOCITY_LIMIT = 15
SPACESHIP_COUNTER_STRAFE_MULTIPLIER = 2
SPACESHIP_ANGLE_INCREMENT = 5

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
        pygame.image.load('./assets/brickinvaders/images/BI_planet1.png').convert_alpha(),
        pygame.image.load('./assets/brickinvaders/images/BI_planet2.png').convert_alpha(),
        pygame.image.load('./assets/brickinvaders/images/BI_planet3.png').convert_alpha()
    ]
    return bullet_image, invader_image, planets

# Level definitions
LEVELS = [
    {
        "rows": 1, #5
        "columns": 1, #9
        "invader_speed": 2, #2
        "pattern": "default"
    },
    {
        "rows": 1, #4
        "columns": 1, #9
         "invader_speed": 3,
        "pattern": "zigzag"
    },
    {
        "rows": 1, #7
        "columns": 1, #13
        "invader_speed": 1.2,
        "pattern": "dense"
    },
    {
        "rows": 5, #6
        "columns": 10, #11
        "invader_speed": 2.5,
        "pattern": "semicircle"
    }
    # Add more levels as needed
]
