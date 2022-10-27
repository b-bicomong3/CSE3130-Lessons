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
    TEXT = Text("hello world")
    TEXT.setTextColor((0, 255, 0))
    TEXT.setTextSize(48)
    TEXT.setPOS(100, 150)

    while True:
        # INPUTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        # PROCESSING
        TEXT.setX(TEXT.getX() + 1)
        # OUTPUTS
        WINDOW.getScreen().fill((50, 50, 50))
        WINDOW.getScreen().blit(TEXT.getText(), TEXT.getPOS())
        WINDOW.updateFrame()
