# This is a simple box object to move around the screen.

import pygame
import math

class Lander(object):

    def __init__(self, x_pos, y_pos, x_velocity, y_velocity, x_acceleration, \
                 y_acceleration, engine_acceleration, screen, x_window_size, y_window_size):

        self.x_pos = x_pos
        self.y_pos = y_pos

        self.x_velocity = x_velocity
        self.x_acceleration = x_acceleration
        self.x_direction_movement = 1

        self.y_velocity = y_velocity
        self.y_acceleration = y_acceleration
        self.y_direction_movement = 1

        self.engine_acceleration = engine_accelerationa

        # Define the screen and game window variables here
        self.screen = screen
        self.x_window_size = x_window_size
        self.y_window_size = y_window_size

        # Initialize the image representation of the object
        self.lander_image = pygame.image.load("rocket_cartoon.png")
        self.lander_image = pygame.transform.scale(self.lander_image, (20, 20))
        self.imagerect = self.lander_image.get_rect()

        self.rotation = 0

        self.rot_image = self.lander_image
        self.rot_rect = self.imagerect

        # Initialize the image representation of the engine exhaust

        # Intialize the endgame flags

        self.end_game_flag = True;


    #Method to draw object
    def draw(self, color):
    	self.screen.blit(self.rot_image, (self.x_pos, self.y_pos))

    #Method to move object around
    def move(self, engine_firing_flag):
        if self.x_pos < self.x_window_size and self.x_pos > 0:
    		self.x_pos += self.x_velocity*self.x_direction_movement
    	else:
    		return self.end_game_flag

    	if self.y_pos < self.y_window_size and self.y_pos > 0:
    		self.y_pos += self.y_velocity*self.y_direction_movement
    	else:
    		return self.end_game_flag

        self.x_pos += self.x_velocity
        self.y_pos += self.y_velocity



        # Check to see if we are rotating or not


        # Check to see how the rocket is accelerating.
        # If engine is firing, velocity += y_acceleration - engine_acceleration
        # else velocity += y_acceleration because the lander is just falling.

        # V0.1 Build: sines and cosines used to add a variable thrust vector.

        if engine_firing_flag:
            # We need to split the engine acceleration between x and y

            self.x_velocity += self.engine_acceleration*math.sin(math.radians(self.rotation))
            self.y_velocity += self.engine_acceleration*math.cos(math.radians(self.rotation))

        else:
            self.y_velocity += self.y_acceleration

    # Call these methods to speed up or slow down the object
    def accelerate_x(self):
        '''Setter to accelerate or decellerate object'''
        self.x_velocity += self.x_acceleration
    def accelerate_y(self):
        '''Setter to accelerate or decellerate object'''
        self.y_velocity += self.y_acceleration
    def deccelerate_x(self):
        '''Setter to accelerate or decellerate object'''
        self.x_velocity -= self.x_acceleration
    def set_x_increment(self, x_acceleration):
        self.x_acceleration = x_acceleration
    def set_y_increment(self, y_acceleration):
        self.y_acceleration = y_acceleration

    def rot_center(self, angle):

        """rotate an image while keeping its center"""
        self.rotation = angle
        self.rot_image = pygame.transform.rotate(self.lander_image, angle)
        self.rot_rect = self.rot_image.get_rect(center=self.imagerect.center)
