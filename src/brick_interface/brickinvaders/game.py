import pygame

class Brickinvaders:
    name = "Brick Invaders"
    running = True
    
    def __init__(self, screen, glb):
        self.running = True
        self.screen = screen
        self.glb = glb

        # Initialize spaceship
        self.spaceship = pygame.Surface((100, 100))
        self.spaceship.fill((255, 0, 0))

        self.spaceship_x = self.screen.get_width() // 2 - 50
        self.spaceship_y = self.screen.get_height() - 250

        self.spaceship_speed_initial = 10
        self.spaceship_speed = self.spaceship_speed_initial
        self.spaceship_speed_increment = 0.2
        self.spaceship_speed_limit = 30
    
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Space key pressed in Brick Invaders!")
                self.spaceship.fill((0, 255, 0))  # Change color on space key press
            if event.key == pygame.K_ESCAPE:
                print("Escape key pressed in Brick Invaders! Returning to menu...")
                self.running = False
                self.glb.return_to_menu = True  # Signal to return to menu
        if event.type == pygame.QUIT:
            print("Quit event received in Brick Invaders!")
            self.running = False
            

    def update_spaceship_position(self):
        # Update spaceship position
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.spaceship_x -= self.spaceship_speed
            if self.spaceship_speed < self.spaceship_speed_limit:
                self.spaceship_speed += self.spaceship_speed_increment
            if self.spaceship_x <= 50:
                self.spaceship_x = 50
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.spaceship_x += self.spaceship_speed
            if self.spaceship_speed < self.spaceship_speed_limit:
                self.spaceship_speed += self.spaceship_speed_increment
            if self.spaceship_x > self.screen.get_width() - 150:
                self.spaceship_x = self.screen.get_width() - 150
        if not keys[pygame.K_a] and not keys[pygame.K_d] and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            if self.spaceship_speed > self.spaceship_speed_initial:
                self.spaceship_speed -= self.spaceship_speed_increment

    def update(self):
        if not self.running:
            self.screen.fill((0, 0, 0))  # Clear the screen
            pygame.display.flip()       # Update the display
            return

        print("Updating Brick Invaders...")
        self.update_spaceship_position()
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.spaceship, (self.spaceship_x, self.spaceship_y))
        pygame.display.flip()