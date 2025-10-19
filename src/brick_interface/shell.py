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

    def _prompt_for_name(self, max_length: int = 12):
        font = pygame.font.Font(None, 36)
        prompt = "New Highscore! Enter name:"
        name = ""
        clock = pygame.time.Clock()
        active = True
        while active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        active = False
                        break
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < max_length:
                            name += event.unicode

            # draw prompt
            self.screen.fill((0, 0, 0))
            prompt_surf = font.render(prompt, True, (255, 255, 255))
            name_surf = font.render(name, True, (200, 200, 200))
            self.screen.blit(prompt_surf, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2))
            self.screen.blit(name_surf, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 50))
            pygame.display.flip()
            clock.tick(30)

        return name.strip()

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
