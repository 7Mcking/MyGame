# Created by mcking at 09.07.23
import pygame
from pygame.locals import *
import random


class Ball:

    def __init__(self, window, window_width, window_height):
        self.window = window
        self.window_width = window_width
        self.window_height = window_height

        self.ballImage = pygame.image.load('images/ball.png')

        # Define the rectangle for the ball
        balalRect = self.ballImage.get_rect()
        self.width = balalRect.width
        self.height = balalRect.height
        self.MAX_HEIGHT = self.window_height - self.height
        self.MAX_WIDTH = self.window_width - self.width

        # Define the initial position of the ball
        self.x = random.randrange(self.MAX_WIDTH)
        self.y = random.randrange(self.MAX_HEIGHT)

        # Define the speed of the ball
        speedList = [-4, -3, -2, -1, 1, 2, 3, 4]
        self.xSpeed = random.choice(speedList)
        self.ySpeed = random.choice(speedList)

    def update(self):
        # Check for location of the ball and interaction with the wall
        if (self.x < 0) or (self.x > self.MAX_WIDTH):
            self.xSpeed = -self.xSpeed

        if (self.y < 0) or (self.y > self.MAX_HEIGHT):
            self.ySpeed = -self.ySpeed

        # Update the Ball's x and y position, using the speed in two directions
        self.x = self.x + self.xSpeed
        self.y = self.y + self.ySpeed

    def draw(self):
        self.window.blit(self.ballImage, (self.x, self.y))
