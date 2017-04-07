import pygame
import math

pygame.init()

#Define some colors to use in our game
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED =   ( 255, 0, 0)
BLUE =  (0, 0, 255)
#Define some constants that we will need
PI = 3.141592653

# Define in-game font-sizes

# Open a new window and set the window size
x_window_size = 500
y_window_size = 500

size = (x_window_size, y_window_size)
screen = pygame.display.set_mode(size)

# Set the window title

pygame.display.set_caption("This is a test.")

# Now let us set up the main program loop

# Loop until the user clicks the close button

done = False

# This is used to manage how fast the screen updates

clock = pygame.time.Clock()

# Initialize game logic variables

# ------------ Main Program Loop -----------
while not done:
	# ---- Main event loop

	# This is the main event loop. Keep all of your code in here.
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			print("User asked to quit")
			done = True # Flag as done so we exit this loop

	#  --- Game logic should go here

	# Add rotation of the lander

	# Drawing code should go here

	# First, clear the screen to go black. Don't put other drawing
	# commmands above this, or they will be erased with this command.
	screen.fill(BLACK)

	# Draw a ball to use as our test object.
	pygame.draw.circle(screen, RED, (100,100), 10)

	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

	# --- Limit to 60 frames per second.
	clock.tick(15)

# Properly shutdown the program

pygame.quit()
