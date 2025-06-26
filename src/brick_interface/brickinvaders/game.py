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
        self.spaceship_y = self.screen.get_height() - 200

        self.spaceship_speed = 10
    
    def handle_event(self, event):
        

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Space key pressed in Brick Invaders!")
                self.spaceship.fill((0, 255, 0))  # Change color on space key press
            

    def update(self):
        print("Updating Brick Invaders...")

        # Update spaceship position
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.spaceship_x -= self.spaceship_speed
            if self.spaceship_x <= 50:
                self.spaceship_x = 50
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.spaceship_x += self.spaceship_speed
            if self.spaceship_x > self.screen.get_width() - 150:
                self.spaceship_x = self.screen.get_width() - 150



        self.screen.fill((0, 0, 0))
        self.screen.blit(self.spaceship, (self.spaceship_x, self.spaceship_y))
        pygame.display.flip()