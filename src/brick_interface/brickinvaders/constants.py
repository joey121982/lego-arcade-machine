# Constants for Brick Invaders game

# Spaceship settings
SPACESHIP_SPEED = 10
SPACESHIP_ACCELERATION = 0.6
SPACESHIP_FRICTION = 0.4
SPACESHIP_VELOCITY_LIMIT = 15
SPACESHIP_COUNTER_STRAFE_MULTIPLIER = 2
SPACESHIP_ANGLE_INCREMENT = 5

# Bullet settings
BULLET_SPEED = 10
BULLET_WIDTH = 20
BULLET_HEIGHT = 20
BULLET_COLOR = (255, 255, 0)

# Invader settings
INVADER_ROWS = 5
INVADER_COLUMNS = 11
INVADER_START_X = 200
INVADER_START_Y = 50
INVADER_SPEED = 2

# Colors
COLOR_RED = (255, 0, 0)
COLOR_YELLOW = (255, 255, 0)
COLOR_WHITE = (255, 255, 255)

# Level definitions
LEVELS = [
    {
        "rows": 5,
        "columns": 11,
        "invader_speed": 2,
        "pattern": "default"
    },
    {
        "rows": 6,
        "columns": 13,
        "invader_speed": 3,
        "pattern": "zigzag"
    },
    # Add more levels as needed
]
