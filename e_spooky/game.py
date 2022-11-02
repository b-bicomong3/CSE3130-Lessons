# game.py in e_spooky

"""
title: the game engine
author: Beatrix Bicomong
date-created: 02-11-22 (Snow Day)
"""
import pygame
from image_sprite import ImageSprite
from window import Window
from text import Text
from box import Box


class Game:

    def __init__(self):
        self.__WINDOW = Window("Spooky", 800, 600, 30)
        self.__TITLE = Text("Spooky!")
        self.__TITLE.setX(self.__WINDOW.getWindowWidth() // 2 - self.__TITLE.getScreenWidth() // 2)

        self.__TITLE_BG = Box()
        self.__TITLE_BG.setWidth(self.__WINDOW.getWindowWidth())
        self.__TITLE_BG.setHeight(self.__TITLE.getScreenHeight())
        self.__TITLE_BG.setColor((0, 0, 0))

        self.__PLAYER = ImageSprite("media/pikachu.png")
        self.__PLAYER.setScale(2)
        self.__PLAYER.setFlipX()
        self.__PLAYER.setSpeed(10)
        self.__PLAYER.setY(self.__TITLE.getScreenHeight())

        self.__ENEMIES = [ImageSprite("media/ghost_sprite.png")]
        self.__ENEMIES[0].setSpeed(5)
        self.__ENEMIES[0].setX(self.__WINDOW.getWindowWidth() // 2 - self.__ENEMIES[0].getScreenWidth() // 2)
        self.__ENEMIES[0].setY(self.__WINDOW.getWindowHeight() // 2 - self.__ENEMIES[0].getScreenHeight() // 2)

    def run(self):
        while True:
            # INPUTS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            KEYS_PRESSED = pygame.key.get_pressed()
            # PROCESSING

            self.__PLAYER.move(KEYS_PRESSED)
            self.__PLAYER.checkBoundaries(self.__WINDOW.getWindowWidth(), self.__WINDOW.getWindowHeight(), 0, self.__TITLE.getScreenHeight())
            for ENEMY in self.__ENEMIES:
                ENEMY.bounceAll(self.__WINDOW.getWindowWidth(), self.__WINDOW.getWindowHeight(), 0, self.__TITLE.getScreenHeight())

            # OUTPUTS

            self.__WINDOW.clearScreen()
            self.blitAll()
            self.__WINDOW.updateFrame()

    def blitAll(self):
        self.__WINDOW.getScreen().blit(self.__TITLE_BG.getScreen(), self.__TITLE_BG.getPOS())
        self.__WINDOW.getScreen().blit(self.__TITLE.getScreen(), self.__TITLE.getPOS())
        for ENEMY in self.__ENEMIES:
            self.__WINDOW.getScreen().blit(ENEMY.getScreen(), ENEMY.getPOS())
        self.__WINDOW.getScreen().blit(self.__PLAYER.getScreen(), self.__PLAYER.getPOS())


if __name__ == "__main__":
    pygame.init()
    GAME = Game()
    GAME.run()
