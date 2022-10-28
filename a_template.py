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
        self.__SPD = 3
        self.__DIRX = 1
        self.__DIRY = 1

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

    def setY(self, Y):
        self.__Y = Y
        self.__POS = (self.__X, self.__Y)

    def marqueeX(self, WINDOW_WIDTH):
        """
        Object move left to right and then wrap around the screen
        :param WINDOW_WIDTH: int
        :return: None
        """
        if self.__X > WINDOW_WIDTH:
            self.__X = -self.__SCREEN.get_width()
        else:
            self.__X += self.__SPD
        self.__POS = (self.__X, self.__Y)

    def marqueeY(self, WINDOW_HEIGHT):
        """
        Object move up to down and then wrap around the screen
        :param WINDOW_HEIGHT: int
        :return: None
        """
        if self.__Y > WINDOW_HEIGHT:
            self.__Y = -self.__SCREEN.get_height()
        else:
            self.__Y += self.__SPD
        self.__POS = (self.__X, self.__Y)

    def bounceX(self, WINDOW_WIDTH):
        """
        Text will bounce back and forth along the X axis
        :param WINDOW_WIDTH: int
        :return: None
        """
        self.__X += self.__DIRX * self.__SPD
        if self.__X > WINDOW_WIDTH - self.__SCREEN.get_width():
            self.__X = WINDOW_WIDTH - self.__SCREEN.get_width()
            self.__DIRX = -1
        if self.__X < 0:
            self.__X = 0
            self.__DIRX = 1

        self.__POS = (self.__X, self.__Y)

    def bounceY(self, WINDOW_HEIGHT):
        """
        Text will bounce up and down along the X axis
        :param WINDOW_HEIGHT: int
        :return: None
        """
        self.__Y += self.__DIRY * self.__SPD
        if self.__Y > WINDOW_HEIGHT - self.__SCREEN.get_height():
            self.__Y = WINDOW_HEIGHT - self.__SCREEN.get_height()
            self.__DIRY = -1
        if self.__Y < 0:
            self.__Y = 0
            self.__DIRY = 1

        self.__POS = (self.__X, self.__Y)

    def setCentreY(self, WINDOW_HEIGHT):
        Y = WINDOW_HEIGHT / 2 - self.__SCREEN.get_height() / 2
        return Y

    def setCentreX(self, WINDOW_WIDTH):
        self.__X = WINDOW_WIDTH / 2 - self.__SCREEN.get_width() / 2

    # ACCESSOR METHODS

    def getText(self):
        return self.__SCREEN

    def getPOS(self):
        return self.__POS

    def getX(self):
        return self.__X

    def getY(self):
        return self.__Y

    def setSpeed(self, SPEED):
        """
        update the text's speed
        :param SPEED:
        :return:
        """
        self.__SPD = SPEED


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
