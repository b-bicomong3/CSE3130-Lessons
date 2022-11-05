# game.py in e_spooky

"""
title: the game engine
author: Beatrix Bicomong
date-created: 02-11-22 (Snow Day)
"""
import pygame
import random
from image_sprite import ImageSprite
from window import Window
from text import Text
from box import Box


class Game:

    def __init__(self):
        self.__SCORE = 0
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

        self.__PLAYER_LIVES = Text(f"Lives: {self.__PLAYER.getLives()}")
        self.__PLAYER_SCORE = Text(f"Score: {self.__PLAYER.getScore()}")
        self.__PLAYER_SCORE.setX(self.__WINDOW.getWindowWidth() - self.__PLAYER_SCORE.getScreenWidth() - 70)

        self.__ENEMIES = [ImageSprite("media/ghost.png")]
        self.__ENEMIES[0].setSpeed(5)
        self.__ENEMIES[0].setX(self.__WINDOW.getWindowWidth() // 2 - self.__ENEMIES[0].getScreenWidth() // 2)
        self.__ENEMIES[0].setY(self.__WINDOW.getWindowHeight() // 2 - self.__ENEMIES[0].getScreenHeight() // 2)

        self.__POWERUPS = [ImageSprite("media/peach.png")]

        self.__GAMEOVER_TEXT = Text("GAMEOVER")
        self.__GAMEOVER_TEXT.setSize(100)
        self.__GAMEOVER_TEXT.setPosition(self.__WINDOW.getWindowWidth(), self.__WINDOW.getWindowHeight())

    def run(self):
        while True:
            # INPUTS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            PRESSED_KEYS = pygame.key.get_pressed()
            # PROCESSING

            self.__PLAYER.move(PRESSED_KEYS)
            self.__PLAYER.checkBoundaries(self.__WINDOW.getWindowWidth(), self.__WINDOW.getWindowHeight(), 0,
                                          self.__TITLE.getScreenHeight())
            for ENEMY in self.__ENEMIES:
                ENEMY.bounceAll(self.__WINDOW.getWindowWidth(), self.__WINDOW.getWindowHeight(), 0,
                                self.__TITLE.getScreenHeight())
                if ENEMY.isCollision(self.__PLAYER.getScreen(),
                                     self.__PLAYER.getPOS()) and not self.__PLAYER.getColliding():
                    self.__PLAYER.loseLife()
                    self.__PLAYER.isColliding()
                    self.__PLAYER_LIVES.setText(f"Lives: {self.__PLAYER.getLives()}")
                elif not ENEMY.isCollision(self.__PLAYER.getScreen(), self.__PLAYER.getPOS()):
                    self.__PLAYER.notColliding()

            if self.__PLAYER.getLives():
                self.__SCORE += 1
                self.__PLAYER_SCORE.setText(f"Score: {self.__SCORE}")

            if self.__SCORE == random.randrange(100):
                self.__POWERUPS.append(ImageSprite())

            if self.__PLAYER.getLives() < 1:
                self.gameOver()

            # OUTPUTS

            self.__WINDOW.clearScreen()
            self.blitAll()
            self.__WINDOW.updateFrame()

    def blitAll(self):
        self.__WINDOW.getScreen().blit(self.__TITLE_BG.getScreen(), self.__TITLE_BG.getPOS())
        self.__WINDOW.getScreen().blit(self.__TITLE.getScreen(), self.__TITLE.getPOS())
        self.__WINDOW.getScreen().blit(self.__PLAYER_SCORE.getScreen(), self.__PLAYER_SCORE.getPOS())
        self.__WINDOW.getScreen().blit(self.__PLAYER_LIVES.getScreen(), self.__PLAYER_LIVES.getPOS())
        for POWERUP in self.__POWERUPS:
            self.__WINDOW.getScreen().blit(POWERUP.getScreen(), POWERUP.getPOS())
        self.__WINDOW.getScreen().blit(self.__GAMEOVER_TEXT.getScreen(), self.__GAMEOVER_TEXT.getPOS())
        for ENEMY in self.__ENEMIES:
            self.__WINDOW.getScreen().blit(ENEMY.getScreen(), ENEMY.getPOS())
        self.__WINDOW.getScreen().blit(self.__PLAYER.getScreen(), self.__PLAYER.getPOS())

    def gameOver(self):
        self.__PLAYER.setPosition(self.__WINDOW.getWindowWidth(), self.__WINDOW.getWindowHeight())
        for ENEMY in self.__ENEMIES:
            ENEMY.setPosition(self.__WINDOW.getWindowWidth(), self.__WINDOW.getWindowHeight())
        self.__GAMEOVER_TEXT.setPosition(
            self.__WINDOW.getWindowWidth() // 2 - self.__GAMEOVER_TEXT.getScreenWidth() // 2,
            self.__WINDOW.getWindowHeight() // 2 - self.__GAMEOVER_TEXT.getScreenHeight() // 2)


if __name__ == "__main__":
    pygame.init()
    GAME = Game()
    GAME.run()
