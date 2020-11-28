import pygame
from typing import List, Optional
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN,
                           QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION,
                           MOUSEWHEEL)
import random

pygame.init()

SCREEN_WIDTH = 1260
SCREEN_HEIGHT =1260

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

running = True


class Blip:
    """"""

    origin: List
    surf: pygame.Surface

    def __init__(self, origin: List[int], surf: pygame.Surface):
        self.origin = origin
        self.surf = surf


blips = []

for i in range(200):
    new_blip = Blip([i, i], pygame.Surface((2, 2)))
    new_blip.rect = new_blip.surf.get_rect(
        topleft=(
            i,
            i
        )
    )
    new_blip.surf.fill(256, 256, 256)
    blips.append(new_blip)





while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == MOUSEMOTION:
            pos = pygame.mouse.get_pos()

        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

    screen.fill((0, 0, 0))

    for blip in blips:
        screen.blit(blip.surf, blip.rect)

    pygame.display.flip()

pygame.quit()


