# window.py in e_spooky
"""
Title: Window Class
Author: Beatrix Bicomong
Date: 31-10-2022
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
        self.__BG_COLOR = (50, 50, 50)
        self.__FRAME = pygame.time.Clock()  # clock object tha tmeasures fps
        self.__SCREEN = pygame.display.set_mode(
            self.__SCREEN_DIM)  # SCREEN object, every item in your program will overlay on top of the screen
        self.__SCREEN.fill((50, 50, 50))  # fills the screen with a layer of color
        self.__CAPTION = pygame.display.set_caption(
            self.__TITLE)  # sets the title of the window to the TITLE value. (It doesn't return anything).

    # MODIFIER

    def updateFrame(self):
        """
        Update the window object based on the FPS
        :return: None
        """
        self.__FRAME.tick(self.__FPS)
        pygame.display.flip()  # updates the computer display with the new frame.

    def clearScreen(self):
        """
        Fill the screen with the background color
        :return:
        """
        self.__SCREEN.fill(self.__BG_COLOR)

    def setColor(self, COLOR):
        """
        Updates the background color
        :param COLOR: tuple -> int
        :return: None
        """
        self.__BG_COLOR = COLOR

    # ACCESSOR

    def getScreen(self):
        return self.__SCREEN

    def getWindowWidth(self):
        return self.__WIDTH

    def getWindowHeight(self):
        return self.__HEIGHT

if __name__ == "__main__":
    WINDOW = Window("Window", 800, 600, 30)
    pygame.init()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        WINDOW.clearScreen()
        WINDOW.updateFrame()