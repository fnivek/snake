#! /usr/bin/env python

import pygame

class Worm:
    """ This be my worm!"""

    def __init__(self, surface, x, y, length):
        self.surface = surface
        self.x = x
        self.y = y
        self.length = length
        self.dir_x = 0
        self.dir_y = -1
        self.body = []
        self.crashed = False
        self.lifetime = 0

    def key_event(self, event):
        """ Handle keyboard events """
        if event.key == pygame.K_UP and self.dir_y != 1:
            self.dir_x = 0
            self.dir_y = -1
        elif event.key == pygame.K_DOWN and self.dir_y != -1:
            self.dir_x = 0
            self.dir_y = 1
        elif event.key == pygame.K_LEFT and self.dir_x != 1:
            self.dir_x = -1
            self.dir_y = 0
        elif event.key == pygame.K_RIGHT and self.dir_x != -1:
            self.dir_x = 1
            self.dir_y = 0

    def move(self):
        self.x += self.dir_x
        self.y += self.dir_y

        if (self.x, self.y) in self.body:
            self.crashed = True
        else:
            self.lifetime += 1
            if not (self.lifetime % 10):
                self.length += 1

        self.body.insert(0, (self.x, self.y))

        if len(self.body) > self.length:
            self.body.pop()

    def draw(self):
        for x, y in self.body:
            self.surface.set_at((x, y), (255, 255, 255))


# Dimensions
width = 640
height = 640

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

# Our worm
w = Worm(screen, width / 2, height / 2, 50)

# Main loop
while running:
    screen.fill((0, 0, 0))
    w.move()
    w.draw()

    if w.crashed or w.x <= 0 or w.x >= width - 1 or w.y <= 0 or w.y >= height - 1:
        print 'Crash!'
        running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            w.key_event(event)

    pygame.display.flip()
    clock.tick(240)
