import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FONT_SIZE = 72
BACKGROUND_COLOR = (255, 255, 255)  # White background
SQUARE_COLOR = (200, 200, 200)  # Color of the squares
NUMBERS_TO_SHOW = 5  # Number of digits to display

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chimp Memory Test")

# Font setup
font = pygame.font.Font(None, FONT_SIZE)

def draw_numbers(numbers, revealed_indices=None):
    screen.fill(BACKGROUND_COLOR)  # Fill background
    for i in range(9):
        x = (i % 3) * (SCREEN_WIDTH // 3) + (SCREEN_WIDTH // 6)
        y = (i // 3) * (SCREEN_HEIGHT // 3) + (SCREEN_HEIGHT // 6)
        if revealed_indices and i in revealed_indices:
            text = font.render(str(numbers[i]), True, (0, 0, 0))  # Black text for revealed numbers
        else:
            pygame.draw.rect(screen, SQUARE_COLOR, (x - 50, y - 50, 100, 100))  # Draw square
            text = font.render("", True, (0, 0, 0))  # Empty text for covered numbers
        text_rect = text.get_rect(center=(x, y))
        screen.blit(text, text_rect)
    pygame.display.flip()

def main():
    # Create a list of numbers to remember
    numbers = random.sample(range(1, 10), 9)  # Unique numbers from 1 to 9
    sequence = random.sample(numbers, NUMBERS_TO_SHOW)  # Select a sequence to show
    revealed_indices = []   # Indices of revealed numbers

    # Show numbers for memorization
    draw_numbers(numbers)
    for i in range(NUMBERS_TO_SHOW):
        time.sleep(1)  # Display each number for 1 second
        draw_numbers(numbers, revealed_indices=[numbers.index(sequence[i])])
    
    # Clear the screen for input
    time.sleep(1)
    draw_numbers(numbers)  # Show all numbers covered

    # Game loop
    current_index = 0  # Track the current index of the sequence
    running = True
    while running:
        draw_numbers(numbers, revealed_indices)  # Draw the current state

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Get mouse position
                mouse_x, mouse_y = event.pos
                # Check if a number was clicked
                for i in range(9):
                    x = (i % 3) * (SCREEN_WIDTH // 3) + (SCREEN_WIDTH // 6)
                    y = (i // 3) * (SCREEN_HEIGHT // 3) + (SCREEN_HEIGHT // 6)
                    text_rect = pygame.Rect(x - 50, y - 50, 100, 100)
                    if text_rect.collidepoint(mouse_x, mouse_y):
                        if numbers[i] == sequence[current_index]:  # Correct number clicked
                            revealed_indices.append(i)
                            current_index += 1
                            if current_index >= len(sequence):  # All numbers correctly clicked
                                running = False
                        else:  # Wrong number clicked
                            print("Game Over! You clicked the wrong number.")
                            running = False
                        break

    # Game over message
    screen.fill(BACKGROUND_COLOR)
    if current_index == len(sequence):
        message = "You completed the sequence!"
    else:
        message = "Game Over! You clicked the wrong number."
    text = font.render(message, True, (0, 0, 0))
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()

if __name__ == "__main__":
    main()
