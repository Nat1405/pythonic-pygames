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

# Open a new window and set the window size
x_window_size = 700
y_window_size = 500


size = (x_window_size, y_window_size)
screen = pygame.display.set_mode(size)

# Set the window title

pygame.display.set_caption("My Super Mega Awesome Pygame")

# Now let us set up the main program loop

# Loop until the user clicks the close button

done = False

# This is used to manage how fast the screen updates

clock = pygame.time.Clock()

# Initialize game logic variables
size_grid = 10
x_pos = x_window_size/2
y_pos = y_window_size/2

pos_increment = 10

# ------------ Main Program Loop -----------
while not done:
	# ---- Main event loop
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			print("User asked to quit")
			done = True # Flag as done so we exit this loop
		elif event.type == pygame.KEYDOWN:
			pos_increment -= 5
			print("Speed decreased by five units")
		elif event.type == pygame.KEYUP:
			pos_increment += 5
			print("Speed increased by five units")
		elif event.type == pygame.MOUSEBUTTONDOWN:
			print("User pressed a mouse button")	

	# --- Game logic should go here
	# Update position variables of the block
	if x_pos < x_window_size and x_pos > 0:
		x_pos += pos_increment
	else:
		pos_increment *= -1
		x_pos += pos_increment
	# Drawing code should go here
	
	# First, clear the screen to go white. Don't put other drawing
	# commmands above this, or they will be erased with this command.
	screen.fill(WHITE)
	
	#draw some text
	font = pygame.font.SysFont('Calibri', 50, True, False)
	text = font.render("WELCOME TO MY GAME", True, BLACK)
	screen.blit(text, [50, int((1.0/3)*(y_window_size))])
	
	#draw a rectangular grid
	for i in range(size_grid):
		for k in range(size_grid):
			pygame.draw.rect(screen, RED, (x_pos,y_pos,10,10))
			
	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

	# --- Limit to 60 frames per second.
	clock.tick(60)

# Properly shutdown the program

pygame.quit()
