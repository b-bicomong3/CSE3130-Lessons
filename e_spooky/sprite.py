# sprite.py in e_spooky
"""
Title: Sprite Class
Author: Beatrix Bicomong
Date: 31-10-2022
"""
import pygame


class MySprite:
    """
    Abstract Sprite Class
    """

    def __init__(self):
        self.__X = 0
        self.__Y = 0
        self.__POS = (self.__X, self.__Y)
        self.__SPD = 1
        self._COLOR = (255, 255, 255)
        self._SCREEN = pygame.Surface((1, 1))  # empty Surface of 1 pixel
        self.__WIDTH = 1
        self.__HEIGHT = 1
        self.__DIR_X = 1
        self.__DIR_Y = 1

    # MODIFIER METHODS

    def setX(self, X):
        self.__X = X
        self.__POS = (self.__X, self.__Y)

    def setY(self, Y):
        self.__Y = Y
        self.__POS = (self.__X, self.__Y)

    def setPosition(self, X, Y):
        self.__X = X
        self.__Y = Y
        self.__POS = (self.__X, self.__Y)

    def setSpeed(self, SPEED):
        self.__SPD = SPEED

    def setColor(self, COLOR):
        self._COLOR = COLOR

    def setWidth(self, WIDTH):
        self.__WIDTH = WIDTH

    def setHeight(self, HEIGHT):
        self.__HEIGHT = HEIGHT

    def move(self, PRESSED_KEYS):
        """
        moves sprite with WASD
        :param PRESSED_KEYS: list -> int
        :return:
        """
        if PRESSED_KEYS[pygame.K_d] == 1:
            self.__X += self.__SPD
        elif PRESSED_KEYS[pygame.K_a] == 1:
            self.__X -= self.__SPD
        elif PRESSED_KEYS[pygame.K_w] == 1:
            self.__Y -= self.__SPD
        elif PRESSED_KEYS[pygame.K_s] == 1:
            self.__Y += self.__SPD

        self.__POS = (self.__X, self.__Y)

    # PROCESSING

    def bounceX(self, MAX_WIDTH, MIN_WIDTH=0):
        self.__X += self.__DIR_X * self.__SPD
        if self.__X > MAX_WIDTH - self.getScreenWidth():
            self.__DIR_X = -1
        elif self.__X < MIN_WIDTH:
            self.__DIR_X = 1

        self.__POS = (self.__X, self.__Y)

    def bounceY(self, MAX_HEIGHT, MIN_HEIGHT=0):
        self.__Y += self.__DIR_Y * self.__SPD
        if self.__Y > MAX_HEIGHT - self.getScreenHeight():
            self.__DIR_Y = -1
        elif self.__Y < MIN_HEIGHT:
            self.__DIR_Y = 1

        self.__POS = (self.__X, self.__Y)

    def bounceAll(self, MAX_WIDTH, MAX_HEIGHT, MIN_WIDTH=0, MIN_HEIGHT=0):
        self.bounceX(MAX_WIDTH, MIN_WIDTH)
        self.bounceY(MAX_HEIGHT, MIN_HEIGHT)

    def marqueeX(self):
        """
        moves sprite from left to right across the screen
        :return:
        """
        self.__X += self.__SPD
        self.__POS = (self.__X, self.__Y)

    def wrapX(self, MAX_WIDTH, MIN_WIDTH=0):
        """
        move sprite to opposite side of the left/right edges
        :param MAX_WIDTH:
        :param MIN_WIDTH:
        :return:
        """
        if self.__X > MAX_WIDTH:
            self.__X = MIN_WIDTH - self.getScreenWidth()
        elif self.__X < MIN_WIDTH - self.getScreenWidth():
            self.__X = MAX_WIDTH

        self.__POS = (self.__X, self.__Y)

    def wrapY(self, MAX_HEIGHT, MIN_HEIGHT=0):
        """
        move sprite to opposite side of the left/right edges
        :param MAX_HEIGHT:
        :param MIN_HEIGHT:
        :return:
        """
        if self.__Y > MAX_HEIGHT:
            self.__Y = MIN_HEIGHT - self.getScreenHeight()
        elif self.__Y < MIN_HEIGHT - self.getScreenHeight():
            self.__Y = MAX_HEIGHT

        self.__POS = (self.__X, self.__Y)

    def wrapAll(self, MAX_WIDTH, MAX_HEIGHT, MIN_WIDTH=0, MIN_HEIGHT=0):
        self.wrapX(MAX_WIDTH, MIN_WIDTH)
        self.wrapY(MAX_HEIGHT, MIN_HEIGHT)

    def checkBoundaries(self, MAX_WIDTH, MAX_HEIGHT, MIN_WIDTH=0, MIN_HEIGHT=0):
        if self.__X > MAX_WIDTH - self.getScreenWidth():
            self.__X = MAX_WIDTH - self.getScreenWidth()
        elif self.__X < MIN_WIDTH:
            self.__X = MIN_WIDTH

        if self.__Y > MAX_HEIGHT - self.getScreenHeight():
            self.__Y = MAX_HEIGHT - self.getScreenHeight()
        elif self.__Y < MIN_HEIGHT:
            self.__Y = MIN_HEIGHT

    # ACCESSOR METHODS

    # INPUTS

    def getX(self):
        return self.__X

    def getY(self):
        return self.__Y

    def getPOS(self):
        return self.__POS

    def getScreen(self):
        return self._SCREEN

    def getScreenWidth(self):
        return self._SCREEN.get_width()

    def getScreenHeight(self):
        return self._SCREEN.get_height()

    def getWidth(self):
        return self.__WIDTH

    def getHeight(self):
        return self.__HEIGHT
