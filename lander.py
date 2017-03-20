import pygame
import math

#Import my created classes for the game
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

# Define in-game font-sizes

telemetry_font_size = 20

# Open a new window and set the window size
x_window_size = 500
y_window_size = 500

size = (x_window_size, y_window_size)
screen = pygame.display.set_mode(size)

# Set the window title

pygame.display.set_caption("Lunar Lander")

# Now let us set up the main program loop

# Loop until the user clicks the close button

done = False

# This is used to manage how fast the screen updates

clock = pygame.time.Clock()

# Initialize game logic variables

# Initialize position, velocity, acceleration and rotation variables
x_pos = 5
y_pos = 5

x_velocity = 0
x_acceleration = 1


y_velocity = 0
y_acceleration = 1

rotation = 0


# Initialize engine variables

engine_acceleration = -1*y_acceleration

# Define game logic flags

engine_firing_flag = False
end_game_flag = False

rotate_left_flag = False
rotate_right_flag = False

# Some math functions that we'll need later on
#
# math.cos(math.radians(angle_in_degrees))

#Create new lunar lander object
lander = mymodule.Lander(x_pos,y_pos, x_velocity, y_velocity, x_acceleration, y_acceleration, engine_acceleration, screen, x_window_size, y_window_size)



# ------------ Main Program Loop -----------
while not done:
	# ---- Main event loop

	# This is the main event loop. Keep all of your code in here.
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			print("User asked to quit")
			done = True # Flag as done so we exit this loop
		elif event.type == pygame.KEYDOWN:
			# Check for key lefts, rights, etc
			if event.key == pygame.K_LEFT:
				rotate_left_flag = True
			if event.key == pygame.K_RIGHT:
				rotate_right_flag = True
			if event.key == pygame.K_DOWN:
				engine_firing_flag = True
				print("Started firing")
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_DOWN:
				engine_firing_flag = False
				print("Stopped firing")
			if event.key == pygame.K_LEFT:
				rotate_left_flag = False
			if event.key == pygame.K_RIGHT:
				rotate_right_flag = False

	# --- Game logic should go here

	# Add rotation of the lander

	if rotate_left_flag:
		rotation += 2
	if rotate_right_flag:
		rotation -= 2
	lander.rot_center(rotation)


	# Drawing code should go here

	# First, clear the screen to go white. Don't put other drawing
	# commmands above this, or they will be erased with this command.
	screen.fill(BLACK)

	# Draw telemetry data inside the game window
	font = pygame.font.SysFont('Calibri', telemetry_font_size, True, False)
	x_velocity_text = font.render("x velocity: " + str(lander.x_velocity), True, WHITE)
	y_velocity_text = font.render("y velocity: " + str(-1*lander.y_velocity), True, WHITE)

	x_velocity_text_rect = x_velocity_text.get_rect(center=(x_window_size*4/5, y_window_size/5))
	y_velocity_text_rect = y_velocity_text.get_rect(center=(x_window_size*4/5, y_window_size/5 + telemetry_font_size))

	screen.blit(x_velocity_text, x_velocity_text_rect)
	screen.blit(y_velocity_text, y_velocity_text_rect)

	# Draw the lander, and move it, and check if the lander experienced a collision.
	# It will return True if it collided with something.

	lander.draw(WHITE)

	end_game_flag = lander.move(engine_firing_flag)

	if end_game_flag:
		print("Game over")
		game_over_text = font.render("Game Over", True, WHITE)
		game_over_text_rect = game_over_text.get_rect(center=(x_window_size*2, y_window_size/2))
		screen.blit(game_over_text, game_over_text_rect)

	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

	# --- Limit to 60 frames per second.
	clock.tick(15)

# Properly shutdown the program

pygame.quit()
