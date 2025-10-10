import pygame

# screen settings
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCROLL = 200
HOVER = SCROLL // 10
FPS = 60

# playable area stretch
STRETCH = 100

# container area
CONTAINER_AREA_TOP_X = SCREEN_WIDTH // 3 - STRETCH
CONTAINER_AREA_TOP_Y = 0

# background settings
BACKGROUND_WIDTH_TOTAL = SCREEN_WIDTH // 3 + STRETCH * 2
PILLAR_WIDTH = 200
PILLAR_HEIGHT = SCREEN_HEIGHT - 390
PLAYABLE_AREA_WIDTH = BACKGROUND_WIDTH_TOTAL - (2 * PILLAR_WIDTH)

# platform settings
ON_SCREEN_NUMBER_OF_PLATFORMS = 5
PLATFORM_WIDTH = 160
PLATFORM_HEIGHT = 30
PLATFORM_INIT_Y = SCREEN_HEIGHT - 150
LEFT_PLATFORM_X = CONTAINER_AREA_TOP_X + PILLAR_WIDTH
RIGHT_PLATFORM_X = CONTAINER_AREA_TOP_X + PILLAR_WIDTH + PLAYABLE_AREA_WIDTH - PLATFORM_WIDTH
PLATFORM_Y_GAP = SCROLL
UPPER_PLATFORM_Y = PLATFORM_INIT_Y - (ON_SCREEN_NUMBER_OF_PLATFORMS - 1) * PLATFORM_Y_GAP
SHAKE_INTENSITIY = 3
INIT_PLATFORM_SHAKE_DURATION = 1000
MIN_PLATFORM_SHAKE_DURATION = 200
GROUND_FORGIVENESS = 20  # pixels before landing
PLATFORM_DRAW_OFFSET_X = 20  # pixels to offset platform drawing for better visual alignment

# player
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_ON_LEFT_PLATFORM_X = LEFT_PLATFORM_X + PLATFORM_WIDTH // 2 - PLAYER_WIDTH // 2 - PLATFORM_DRAW_OFFSET_X
PLAYER_ON_RIGHT_PLATFORM_X = RIGHT_PLATFORM_X + PLATFORM_WIDTH // 2 - PLAYER_WIDTH // 2 + PLATFORM_DRAW_OFFSET_X

# colors
SKY_BLUE = (135, 206, 235)
UNDERGROUND_BROWN = (139, 69, 19)
FOREST_GREEN = (34, 139, 34)

# TINTS
TINTS = [
    (0, 255, 0, 100),    # green
    (255, 0, 0, 100),    # red
    (128, 0, 128, 100),  # purple
    (0, 0, 255, 100),    # blue
    (255, 255, 0, 100)   # yellow
]

def load_game_images():
    bunny_images = [
        pygame.transform.scale(
            pygame.image.load('./assets/brickjump/images/bunny_left.png').convert_alpha(),
            (PLAYER_WIDTH, PLAYER_HEIGHT)
        ),
        pygame.transform.scale(
            pygame.image.load('./assets/brickjump/images/bunny_right.png').convert_alpha(),
            (PLAYER_WIDTH, PLAYER_HEIGHT)
        ),
        pygame.transform.scale(
            pygame.image.load('./assets/brickjump/images/bunny_crouch_left.png').convert_alpha(),
            (PLAYER_WIDTH, PLAYER_HEIGHT)
        ),
        pygame.transform.scale(
            pygame.image.load('./assets/brickjump/images/bunny_crouch_right.png').convert_alpha(),
            (PLAYER_WIDTH, PLAYER_HEIGHT)
        )
    ]
    background = pygame.transform.scale(
        pygame.image.load('./assets/brickjump/images/background.png').convert(),
        (SCREEN_WIDTH, SCREEN_HEIGHT)
    )

    return bunny_images, background

def load_level_images():
    green_platform = pygame.transform.scale(
            pygame.image.load('./assets/brickjump/images/green_platform.png').convert_alpha(),
            (PLATFORM_WIDTH, PLATFORM_HEIGHT)
        )
    
    red_platform = pygame.transform.scale(
            pygame.image.load('./assets/brickjump/images/red_platform.png').convert_alpha(),
            (PLATFORM_WIDTH, PLATFORM_HEIGHT)
    )
    purple_platform = pygame.transform.scale(
            pygame.image.load('./assets/brickjump/images/purple_platform.png').convert_alpha(),
            (PLATFORM_WIDTH, PLATFORM_HEIGHT)
    )
    blue_platform = pygame.transform.scale(
            pygame.image.load('./assets/brickjump/images/blue_platform.png').convert_alpha(),
            (PLATFORM_WIDTH, PLATFORM_HEIGHT)
    )
    yellow_platform = pygame.transform.scale(
            pygame.image.load('./assets/brickjump/images/yellow_platform.png').convert_alpha(),
            (PLATFORM_WIDTH, PLATFORM_HEIGHT)
    )

    platforms = [
        green_platform,
        red_platform,
        purple_platform,
        blue_platform,
        yellow_platform
    ]
    green_pillar = pygame.transform.scale(
            pygame.image.load('./assets/brickjump/images/green_pillar.png').convert_alpha(),
            (PILLAR_WIDTH, PILLAR_HEIGHT)
        )
    red_pillar = pygame.transform.scale(
            pygame.image.load('./assets/brickjump/images/red_pillar.png').convert_alpha(),
            (PILLAR_WIDTH, PILLAR_HEIGHT)
        )
    purple_pillar = pygame.transform.scale(
            pygame.image.load('./assets/brickjump/images/purple_pillar.png').convert_alpha(),
            (PILLAR_WIDTH, PILLAR_HEIGHT)
        )
    blue_pillar = pygame.transform.scale(
            pygame.image.load('./assets/brickjump/images/blue_pillar.png').convert_alpha(),
            (PILLAR_WIDTH, PILLAR_HEIGHT)
        )
    yellow_pillar = pygame.transform.scale(
            pygame.image.load('./assets/brickjump/images/yellow_pillar.png').convert_alpha(),
            (PILLAR_WIDTH, PILLAR_HEIGHT)
        )
    
    pillars = [
        green_pillar,
        red_pillar,
        purple_pillar,
        blue_pillar,
        yellow_pillar
    ]
    return platforms, pillars