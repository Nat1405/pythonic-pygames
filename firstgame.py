import pygame
import math

#Import my classes for the game
import mymodule

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
y_window_size = 700

size = (x_window_size, y_window_size)
screen = pygame.display.set_mode(size)

# Set the window title

pygame.display.set_caption("A pretty cool python game!")

# Now let us set up the main program loop

# Loop until the user clicks the close button

done = False

# This is used to manage how fast the screen updates

clock = pygame.time.Clock()

# Initialize game logic variables
size_grid = 10

x_pos = x_window_size/2
y_pos = y_window_size/2

x_velocity = 10
x_velocity_increment = 5
x_direction_movement = 1

y_velocity = 0
y_velocity_increment = 5
y_direction_movement = 1

#Create new box objects
box_2 = mymodule.Box(x_pos,y_pos,screen, x_window_size, y_window_size)



# ------------ Main Program Loop -----------
while not done:
	# ---- Main event loop

	# Migrate this code into the Box() object
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			print("User asked to quit")
			done = True # Flag as done so we exit this loop
		elif event.type == pygame.KEYDOWN:
			# Check for key lefts, rights, etc
			if event.key == pygame.K_RIGHT:
				box_2.accelerate_x();
			if event.key == pygame.K_LEFT:
				box_2.deccelerate_x();
			if event.key == pygame.K_DOWN:
				box_2.accelerate_y();
			if event.key == pygame.K_UP:
				box_2.deccelerate_y();
			# Check for integers. This controls acceleration increment.
			if event.key == pygame.K_0:
				x_velocity_increment = 0
			if event.key == pygame.K_1:
				x_velocity_increment = 1
			if event.key == pygame.K_2:
				x_velocity_increment = 2
			if event.key == pygame.K_3:
				x_velocity_increment = 5
			if event.key == pygame.K_4:
				x_velocity_increment = 10
			box_2.set_x_increment(x_velocity_increment)
			# Check from 6 till 8 for y velocities
			if event.key == pygame.K_6:
				y_velocity_increment = 0
			if event.key == pygame.K_7:
				y_velocity_increment = 1
			if event.key == pygame.K_8:
				y_velocity_increment = 2
			if event.key == pygame.K_9:
				y_velocity_increment = 5
			box_2.set_y_increment(y_velocity_increment)

		elif event.type == pygame.MOUSEBUTTONDOWN:
			print("User pressed a mouse button")

	# --- Game logic should go here

	# Drawing code should go here

	# First, clear the screen to go white. Don't put other drawing
	# commmands above this, or they will be erased with this command.
	screen.fill(BLACK)

	# Draw a title INSIDE the game window
	font = pygame.font.SysFont('Calibri', 50, True, False)
	text = font.render(mymodule.game_title, True, WHITE)
	screen.blit(text, [40, int((1.0/3)*(y_window_size))])

	#Update the instance variables of the box_2 object

	box_2.draw(size_grid, WHITE)
	box_2.move()
	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

	# --- Limit to 60 frames per second.
	clock.tick(60)

# Properly shutdown the program

pygame.quit()
