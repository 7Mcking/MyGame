import pygame
from pygame.locals import *
import sys
import random


def main():
    # Define constants
    BLACK = (0, 0, 0)
    WINDOWWIDTH = 1024
    WINDOWHEIGHT = 720
    FRAMES_PER_SECOND = 60
    N_PIXELS_TO_MOVE = 3

    # Initialize Pygame
    pygame.init()
    window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    clock = pygame.time.Clock()

    # Load assets
    ballImage = pygame.image.load('images/ball.png')
    bounceSound = pygame.mixer.Sound('sounds/bounce.wav')

    # Initialize variables
    MAX_HEIGHT = WINDOWHEIGHT - ballImage.get_height()
    MAX_WIDTH = WINDOWWIDTH - ballImage.get_width()
    ballRect = ballImage.get_rect()
    ballRect.left = random.randrange(MAX_WIDTH)
    ballRect.top = random.randrange(MAX_HEIGHT)
    xSpeed = N_PIXELS_TO_MOVE
    ySpeed = N_PIXELS_TO_MOVE

    # Main game loop
    while True:
        # Check for events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Do per frame tasks
        if (ballRect.left < 0) or (ballRect.right > MAX_WIDTH):
            xSpeed = -xSpeed
            bounceSound.play()

        if (ballRect.top < 0) or (ballRect.bottom > MAX_HEIGHT):
            ySpeed = -ySpeed
            bounceSound.play()

        ballRect.left = ballRect.left + xSpeed
        ballRect.top = ballRect.top + ySpeed

        # Clear the screen
        window.fill(BLACK)

        # Draw all window elements
        window.blit(ballImage, ballRect)

        # Update the display
        pygame.display.update()

        # Delay the next frame
        clock.tick(FRAMES_PER_SECOND)


if __name__ == '__main__':
    main()