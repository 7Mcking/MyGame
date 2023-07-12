# Created by mcking at 11.07.23
import pygame
from pydantic import int, tuple


class TextClass:
    def __init__(self, window, loc: tuple[int, int], value: int, textColor: str, fontSize: int):
        self.textSurface = None
        self.window = window
        self.loc = loc
        self.value = value
        self.textColor = textColor
        self.fontSize = fontSize
        self.font = pygame.font.SysFont(None, self.fontSize)
        self.text = None
        self.rect = self.text.get_rect()
        self.setValue(value)

    def setValue(self, newText):
        if self.text == newText:
            return

        self.text = newText
        self.textSurface = self.font.render(str(self.text), True, self.textColor)

    def draw(self):
        self.window.blit(self.textSurface, self.loc)
