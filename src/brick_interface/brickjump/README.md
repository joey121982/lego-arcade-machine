# Brick Jump

Brick Jump is a fast-paced arcade platformer game, part of the LEGO Arcade Machine project.  
This folder contains all the code and assets for the Brick Jump game.

## Folder Structure

brickjump/
│
├── __init__.py           # Package initialization
├── constants.py          # Game-wide constants and image loading
├── game.py               # Main game loop and state management
├── level.py              # Level generation and platform management
├── pillar.py             # Pillar sprite class and logic
├── platform.py           # Platform sprite class and logic
├── player.py             # Player sprite class and movement logic
├── utilities.py          # Helper functions for collisions, animations, etc.
└── README.md             # This documentation

## Main Modules and Classes

### `game.py`
**Brickjump**  
Main class for running the Brick Jump game.  
Handles game state, event processing, updating, and rendering.

- **Key Attributes:**
  - `screen`: The game display surface.
  - `glb`: Global settings and state.
  - `running`: Whether the game is active.
  - `score`: Current player score.
  - `level`: Level management object.
  - `player`: Player character object.
  - `background_image`: Dynamic background that changes color based on score.

- **Key Methods:**
  - `handle_event(event)`: Handles pygame events, including A/D key presses for movement and ESC for menu return.
  - `update()`: Updates game state, renders all elements, and manages game flow.

---

### `player.py`
**Player**  
Represents the player character (bunny) with smooth arc-based movement animations.

- **Constructor Arguments:**
  - `x`, `y`: Initial position coordinates.
  - `images`: List of player sprite images for different states.

- **Key Attributes:**
  - `velocity_x`, `velocity_y`: Movement velocities.
  - `on_ground`: Whether the player is currently on a platform.
  - `is_moving`: Whether the player is currently in an animated movement.
  - `arc_height`: Height of the jump arc animation.

- **Key Methods:**
  - `update(platforms)`: Updates player physics, animations, and collision detection.
  - `start_move_animation(target_x, target_y)`: Initiates smooth arc movement to target position.
  - `move_up()`, `move_left()`, `move_right()`: Direction-specific movement commands.
  - `calculate_arc_position(t)`: Calculates position along movement arc using easing functions.
  - `draw(screen)`: Renders the player at the correct animated position.

---

### `platform.py`
**Platform**  
Represents jumping platforms with shake effects when touched.

- **Key Attributes:**
  - `touched`: Whether the platform has been landed on.
  - `is_shaking`: Whether the platform is currently shaking.
  - `shake_duration`: How long the shake effect lasts.
  - `visual_offset_x`, `visual_offset_y`: Shake animation offsets.

---

### `level.py`
**Level**  
Manages platform and pillar generation, recycling, and visual updates.

- **Key Attributes:**
  - `platforms`: Sprite group containing all active platforms.
  - `pillars`: Sprite group containing boundary pillars.
  - `platform_images`, `pillar_images`: Lists of different colored sprites.

- **Key Methods:**
  - `create_initial_elements()`: Sets up starting platforms and boundary pillars.

---

### `pillar.py`
**Pillar**  
Represents the side boundary pillars that frame the playable area.

---

### `constants.py`
Defines constants and image loading functions for Brick Jump.

- **Key Functions:**
  - `load_game_images()`: Loads player sprites and background image all at once.
  - `load_level_images()`: Loads platform and pillar sprites in different colors.

---

### `utilities.py`
Helper functions for Brick Jump game mechanics.

- **Key Functions:**
  - `death_screen(self)`: Displays game over screen with score and restart option.
  - `check_player_below_screen(self)`: Detects when player falls off screen, triggering the end of the game.
  - `advance(self)`: Handles score progression and screen scrolling when player jumps up a platform
  - `platform_shake(self)`: Manages platform shake animation effects, and kills the platform further in.
  - `check_player_platform_collisions(player, platforms)`: Handles collision detection between player and platforms with forgiveness mechanics for smoother gameplay.

---

## How the Game Works

- The player controls a bunny character that must jump between left and right platforms.
- Movement uses smooth arc animations with easing functions for polished feel.
- The game continuously scrolls upward, requiring constant forward progress.
- Platforms shake when touched and disappear after a duration that decreases with score.
- Background colors and platform/pillar sprites change every 100 points for visual variety.
- The game ends if the player falls below the screen edge.
- Score increases with each successful platform jump.

## Controls

- **A Key**: Move left (or jump up if already on left platform)
- **D Key**: Move right (or jump up if already on right platform)  
- **ESC Key**: Return to main menu
