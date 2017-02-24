# This is a simple box object to move around the screen.

import pygame
game_title = "This is not a test"

class Box(object):

    def __init__(self, x_pos, y_pos, screen, x_window_size, y_window_size):
        self.x_pos = x_pos
        self.y_pos = y_pos

        self.x_velocity = 10
        self.x_velocity_increment = 5
        self.x_direction_movement = 1

        self.y_velocity = 0
        self.y_velocity_increment = 5
        self.y_direction_movement = 1

        # Define the screen and game window variables here
        self.screen = screen
        self.x_window_size = x_window_size
        self.y_window_size = y_window_size


    #Method to draw object
    def draw(self,size_grid, color):
    	pygame.draw.circle(self.screen, color, (self.x_pos, self.y_pos), 10)

    #Method to move object around
    def move(self):
        if self.x_pos < self.x_window_size and self.x_pos > 0:
    		self.x_pos += self.x_velocity*self.x_direction_movement
    	else:
    		self.x_direction_movement *= -1
    		self.x_pos += self.x_velocity*self.x_direction_movement

    	if self.y_pos < self.y_window_size and self.y_pos > 0:
    		self.y_pos += self.y_velocity*self.y_direction_movement
    	else:
    		self.y_direction_movement *= -1
    		self.y_pos += self.y_velocity*self.y_direction_movement

        self.x_pos += self.x_velocity*self.x_direction_movement
        self.y_pos += self.y_velocity*self.y_direction_movement

    # Call these methods to speed up or slow down the object
    def accelerate_x(self):
        '''Setter to accelerate or decellerate object'''
        self.x_velocity += self.x_velocity_increment
    def accelerate_y(self):
        '''Setter to accelerate or decellerate object'''
        self.y_velocity += self.y_velocity_increment
    def deccelerate_x(self):
        '''Setter to accelerate or decellerate object'''
        self.x_velocity -= self.x_velocity_increment
    def deccelerate_y(self):
        '''Setter to accelerate or decellerate object'''
        self.y_velocity -= self.y_velocity_increment
    def set_x_increment(self, x_velocity_increment):
        self.x_velocity_increment = x_velocity_increment
    def set_y_increment(self, y_velocity_increment):
        self.y_velocity_increment = y_velocity_increment


# Ideas: give objects a way to sense other surrounding objects. Have a way to repel on collision.
