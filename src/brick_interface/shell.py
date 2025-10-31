# --- info
# shell-ul e doar un fel de "wrapper" pentru restul jocurilor
# fiecare joc deschis se afla in interiorul shellului
# ca sa putem trece usor de la meniu la unul din jocuri si inapoi.
# --- joey

import pygame

from .menu.menu import *
from .brickjump.game import *
from .brickinvaders.game import *
from .brickman.game import *
from .bricktetris.game import *
from .highscores import *

GameType = Brickjump | Brickinvaders | Bricktetris | Brickman | Menu | None

class Shell:
    def parse_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if self.game and hasattr(self.game, 'handle_event'):
                self.game.handle_event(event)

    def __init__(self, new_screen, new_globals):
        self.screen = new_screen
        self.glb = new_globals
        self.game = Menu(self.screen, self.glb)

    def _prompt_for_name(self, max_length: int = 3) -> str:
        font_path = "./assets/fonts/Pixellettersfull-BnJ5.ttf"
        try:
            prompt_font = pygame.font.Font(font_path, 72)
            letter_font = pygame.font.Font(font_path, 140)
            info_font = pygame.font.Font(font_path, 28)
        except Exception:
            prompt_font = pygame.font.SysFont(None, 72)
            letter_font = pygame.font.SysFont(None, 140)
            info_font = pygame.font.SysFont(None, 28)

        prompt = "New Highscore! Choose 3 letters"
        name = ["A"] * max_length
        idx = 0
        clock = pygame.time.Clock()
        active = True

        while active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return ""
                    elif event.key == pygame.K_SPACE:
                        # advance; if last position, finish
                        if idx < max_length - 1:
                            idx += 1
                        else:
                            active = False
                            break
                    elif event.key == pygame.K_BACKSPACE:
                        if idx > 0:
                            idx -= 1
                            name[idx] = "A"
                    elif event.key == pygame.K_w:
                        # increment letter at idx
                        ch = name[idx]
                        if len(ch) != 1 or not ch.isalpha():
                            ch = "A"
                        code = ord(ch.upper()) - ord("A")
                        code = (code + 1) % 26
                        name[idx] = chr(ord("A") + code)
                    elif event.key == pygame.K_s:
                        # decrement letter at idx
                        ch = name[idx]
                        if len(ch) != 1 or not ch.isalpha():
                            ch = "A"
                        code = ord(ch.upper()) - ord("A")
                        code = (code - 1) % 26
                        name[idx] = chr(ord("A") + code)

            self.screen.fill((0, 0, 0))
            prompt_surf = prompt_font.render(prompt, True, (255, 255, 255))
            self.screen.blit(prompt_surf, (self.glb.WINWIDTH // 2 - prompt_surf.get_width() // 2, self.glb.WINHEIGHT // 2 - 120))

            total_w = 0
            letter_surfs = []
            for ch in name:
                s = letter_font.render(ch, True, (255, 255, 255))
                letter_surfs.append(s)
                total_w += s.get_width() + 20
            start_x = self.glb.WINWIDTH // 2 - total_w // 2

            x = start_x
            for i, s in enumerate(letter_surfs):
                rect = s.get_rect(topleft=(x, self.glb.WINHEIGHT // 2 - 20))
                self.screen.blit(s, rect)
                if i == idx:
                    pygame.draw.rect(self.screen, (255, 200, 0), (rect.x - 8, rect.y + rect.height + 8, rect.width + 16, 8))
                x += s.get_width() + 20

            info = info_font.render("Use UP/DOWN to change letter, SPACE to confirm, BACKSPACE to go back", True, (200, 200, 200))
            self.screen.blit(info, (self.glb.WINWIDTH // 2 - info.get_width() // 2, self.glb.WINHEIGHT // 2 + 140))

            pygame.display.flip()
            clock.tick(30)

        return "".join(name).strip()

    def update(self):
        if not self.game:
            return
        
        if self.game.running:
            self.game.update()
        
        if hasattr(self.glb, 'return_to_menu') and self.glb.return_to_menu:
            print("Returning to menu...")

            # try to save highscore for the current game
            try:
                score = 0
                if hasattr(self.game, 'score'):
                    s = getattr(self.game, 'score')
                    if isinstance(s, int):
                        score = s
                    elif hasattr(s, 'value'):
                        try:
                            score = int(s.value)
                        except Exception:
                            score = 0
                elif hasattr(self.game, 'playable_screen') and hasattr(self.game.playable_screen, 'score'):
                    try:
                        score = int(self.game.playable_screen.score)
                    except Exception:
                        score = 0
                elif hasattr(self.game, 'score_value'):
                    try:
                        score = int(self.game.score_value)
                    except Exception:
                        score = 0

                game_name = getattr(self.game, 'name', 'Unknown')
                saved, needs_name = update_highscore(game_name, score)
                if needs_name:
                    name = self._prompt_for_name()
                    if name:
                        update_highscore(game_name, score, name)
            except Exception as e:
                print('Highscore save failed:', e)

            self.game.running = False

            self.screen.fill((0, 0, 0))
            pygame.display.flip()       

            self.glb.return_to_menu = False 
            self.game = Menu(self.screen, self.glb)
            return
        
        if not isinstance(self.game, Menu) and not self.game.running:
            try:
                score = 0
                if hasattr(self.game, 'score'):
                    s = getattr(self.game, 'score')
                    if isinstance(s, int):
                        score = s
                    elif hasattr(s, 'value'):
                        try:
                            score = int(s.value)
                        except Exception:
                            score = 0
                elif hasattr(self.game, 'playable_screen') and hasattr(self.game.playable_screen, 'score'):
                    try:
                        score = int(self.game.playable_screen.score)
                    except Exception:
                        score = 0
                elif hasattr(self.game, 'score_value'):
                    try:
                        score = int(self.game.score_value)
                    except Exception:
                        score = 0

                game_name = getattr(self.game, 'name', 'Unknown')
                saved, needs_name = update_highscore(game_name, score)
                if needs_name:
                    name = self._prompt_for_name()
                    if name:
                        update_highscore(game_name, score, name)
            except Exception as e:
                print('Highscore save failed:', e)

            self.screen.fill((0, 0, 0))
            pygame.display.flip()
            self.game = Menu(self.screen, self.glb)
            return
        
            
        if isinstance(self.game, Menu) and self.game.new_game != "None":
            ngame = self.game.new_game
            if ngame == "Brick Invaders":
                self.game = Brickinvaders(self.screen, self.glb)
                return
            if ngame == "Brick Jump":
                self.game = Brickjump(self.screen, self.glb)
                return
            if ngame == "Brick Man":
                self.game = Brickman(self.screen, self.glb)
                return
            if ngame == "Brick Tetris":
                self.game = Bricktetris(self.screen, self.glb)
                return
