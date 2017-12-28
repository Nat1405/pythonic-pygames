#!/usr/bin/env python

# A game of snake? Maybe, I'm bored

# mvp: make a single dot that moves around with nothing but the standard library

# What do we need...
#
# Game initialization.
    #
#
#
#
# We need a loop. In this loop:
    #
    # Check for input from the user within a time limit. If no value recieved,
    # use the same move as last time.
    #
    # Update the location of the dot.
    # Redraw the field with a new location for the dot.

# Draw method.
def draw(matrix, blankchar, filledchar):
    """Draw the matrix in terminal

    Parameters
    ----------
    matrix : iterable
        a list of boolean values. true will be draw, false will not.
    blankchar : str
        character to draw in a blank location
    filledchar : str
        character to draw in a filled location

    """
    for i in range(len(a)):
        for j in range(len(a[i])):
            if matrix[i,j]:
                print(filledchar, end='')
            else:
                print(blankchar, end='')
        print('\n', end='')


if __name__ == "__main__":
    a = [[1,0], [0,1]]
    draw(a, '[ ]', '[*]')
