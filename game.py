#! /usr/bin/env python

import pygame
import time

# Initilize a surface
screen = pygame.display.set_mode((640, 400))

def wrap_color(c):
    if c >= 256:
        return 511 - c
    else:
        return c

# Infinite loop
while True:

    # Event handling
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    # Graphics
    color = [int(time.time() * 1) % 512,
             int(time.time() * 5) % 512,
             int(time.time() * 10) % 512]
    color = map(wrap_color, color)

    screen.fill(color)
    pygame.display.flip()