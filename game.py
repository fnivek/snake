#! /usr/bin/env python

import pygame
import random

# Globals
kBackCol = (0, 0, 0)
kFoodCol = (0, 255, 0)
kSnakeCol = (255, 255, 255)
# Dimensions
width = 640
height = 640

class Food:
    """ This is food """

    def __init__(self, surface):
        self.surface = surface
        self.col = kFoodCol
        self.width = 10
        self.height = 10
        self.place()        

    def place(self):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)

        while self.surface.get_at((x, y)) is kSnakeCol:
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)

        self.x = x
        self.y = y

    def draw(self):
        for x in xrange(self.x - self.width / 2, self.x + self.width / 2):
            for y in xrange(self.y - self.height / 2, self.y + self.width / 2):
                self.surface.set_at((x, y), self.col)

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
        self.col = kSnakeCol
        self.width = 5
        self.height = 5

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

        col = self.surface.get_at((self.x, self.y))[:3]

        if col == self.col:
            self.crashed = True
        elif col == kFoodCol:
            f.place()
            self.length += 10

        self.body.insert(0, (self.x, self.y))

        if len(self.body) > self.length:
            self.body.pop()

    def draw(self):
        for x, y in self.body:
            for x2 in xrange(x - self.width / 2, x + self.width / 2):
                for y2 in xrange(y - self.height / 2, y + self.width / 2):
                    self.surface.set_at((x2, y2), self.col)


screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

# Our worm
w = Worm(screen, width / 2, height / 2, 50)
f = Food(screen)

# Main loop
while running:
    screen.fill((0, 0, 0))
    f.draw()
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
