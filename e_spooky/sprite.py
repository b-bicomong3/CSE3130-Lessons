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

    # ACCESSOR METHODS

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
