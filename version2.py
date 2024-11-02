import pygame
import sys

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
GRAVITY = 0.5
JUMP_STRENGTH = 15
PLAYER_WIDTH = 30
PLAYER_HEIGHT = 60

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jump King Inspired Game")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Player class
class Player:
    def __init__(self):
        self.rect = pygame.Rect(100, SCREEN_HEIGHT - 150, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.velocity_y = 0
        self.jumping = False
        self.jump_time = 0  # To control jump duration

    def update(self):
        # Apply gravity
        if self.rect.bottom < SCREEN_HEIGHT:
            self.velocity_y += GRAVITY
        else:
            self.velocity_y = 0
            self.rect.bottom = SCREEN_HEIGHT  # Prevent falling through the ground

        self.rect.y += self.velocity_y

        # Check for landing
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.jumping = False

    def jump(self):
        if not self.jumping:
            self.jumping = True
            self.jump_time = JUMP_STRENGTH
            self.velocity_y = -JUMP_STRENGTH

    def hold_jump(self):
        if self.jumping and self.jump_time > 0:
            self.jump_time -= 1
            self.velocity_y = -JUMP_STRENGTH * (self.jump_time / JUMP_STRENGTH)

# Main game loop
def main():
    player = Player()
    running = True

    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if not player.jumping:
                player.jump()
            else:
                player.hold_jump()

        # Update player and draw
        player.update()
        pygame.draw.rect(screen, BLUE, player.rect)

        # Displaying the ground
        pygame.draw.rect(screen, GREEN, (0, SCREEN_HEIGHT - 10, SCREEN_WIDTH, 10))

        # Refresh the display
        pygame.display.flip()
        clock.tick(FPS)

# Run the game
if __name__ == "__main__":
    main()
