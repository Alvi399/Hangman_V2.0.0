import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pygame Example')

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    window.fill(white)

    # Draw a black rectangle
    pygame.draw.rect(window, black, (150, 150, 100, 50))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()