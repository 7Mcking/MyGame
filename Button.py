# Created by Mcking at 09.07.23
import sys

import pygame
from pygame.locals import *


class Button:
    STATE_IDLE = 'idle'
    STATE_ARMED = 'armed'
    STATE_DISARMED = 'disarmed'

    def __init__(self, window, loc, up, down):
        self.window = window
        self.loc = loc
        self.up = pygame.image.load(up)
        self.down = pygame.image.load(down)

        # Get the rectangle of the button
        self.rect = self.up.get_rect()
        self.rect[0] = loc[0]
        self.rect[1] = loc[1]
        self.state = Button.STATE_IDLE

    def handleEvent(self, eventObj):

        if eventObj.type not in (MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN):
            return False

        eventPointInButtonRect = self.rect.collidepoint(eventObj.pos)

        if self.state == Button.STATE_IDLE:
            if eventObj.type == MOUSEBUTTONDOWN and eventPointInButtonRect:
                self.state = Button.STATE_ARMED

            elif self.state == Button.STATE_ARMED:
                if (eventObj.type == MOUSEBUTTONUP) and eventPointInButtonRect:
                    self.state = Button.STATE_DISARMED

                # If the mouse moved off the button, disarm it.
                elif self.state == Button.STATE_ARMED:
                    if eventObj.type == MOUSEBUTTONUP and eventPointInButtonRect:
                        self.state = Button.STATE_IDLE
                        return True  # Clicked!

                    if eventObj.type == MOUSEMOTION and not eventPointInButtonRect:
                        self.state = Button.STATE_DISARMED
                elif self.state == Button.STATE_DISARMED:
                    if eventPointInButtonRect:
                        self.state = Button.STATE_ARMED
                    elif eventObj.type == MOUSEBUTTONUP:
                        self.state = Button.STATE_IDLE

                return False  # Not clicked.

    def draw(self):
        if self.state == Button.STATE_ARMED:
            self.window.blit(self.down, self.loc)

        else:
            self.window.blit(self.up, self.loc)


if __name__ == '__main__':

    # Define Constants
    GRAY = (100, 100, 100)
    WINDOW_HEIGHT = 400
    WINDOW_WIDTH = 400
    FRAMES_PER_SECOND = 30

    # Initialize Pygame
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    myButtonA = Button(window, (50, 50), up='Images/buttonAUp.png',
                       down='Images/buttonADown.png')

    myButtonB = Button(window, (50, 100), up='Images/buttonBUp.png',
                       down='Images/buttonBDown.png')
    myButtonC = Button(window, (50, 150), up='Images/buttonCUp.png',
                       down='Images/buttonCDown.png')

    # Set the font and font size
    font = pygame.font.Font(None, 36)

    # Set the text content
    text_content = "Hello, Pygame!"

    # Render the text surface
    text_surface = font.render(text_content, True, (255, 255, 255))

    # Get the dimensions of the text surface
    TEXT_WIDTH = text_surface.get_width()
    TEXT_HEIGHT = text_surface.get_height()

    # Calculate the position to center the text on the window
    text_x = (WINDOW_WIDTH - TEXT_WIDTH) // 2
    text_y = (WINDOW_HEIGHT - TEXT_HEIGHT) // 2

    while True:

        # Check for events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if myButtonA.handleEvent(event):
                print("Button A Clicked")

            if myButtonB.handleEvent(event):
                window.blit(text_surface, (text_x, text_y))
                print("Button B Clicked")

            if myButtonC.handleEvent(event):
                print("Button C Clicked")

        # Do any per frame tasks
        window.blit(text_surface, (text_x, text_y))
        # Clear the screen
        window.fill(GRAY)

        # Draw all window elements
        myButtonA.draw()
        myButtonB.draw()
        myButtonC.draw()

        # Update the window
        pygame.display.update()

        # Slow things down a bit
        clock.tick(FRAMES_PER_SECOND)  # 30 frames per second is plenty for this game
