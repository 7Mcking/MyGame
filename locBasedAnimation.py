# Created by mcking at 09.07.23

# Importing Packages

import pygame
import sys
from pygame.locals import *
import random
from ball import Ball


def main():
    # N_Balls
    NBALLS = 4

    # Defining Constants
    ballList = []
    BLACK = (0, 0, 0)
    WINDOWWIDTH = 1024
    WINDOWHEIGHT = 720
    FRAMES_PER_SECOND = 60
    BALL_WIDTH_HEIGHT = 100
    N_PIXELS_TO_MOVE = 3

    # Initializing Pygame
    pygame.init()
    window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    clock = pygame.time.Clock()

    # Loading Assets

    # Initialize Variables
    for oBalls in range(NBALLS):
        oBall = Ball(window, WINDOWWIDTH, WINDOWHEIGHT)
        ballList.append(oBall)

    # Main Game Loop
    while True:

        # Checking for events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Do per frame tasks
        for oBall in ballList:
            oBall.update()

        # Clear the screen
        window.fill(BLACK)

        # Draw all window elements
        for oBall in ballList:
            oBall.draw()

        # Update the window
        pygame.display.update()

        # Slow things down
        clock.tick(FRAMES_PER_SECOND)


if __name__ == '__main__':
    main()
