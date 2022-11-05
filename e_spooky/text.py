# text.py in e_spooky
"""
title: text sprites
author: beatrix bicomong
date-created: 01-11-22
"""
from sprite import MySprite
import pygame


class Text(MySprite):
    def __init__(self, TEXT):
        MySprite.__init__(self)
        self.__TEXT = TEXT
        self.__FONT_FAMILY = "comicsans"
        self.__FONT_SIZE = 36
        self.__FONT = pygame.font.SysFont(self.__FONT_FAMILY, self.__FONT_SIZE)
        self._SCREEN = self.__FONT.render(self.__TEXT, True, self._COLOR)

    # MODIFIER METHODS

    def setSize(self, SIZE):
        self.__FONT_SIZE = SIZE
        self.__FONT = pygame.font.SysFont(self.__FONT_FAMILY, self.__FONT_SIZE)
        self._SCREEN = self.__FONT.render(self.__TEXT, True, self._COLOR)

    def setText(self, NEW_TEXT):
        self.__TEXT = NEW_TEXT
        self._SCREEN = self.__FONT.render(self.__TEXT, True, self._COLOR)


if __name__ == "__main__":
    from window import Window

    pygame.init()
    WINDOW = Window("Text", 800, 600, 30)
    TEXT = Text("(0-0)")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        TEXT.marqueeX()
        TEXT.wrapX(WINDOW.getWindowWidth())

        WINDOW.clearScreen()
        WINDOW.getScreen().blit(TEXT.getScreen(), TEXT.getPOS())
        WINDOW.updateFrame()
