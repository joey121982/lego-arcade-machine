Brick Tetris

Brick Tetris is a classic falling-block puzzle game, part of the LEGO Arcade Machine project.  
This folder contains the game logic and UI for the Brick Tetris game.

Folder Structure

bricktetris/
│
├── game.py           # Main game loop and state management
├── screens.py        # UI screens (menu, info, pause)
├── assets/           # Game-specific assets
└── README.md         # This documentation

Main Modules and Classes

--- game.py
Main entrypoint for Brick Tetris. Responsible for the game state, input handling, piece spawning, collision/line checks and rendering.

- Key responsibilities:
  - Holding the active board, current piece, next piece, score and level.
  - Handling player input (move left/right, rotate, soft/hard drop).
  - Running the main update loop and drawing frames.

Referenced functions/methods:
- [Bricktetris.update] main per-frame update and render function.

--- `screens.py
UI layer for non-gameplay screens: info, pause, game over and HUD.

- Notable symbol:
  - [InfoScreen.draw] — draws the info/HUD area (font loading and layout live here; ensure asset paths are correct).

--- assets
Contains sprites, fonts and other media used by Brick Tetris.

How the Game Works

- Pieces (Tetrominoes) spawn at the top of the board and fall at a rate determined by the current level.
- Player can move pieces left/right, rotate them, perform soft drops and hard drops.
- Filled rows are cleared, score/level is updated, and pieces above drop down.
- Game ends when a new piece cannot spawn because the spawn area is blocked.
- UI screens (pause, info, game over) are implemented in screens.py.

Controls

- Left / Right arrows (or A/D): Move piece horizontally.
- Up arrow (or W / X): Rotate piece.
- Down arrow: Soft drop.
- ESC: Pause / return to menu.

Getting Started

- The launcher loads Brick Tetris via the arcade shell; run the main launcher from project root:

```sh
make run
```