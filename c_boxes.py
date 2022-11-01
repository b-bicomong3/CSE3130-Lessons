# c_boxes.py

"""
Title: Boxes
Author: Beatrix Bicomong
Date: 28-10-22
"""

import pygame


class Box:

    def __init__(self, WIDTH=1, HEIGHT=1, X=0, Y=0):
        self.__WIDTH = WIDTH
        self.__HEIGHT = HEIGHT
        self.__DIM = (self.__WIDTH, self.__HEIGHT)
        self.__X = X
        self.__Y = Y
        self.__POS = (self.__X, self.__Y)
        self.__COLOR = (255, 255, 255)
        self.__SCREEN = pygame.Surface(self.__DIM, pygame.SRCALPHA, 32)
        self.__SCREEN.fill(self.__COLOR)
        self.__SPD = 10

    # MODIFIER METHODS
    def setX(self, X):
        self.__X = X
        self.__POS = (self.__X, self.__Y)

    def setY(self, Y):
        self.__Y = Y
        self.__POS = (self.__X, self.__Y)

    def setColor(self, COLOR):
        """

        :return:
        """
        self.__COLOR = COLOR
        self.__SCREEN.fill(self.__COLOR)

    def moveBox(self, KEYS_PRESSED):
        """
        move box with WASD
        :param KEYS_PRESSED: int
        :param MAX_WIDTH: int
        :param MAX_HEIGHT: int
        :param MIN_WIDTH: int
        :param MIN_HEIGHT: int
        :return: None
        """
        if KEYS_PRESSED[pygame.K_d] == 1:
            self.__X += self.__SPD
        if KEYS_PRESSED[pygame.K_a] == 1:
            self.__X -= self.__SPD
        if KEYS_PRESSED[pygame.K_w] == 1:
            self.__Y -= self.__SPD
        if KEYS_PRESSED[pygame.K_s] == 1:
            self.__Y += self.__SPD

        self.__POS = (self.__X, self.__Y)

        # Stops at the edge of the screen

    def stopAtEdge(self, MAX_WIDTH, MAX_HEIGHT, MIN_WIDTH=0, MIN_HEIGHT=0):
        if self.__X > MAX_WIDTH - self.__SCREEN.get_width():
            self.__X = MAX_WIDTH - self.__SCREEN.get_width()
        elif self.__X < MIN_WIDTH:
            self.__X = MIN_WIDTH

        if self.__Y > MAX_HEIGHT - self.__SCREEN.get_height():
            self.__Y = MAX_HEIGHT - self.__SCREEN.get_height()
        elif self.__Y < MIN_HEIGHT:
            self.__Y = MIN_HEIGHT

        self.__POS = (self.__X, self.__Y)

    def wrapEdge(self, MAX_WIDTH, MAX_HEIGHT, MIN_WIDTH=0, MIN_HEIGHT=0):
        """
        when the object goes past one wall, it will reappear on the opposite edge
        :param MAX_WIDTH: int
        :param MAX_HEIGHT: int
        :param MIN_WIDTH: int
        :param MIN_HEIGHT: int
        :return: None
        """
        if self.__X > MAX_WIDTH:
            self.__X = MIN_WIDTH - self.__SCREEN.get_width()
        elif self.__X < MIN_WIDTH - self.__SCREEN.get_width():
            self.__X = MAX_WIDTH

        if self.__Y > MAX_HEIGHT:
            self.__Y = MIN_WIDTH - self.__SCREEN.get_height()
        elif self.__Y < MIN_HEIGHT - self.__SCREEN.get_height():
            self.__Y = MAX_HEIGHT

        self.__POS = (self.__X, self.__Y)

    def autoScroll(self):
        self.__X += self.__SPD
        self.__POS = (self.__X, self.__Y)

    # ACCESSOR METHODS

    def getBox(self):
        return self.__SCREEN

    def getPOS(self):
        return self.__POS


if __name__ == "__main__":
    from a_template import Window

    pygame.init()

    WINDOW = Window("Boxes", 800, 600, 30)
    BOX = Box(100, 100, 0, 0)
    BOX.setX(100)
    BOX.setY(100)
    BOX.setColor((255, 0, 0))
    BOX2 = Box(100, 100, 0, 0)
    BOX2.setX(500)
    BOX2.setY(400)
    BOX2.setColor((0, 0, 255))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        PRESSED_KEYS = pygame.key.get_pressed()
        # PROCESSOR
        BOX.moveBox(PRESSED_KEYS)
        BOX2.moveBox(PRESSED_KEYS)

        BOX.stopAtEdge(WINDOW.getWindowWidth(), WINDOW.getWindowHeight())
        BOX2.stopAtEdge(WINDOW.getWindowWidth(), WINDOW.getWindowHeight())

        # OUTPUTS
        WINDOW.clearScreen()
        WINDOW.getScreen().blit(BOX.getBox(), BOX.getPOS())
        WINDOW.getScreen().blit(BOX2.getBox(), BOX2.getPOS())
        WINDOW.updateFrame()
