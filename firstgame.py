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
			if event.key == pygame.K_RIGHT:
				x_velocity += x_velocity_increment
				print("X Speed decreased")
			if event.key == pygame.K_LEFT:
				x_velocity -= x_velocity_increment
				print("X Speed increased")
			if event.key == pygame.K_DOWN:
				y_velocity += y_velocity_increment
				print("Y Speed increased")
			if event.key == pygame.K_UP:
				y_velocity -= y_velocity_increment
				print("Y Speed decreased")

		elif event.type == pygame.KEYUP:
			#Placeholder?
			"pass"
		elif event.type == pygame.MOUSEBUTTONDOWN:
			print("User pressed a mouse button")

	# --- Game logic should go here
	# Update position variables of the block
	if x_pos < x_window_size and x_pos > 0:
		x_pos += x_velocity*x_direction_movement
	else:
		x_direction_movement *= -1
		x_pos += x_velocity*x_direction_movement

	if y_pos < y_window_size and y_pos > 0:
		y_pos += y_velocity*y_direction_movement
	else:
		y_direction_movement *= -1
		y_pos += y_velocity*y_direction_movement

	# Drawing code should go here

	# First, clear the screen to go white. Don't put other drawing
	# commmands above this, or they will be erased with this command.
	screen.fill(WHITE)

	#draw some text
	font = pygame.font.SysFont('Calibri', 50, True, False)
	text = font.render(mymodule.game_title, True, BLACK)
	screen.blit(text, [40, int((1.0/3)*(y_window_size))])

	#Update the instance variables of the box_2 object

	box_2.draw(size_grid)
	box_2.move()
	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

	# --- Limit to 60 frames per second.
	clock.tick(60)

# Properly shutdown the program

pygame.quit()
