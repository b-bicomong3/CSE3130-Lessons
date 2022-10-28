# d_star.py

"""
Title: star-field
Author: Beatrix Bicomong
Date: 28-10-22
"""

if __name__ == "__main__":
    import pygame
    import random
    from a_template import Window
    from c_boxes import Box

    pygame.init()

    WINDOW = Window("Star Field", 800, 600, 30)
    BOXES = []
    for i in range(100):
        WIDTH = random.randrange(2, 6)
        BOXES.append(Box(WIDTH, WIDTH, random.randrange(WINDOW.getWindowWidth() - WIDTH),
                         random.randrange(WINDOW.getWindowHeight() - WIDTH)))

    while True:

        # INPUT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        PRESSED_KEYS = pygame.key.get_pressed()
        # PROCESSING
        for BOX in BOXES:
            BOX.moveBox(PRESSED_KEYS, WINDOW.getWindowWidth(), WINDOW.getWindowHeight())

        # OUTPUTS
        WINDOW.clearScreen()
        for BOX in BOXES:
            WINDOW.getScreen().blit(BOX.getBox(), BOX.getPOS())
        WINDOW.updateFrame()
