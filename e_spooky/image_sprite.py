# image_sprite.py in e_spooky
"""
title: image sprites
author: Beatrix Bicomong
date-created: 01-11-22
"""
from sprite import MySprite
import pygame


class ImageSprite(MySprite):

    def __init__(self, IMAGE_FILE):
        MySprite.__init__(self)
        self.__FILE_LOC = IMAGE_FILE
        self._SCREEN = pygame.image.load(self.__FILE_LOC).convert_alpha()
        self.__X_FLIP = False

    def setFlipX(self):
        """
        flip the image once
        :return:
        """
        self._SCREEN = pygame.transform.flip(self._SCREEN, True, False)

    def setScale(self, SCALE_X, SCALE_Y=0):
        """
        change the scale of the image
        :param SCALE_X:
        :param SCALE_Y:
        :return:
        """
        if SCALE_Y == 0:
            SCALE_Y = SCALE_X
        self._SCREEN = pygame.transform.scale(self._SCREEN,
                                              (self.getScreenWidth() // SCALE_X, self.getScreenHeight() // SCALE_Y))

    def flipImageX(self, KEYS_PRESSED):
        if KEYS_PRESSED[pygame.K_d] == 1 and self.__X_FLIP:
            self._SCREEN = pygame.transform.flip(self._SCREEN, True, False)
            self.__X_FLIP = False
        if KEYS_PRESSED[pygame.K_a] == 1 and not self.__X_FLIP:
            self._SCREEN = pygame.transform.flip(self._SCREEN, True, False)
            self.__X_FLIP = True

    def move(self, KEYS_PRESSED):
        MySprite.move(self, KEYS_PRESSED)
        self.flipImageX(KEYS_PRESSED)


if __name__ == "__main__":
    from window import Window

    pygame.init()
    WINDOW = Window("Image Sprite", 800, 600, 30)
    PIKACHU = ImageSprite("media/pikachu.png")
    GHOST = ImageSprite("media/ghost_sprite.png")
    PIKACHU.setFlipX()
    PIKACHU.setScale(1)
    GHOST.setScale(0.5)
    PIKACHU.setSpeed(10)
    GHOST.setSpeed(10)
    GHOST.setX(WINDOW.getWindowWidth()/2 - GHOST.getScreenWidth())
    GHOST.setY(WINDOW.getWindowHeight()/2 - GHOST.getScreenHeight())
    GHOST.setFlipX()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # INPUTS
        KEY_PRESSES = pygame.key.get_pressed()
        PIKACHU.move(KEY_PRESSES)
        PIKACHU.wrapAll(WINDOW.getWindowWidth(), WINDOW.getWindowHeight())
        PIKACHU.checkBoundaries(WINDOW.getWindowWidth(), WINDOW.getWindowHeight())
        GHOST.bounceAll(WINDOW.getWindowWidth(), WINDOW.getWindowHeight())
        GHOST.checkBoundaries(WINDOW.getWindowWidth(), WINDOW.getWindowHeight())


        # OUTPUTS
        WINDOW.clearScreen()
        WINDOW.getScreen().blit(PIKACHU.getScreen(), PIKACHU.getPOS())
        WINDOW.getScreen().blit(GHOST.getScreen(), GHOST.getPOS())
        WINDOW.updateFrame()
