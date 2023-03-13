import pygame
import random
import sys

width = 800
height = 500

pygame.display.init()
screen = pygame.display.set_mode((width, height))
FPS = 60

class Floor(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, screen):
        super(Floor, self).__init__()
        self.surface = screen
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = pygame.draw.rect(self.surface,(255,255,255), pygame.Rect(self.x, self.y, self.w, self.h))

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        self.surface = screen
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
        self.r = 25

    def draw(self, colour, shape, screen, case):
        self.pos = (self.x, self.y)
        global inipipe_top, inipipe_bottom, midpipe_top, midpipe_bottom, finpipe_top, finpipe_bottom

        pipe_width = 50

        inipipe_top = pygame.draw.rect(screen, colour, pygame.Rect(inipipe_x, 0, pipe_width, inipipe_len))
        inipipe_bottom = pygame.draw.rect(screen, colour, pygame.Rect(inipipe_x, (inipipe_len + 100), pipe_width, 1000))

        midpipe_top = pygame.draw.rect(screen, colour, pygame.Rect((inipipe_x + 200), 0, pipe_width, midpipe_len))
        midpipe_bottom = pygame.draw.rect(screen, colour,
                                          pygame.Rect((inipipe_x + 200), (midpipe_len + 100), pipe_width, 1000))

        finpipe_top = pygame.draw.rect(screen, colour, pygame.Rect((inipipe_x + 400), 0, pipe_width, finpipe_len))
        finpipe_bottom = pygame.draw.rect(screen, colour,
                                          pygame.Rect((inipipe_x + 400), (finpipe_len + 100), pipe_width, 1000))


def main(screen):
    clock = pygame.time.Clock()  # for speed

    global inipipe_len, midpipe_len, finpipe_len, inipipe_x
    obstacle = Obstacle(450, 350, screen)
    colour = "grey"
    shape = "pipe"
    case = random.randint(0, 2)
    inipipe_len = random.randint(0, 350)
    midpipe_len = random.randint(0, 350)
    finpipe_len = random.randint(0, 350)
    inipipe_x = random.randint(400, 500)

    run = True

    while run:
        screen.fill((0, 0, 0))

        obstacle.draw(colour, shape, screen, case)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        inipipe_x -= 1
        if inipipe_x == 200:
            inipipe_x += 200
            inipipe_len = midpipe_len
            midpipe_len = finpipe_len
            finpipe_len = random.randint(0, 350)

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main(screen)
