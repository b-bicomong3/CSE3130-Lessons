# b_hello_world

"""
Title: playing with text
Author: Beatrix Bicomong
Date: 26-10-2022
"""

import pygame
from a_template import Window, Text

if __name__ == "__main__":
    pygame.init()

    WINDOW = Window("Hello World", 800, 600, 30)
    WINDOW.setColor((0, 0, 255))
    TEXT = Text("(^3^)")
    TEXT.setTextColor((0, 255, 0))
    TEXT.setTextSize(48)
    TEXT.setPOS(TEXT.setCentreX(WINDOW.getWindowWidth()), TEXT.setCentreY(WINDOW.getWindowHeight()))
    TEXT.setSpeed(10)

    TEXT2 = Text("(0_0)")
    TEXT2.setPOS(100, 300)
    TEXT2.setSpeed(10)

    while True:
        # INPUTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        # PROCESSING
        # TEXT.marqueeX(WINDOW.getWindowWidth())
        # TEXT2.marqueeX(WINDOW.getWindowWidth())
        TEXT.bounceX(WINDOW.getWindowWidth())
        TEXT2.bounceX(WINDOW.getWindowWidth())
        # TEXT.marqueeY(WINDOW.getWindowWidth())
        # TEXT2.marqueeY(WINDOW.getWindowWidth())
        TEXT.bounceY(WINDOW.getWindowHeight())
        TEXT2.bounceY(WINDOW.getWindowHeight())

        # OUTPUTS
        WINDOW.clearScreen()
        WINDOW.getScreen().blit(TEXT.getText(), TEXT.getPOS())
        WINDOW.getScreen().blit(TEXT2.getText(), TEXT2.getPOS())
        WINDOW.updateFrame()
