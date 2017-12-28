# This is nothing but a small little template!!!a


import pygame

pygame.init()

# Let's define some colors here.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (46, 133, 204)
RED = (244, 23, 23)
GREEN = (172, 231, 55)
PURPLE = (138, 49, 238)

# Open and set the window size.
size = (700, 500)
screen = pygame.display.set_mode(size)

# Set the window title.
pygame.display.set_caption("Control a ball... To start!")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop ----------- #
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

    # --- Game logic should go here

    # --- Drawing code should go here

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)
