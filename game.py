#! /usr/bin/env python

import pygame
import time
import random
from collections import deque

# Some variables
update_rate = 10
last_time = time.time()
width = 640
height = 640
num_lines = 10
y_line = [height - (height * i / num_lines) for i in range(num_lines)]
x_line = [width * i / num_lines for i in range(num_lines)]
mx, my = 0, 0
running = True
pixels_to_keep = 1000
pixels = deque()

# Initilize a surface
screen = pygame.display.set_mode((width, height))

# Initilize a clock
clock = pygame.time.Clock()

def wrap_color(c):
    if c >= 256:
        return 511 - c
    else:
        return c

def invert_color(c):
    return 255 - c 

def step_x(x):
    x = x + update_rate * 25.87654 * step
    if x > width:
        x = 0
    return x

def step_y(y):
    y = y - update_rate * 10.867 * step
    if y < 0:
        y = height
    return y
    


# Infinite loop
while running:
    # Time stuff
    now = time.time()
    step = now - last_time
    last_time = now

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.MOUSEMOTION:
            mx, my = event.pos

    if not running:
        break

    # Logic
    x_line = map(step_x, x_line)
    y_line = map(step_y, y_line)

    for i in xrange(100):
        rgb = [random.randint(0, 255) for x in range(3)]
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)

        pixels.append([(x, y), rgb])
        if len(pixels) > pixels_to_keep:
            pixels.popleft()

    # Graphics
    color = [int(now * 1) % 512,
             int(now * 5) % 512,
             int(now * 10) % 512]
    color = map(wrap_color, color)

    # Draw backround
    screen.fill(color)

    # Draw Lines
    for l in zip(x_line, y_line):
        pygame.draw.line(screen, map(invert_color, color), (mx, l[1]), (l[0], my))

    # Draw pixels
    for p in pixels:
        screen.set_at(p[0], p[1])

    # Flip the screen
    pygame.display.flip()

    # Sleep 1/24 of a second
    clock.tick(24)