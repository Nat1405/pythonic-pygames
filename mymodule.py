# This is a simple box object to move around the screen.

import pygame
game_title = "THAT GAME"

class Box(object):

    def __init__(self, x, y, screen):
        self.x_pos = x
        self.y_pos = y

        self.x_direction_movement = 1
        self.y_direction_movement = 1

        self.screen = screen

        self.BLACK = ( 0, 0, 0)
        self.WHITE = ( 255, 255, 255)
        self.GREEN = ( 0, 255, 0)
        self.RED =   ( 255, 0, 0)
        self.BLUE =  (0, 0, 255)

    #Method to draw object
    def draw(self,size_grid):
        for i in range(size_grid):
    		for k in range(size_grid):
    			pygame.draw.rect(self.screen, self.BLACK, (self.x_pos,self.y_pos,10,10))

    #Method to move object around
    def move(self, x_velocity, x_direction_movement, y_velocity, y_direction_movement):
        self.x_pos += x_velocity*x_direction_movement
        self.y_pos += y_velocity*y_direction_movement
