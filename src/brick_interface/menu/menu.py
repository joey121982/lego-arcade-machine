import pygame
from ..highscores import get_highscores

class Menu:
    name = "Menu"
    new_game = "None"
    running = True
    up = True
    left = True
    selected_item = 0   # 0 to 3 values (inclusive)

    def __init__(self, new_screen, new_globals):
        self.screen = new_screen
        self.glb = new_globals
        self.background = pygame.image.load("././assets/menu/images/bg.png")
        self.background = pygame.transform.scale(self.background, (self.glb.WINWIDTH, self.glb.WINHEIGHT))

    def controls(self):
        # --- todo
        # replace with gpio pins from physical buttons
        # (maybe also keep these for debugging)
        # --- joey

        keys = pygame.key.get_pressed()
        state = {
            'w': keys[pygame.K_w],
            'a': keys[pygame.K_a],
            's': keys[pygame.K_s],
            'd': keys[pygame.K_d],
            'space': keys[pygame.K_SPACE]
        }
        
        if state['w']:
            self.up = True
        if state['a']:
            self.left = True
        if state['s']:
            self.up = False
        if state['d']:
            self.left = False

        if self.up and self.left:
            self.selected_item = 0
        elif self.up and not self.left:
            self.selected_item = 1
        elif not self.up and self.left:
            self.selected_item = 2
        elif not self.up and not self.left:
            self.selected_item = 3

        if state['space']:
            self.change_game()

    def change_game(self):
        match self.selected_item:
            case 0:
                self.new_game = "Brick Man"
            case 1:
                self.new_game = "Brick Tetris"
            case 2:
                self.new_game = "Brick Invaders"
            case 3:
                self.new_game = "Brick Jump"
        
        print("Changing game to " + self.new_game + "...")
        self.running = False

    def update(self):
        if not self.screen:
            print("No screen at Menu.update()... Check for errors.")
            return
        
        if not self.background:
            print("Background not loaded at Menu.update()... Check for errors.")
            return
        
        if not self.glb:
            print("Global parameters not loaded at Menu.update()... Check for errors.")
        
        selected_color = (255, 150, 0) # orangey colour
        unselected_color = (50, 50, 50) # grey
        grid_item_height = 270
        grid_item_width = 480
        padding_size_horz = 300
        padding_size_vert = padding_size_horz * 0.55

        # --- info
        # we calculate the exact positions here for the game icons in a grid layout
        # so we can then use these to draw selected/unselected outlines and
        # know where the actual game icon is located.
        #
        # order is: 1 = top-left (Brick Man), 2 = top-right (Brick Fighter), 
        #           3 = bottom-left (Brick Invaders), 4 = bottom-right (Brick Jump)
        #
        # p.s. its just math
        # --- joey
        game_positions = [
            [(self.glb.WINWIDTH - padding_size_horz) / 2 - grid_item_width, (self.glb.WINHEIGHT - padding_size_vert) / 2 - grid_item_height],
            [(self.glb.WINWIDTH + padding_size_horz) / 2, (self.glb.WINHEIGHT - padding_size_vert) / 2 - grid_item_height],
            [(self.glb.WINWIDTH - padding_size_horz) / 2 - grid_item_width, (self.glb.WINHEIGHT + padding_size_vert) / 2],
            [(self.glb.WINWIDTH + padding_size_horz) / 2, (self.glb.WINHEIGHT + padding_size_vert) / 2]
        ]
        
        # Title mapping for each grid item (index -> game name)
        titles = ["Brick Man", "Brick Tetris", "Brick Invaders", "Brick Jump"]

        # draw menu tiles and highscores (ignore Brick Man for highscores)
        font_path = "././assets/fonts/Pixellettersfull-BnJ5.ttf"
        title_font = pygame.font.Font(font_path, 36)
        hs_font = pygame.font.Font(font_path, 24)
        for i in range(0, 4):
            color = selected_color if self.selected_item == i else unselected_color
            pos = game_positions[i]
            rect_x, rect_y = pos[0], pos[1]
            pygame.draw.rect(self.screen, color, pygame.Rect(rect_x, rect_y, grid_item_width, grid_item_height))

            # draw the game title in the tile
            title_surf = title_font.render(titles[i], True, (255, 255, 255))
            self.screen.blit(title_surf, (rect_x + 12, rect_y + 12))

            # show top-3 highscores for Brick Tetris, Brick Invaders, Brick Jump
            if i != 0:  # ignore Brick Man
                try:
                    hs_list = get_highscores(titles[i])
                except Exception:
                    hs_list = []
                # draw up to top 3 entries under each tile
                start_y = rect_y + grid_item_height + 8
                for rank in range(3):
                    if rank < len(hs_list):
                        entry = hs_list[rank]
                        name = entry.get("name", "ANON")
                        score = entry.get("score", 0)
                        line = f"{rank+1}. {name} - {score}"
                    else:
                        line = f"{rank+1}. ---"
                    line_surf = hs_font.render(line, True, (220, 220, 220))
                    self.screen.blit(line_surf, (rect_x + 12, start_y + rank * 20))

        pygame.display.update()
        self.controls()