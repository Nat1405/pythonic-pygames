import pygame

pygame.init()

#Define some colors to use in our game
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED =   ( 255, 0, 0)
BLUE =  (0, 0, 255)
#Define some constants that we will need
PI = 3.141592653

# Open a new window and set the window size

size = (700, 500)
screen = pygame.display.set mode(size)

# Set the window title

pygame.display.set caption("My Super Mega Awesome Pygame")

# Now let us set up the main program loop

# Loop until the user clicks the close button

done = False

# This is used to manage how fast the screen updates

clock = pygame.time.Clock()

# ------------ Main Program Loop -----------
while not done:
	# ---- Main event loop
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			done = True # Flag as done so we exit this loop
	# --- Game logic should go here

	# Drawing code should go here
	
	# First, clear the screen to go white. Don't put other drawing
	# commmands above this, or they will be erased with this command.
	screen.fill(WHITE)

	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

	# --- Limit to 60 frames per second.
	clock.tick(60)
