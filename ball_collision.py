# Created by: Naren Sadhwani

import pygame
import random
from pygame.locals import *
import sys, cv2
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent
pathToBall = str(BASE_PATH) + "/Images/ball.png"


def main():
    # Define constants
    BLACK = (255, 255, 255)
    WINDOWWIDTH = 1024
    WINDOWHEIGHT = 720
    FRAMES_PER_SECOND = 60
    BALL_WIDTH_HEIGHT = 50
    MAX_HEIGHT = WINDOWHEIGHT - BALL_WIDTH_HEIGHT
    MAX_WIDTH = WINDOWWIDTH - BALL_WIDTH_HEIGHT
    TARGET_X = 400
    TARGET_Y = 320
    TARGET_WIDTH_HEIGHT = 120
    N_PIXELS_TO_MOVE = 3

    # Initialize the world
    pygame.init()
    window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    clock = pygame.time.Clock()

    # Load assets
    ballImage = pygame.image.load('images/ball.png')
    targetImage = pygame.image.load('images/target.jpg')

    # Initialize variables
    ballX = random.randrange(MAX_WIDTH)
    ballY = random.randrange(MAX_HEIGHT)
    targetRect = pygame.Rect(TARGET_X, TARGET_Y, TARGET_WIDTH_HEIGHT, TARGET_WIDTH_HEIGHT)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # See if user clicked
        keyPressedTuple = pygame.key.get_pressed()

        if keyPressedTuple[pygame.K_LEFT]:  # moving left
            ballX = ballX - N_PIXELS_TO_MOVE

        if keyPressedTuple[pygame.K_RIGHT]:  # moving right
            ballX = ballX + N_PIXELS_TO_MOVE

        if keyPressedTuple[pygame.K_UP]:  # moving up
            ballY = ballY - N_PIXELS_TO_MOVE

        if keyPressedTuple[pygame.K_DOWN]:  # moving down
            ballY = ballY + N_PIXELS_TO_MOVE

        # Check if the ball is colliding with the target
        ballRect = pygame.Rect(ballX, ballY,
                               BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
        if ballRect.colliderect(targetRect):
            print('Ball is touching the target')

        # Clear the window
        window.fill(BLACK)

        # Draw all window elements
        window.blit(targetImage, (TARGET_X, TARGET_Y))  # draw the target
        window.blit(ballImage, (ballX, ballY))  # draw the ball

        # Update the window
        pygame.display.update()

        # Slow things down a bit
        clock.tick(FRAMES_PER_SECOND)  # make pygame wait


if __name__ == '__main__':
    main()
