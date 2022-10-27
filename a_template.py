# a_template.py

"""
Title: Pygame template
Author: Beatrix Bicomong
Date: 26-10-2022
"""

import pygame


class Window:
    """
    Create the window that will load pygame
    :return: None
    """

    def __init__(self, TITLE, WIDTH, HEIGHT, FPS):
        self.__TITLE = TITLE  # text that appears in the title bar
        self.__FPS = FPS  # frames per second
        self.__WIDTH = WIDTH  # width of the window frame
        self.__HEIGHT = HEIGHT  # height og the window frame
        self.__SCREEN_DIM = (self.__WIDTH, self.__HEIGHT)  # screen dimensions
        self.__FRAME = pygame.time.Clock()  # clock object tha tmeasures fps
        self.__SCREEN = pygame.display.set_mode(
            self.__SCREEN_DIM)  # SCREEN object, every item in your program will overlay on top of the screen
        self.__SCREEN.fill((50, 50, 50))  # fills the screen with a layer of color
        self.__CAPTION = pygame.display.set_caption(
            self.__TITLE)  # sets the title of the window to the TITLE value. (It doesn't return anything).

    def updateFrame(self):
        """
        Update the window object based on the FPS
        :return: None
        """
        self.__FRAME.tick(self.__FPS)
        pygame.display.flip()  # updates the computer display with the new frame.

    def getScreen(self):
        return self.__SCREEN


class Text:
    """
    Creates a text object to be placed on a Screen
    """

    def __init__(self, TEXT):
        """
        Creates a Text object to be placed on a Screen
        :param TEXT:
        """
        self.__TEXT = TEXT
        self.__COLOR = (255, 255, 255)
        self.__FONT = pygame.font.SysFont("comicsans", 36)
        self.__SCREEN = self.__FONT.render(self.__TEXT, True, self.__COLOR)
        self.__X = 0
        self.__Y = 0
        self.__POS = (self.__X, self.__Y)

    # MODIFIER METHODS

    def setTextColor(self, COLOR):
        """
        update text color
        :param COLOR: tuple -> (R, G, B)
        :return: None
        """
        self.__COLOR = COLOR
        self.__SCREEN = self.__FONT.render(self.__TEXT, True, COLOR)

    def setTextSize(self, SIZE):
        """
        update text size
        :param SIZE: int
        :return: None
        """
        self.__FONT = pygame.font.SysFont("comicsans", SIZE)
        self.__SCREEN = self.__FONT.render(self.__TEXT, True, self.__COLOR)

    def setPOS(self, X, Y):
        """
        updates both X and Y
        :param X: int
        :param Y: int
        :return: None
        """
        self.__X = X
        self.__Y = Y
        self.__POS = (self.__X, self.__Y)

    def setX(self, X):
        self.__X = X
        self.__POS = (self.__X, self.__Y)

    # ACCESSOR METHODS

    def getText(self):
        return self.__SCREEN

    def getPOS(self):
        return self.__POS

    def getX(self):
        return self.__X


if __name__ == "__main__":
    pygame.init()

    WINDOW = Window("template", 800, 600, 30)
    TEXT = Text("hello world")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        WINDOW.getScreen().blit(TEXT.getText(), (0, 0))
        WINDOW.updateFrame()
