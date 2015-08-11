#! /usr/bin/env python

import pygame
import time

# Some variables
update_rate = 10
last_time = time.time()
width = 640
height = 640
num_lines = 10
y_line = [height - (height * i / num_lines) for i in range(num_lines)]
x_line = [width * i / num_lines for i in range(num_lines)]

# Initilize a surface
screen = pygame.display.set_mode((width, height))

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
    
mx, my = 0, 0

# Infinite loop
while True:
    # Time stuff
    now = time.time()
    step = now - last_time
    last_time = now

    # Event handling
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    elif event.type == pygame.MOUSEMOTION:
        mx, my = event.pos

    # Logic
    x_line = map(step_x, x_line)
    y_line = map(step_y, y_line)

    # Graphics
    color = [int(now * 1) % 512,
             int(now * 5) % 512,
             int(now * 10) % 512]
    color = map(wrap_color, color)

    screen.fill(color)
    for l in zip(x_line, y_line):
        pygame.draw.line(screen, map(invert_color, color), (mx, l[1]), (l[0], my))
    pygame.display.flip()