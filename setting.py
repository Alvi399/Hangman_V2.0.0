import pygame

# Initialize Pygame
pygame.init()

#set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pygame Example')

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up game variables
x, y = 150, 150
velocity = 1    

# Main game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= velocity
    if keys[pygame.K_RIGHT]:
        x += velocity
    if keys[pygame.K_UP]:
        y -= velocity
    if keys[pygame.K_DOWN]:
        y += velocity
    if keys[pygame.K_ESCAPE]:
        x = 150
        y = 150
    # Fill the background with white
    window.fill(white)

    # Draw a black rectangle
    pygame.draw.rect(window, black, (x, y, 100, 50))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

#sys.exit()