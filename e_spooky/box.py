# box.py in e_spooky
"""
Title: Box Class
Author: Beatrix Bicomong
Date: 31-10-2022
"""
from sprite import MySprite
import pygame


class Box(MySprite):
    def __init__(self):
        MySprite.__init__(self)
        self.setWidth(100)
        self.setHeight(100)
        self.__DIM = (self.getWidth(), self.getHeight())
        self._SCREEN = pygame.Surface(self.__DIM, pygame.SRCALPHA, 32)
        self._SCREEN.fill(self._COLOR)


if __name__ == "__main__":
    from window import Window
    pygame.init()
    BOX = Box()
    BOX.setSpeed(10)
    WINDOW = Window("Box", 800, 600, 30)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        KEY_PRESSES = pygame.key.get_pressed()
        BOX.move(KEY_PRESSES)
        BOX.wrapAll(WINDOW.getWindowWidth(), WINDOW.getWindowHeight())

        WINDOW.clearScreen()
        WINDOW.getScreen().blit(BOX.getScreen(), BOX.getPOS())
        WINDOW.updateFrame()

