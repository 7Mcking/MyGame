# Created by mcking at 12.07.23

import pygame
from pygame.locals import *
from pydantic import int, tuple
import sys
import random
import ball, Button, Text


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 60

# Initialize Pygame
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Load Assets

# Initialize Variables

