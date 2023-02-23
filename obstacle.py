import pygame
import random
import sys

width = 400
height = 400

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

    def obs_colour(self):
        global Palette
        Palette = ['red', 'blue', 'green', 'yellow', 'red', 'blue', 'green', 'yellow']
        index = random.randint(0,len(Palette)-1)
        if index > 3:
            index -= 4
        r = Palette[index]
        s = Palette[index+1]
        t = Palette[index+2]
        u = Palette[index+3]
        return r, s, t, u

    def obs_shape(self):
        Shape = ['square', 'line', 'triangle', 'circle', 'cross']
        x = Shape[random.randint(0,len(Shape)-1)]
        return x

    def draw(self, colour, shape, screen, case):
        self.pos = (self.x, self.y)
        global part1, part2, part3, part4

        if shape == 'square':
            part1 = pygame.draw.line(screen, colour[0], (150, 150), (250, 150), 5)
            part2 = pygame.draw.line(screen, colour[1], (250, 150), (250, 250), 5)
            part3 = pygame.draw.line(screen, colour[2], (250, 250), (150, 250), 5)
            part4 = pygame.draw.line(screen, colour[3], (150, 250), (150, 150), 5)

        elif shape == 'line':
            part1 = pygame.draw.line(screen, colour[0], (0,200), (100, 200), 5)
            part2 = pygame.draw.line(screen, colour[1], (100, 200), (200, 200), 5)
            part3 = pygame.draw.line(screen, colour[2], (200, 200), (300, 200), 5)
            part4 = pygame.draw.line(screen, colour[3], (300, 200), (400, 200), 5)

        elif shape == 'triangle':
            part1 = pygame.draw.line(screen, colour[0], (150, 150), (200, 200), 5)
            part2 = pygame.draw.line(screen, colour[1], (200, 200), (250, 150), 5)
            part3 = pygame.draw.line(screen, colour[2], (250, 150), (150,150), 5)

        elif shape == 'circle':
            part1 = pygame.draw.circle(screen, colour[0], [200, 200], 50, 5, draw_top_right=True)
            part2 = pygame.draw.circle(screen, colour[1], [200, 200], 50, 5, draw_top_left=True)
            part3 = pygame.draw.circle(screen, colour[2], [200, 200], 50, 5, draw_bottom_left=True)
            part4 = pygame.draw.circle(screen, colour[3], [200, 200], 50, 5, draw_bottom_right=True)

        else:
            if case:
                part1 = pygame.draw.line(screen, colour[0], (150, 125), (150, 200), 5)
                part2 = pygame.draw.line(screen, colour[1], (225, 200), (150, 200), 5)
                part3 = pygame.draw.line(screen, colour[2], (150, 275), (150, 200), 5)
                part4 = pygame.draw.line(screen, colour[3], (75, 200), (150, 200), 5)
                
            else:
                part1 = pygame.draw.line(screen, colour[0], (250, 125), (250, 200), 5)
                part2 = pygame.draw.line(screen, colour[1], (325, 200), (250, 200), 5)
                part3 = pygame.draw.line(screen, colour[2], (250, 275), (250, 200), 5)
                part4 = pygame.draw.line(screen, colour[3], (175, 200), (250, 200), 5)


def main(screen):
    clock = pygame.time.Clock()  # for speed

    obstacle = Obstacle(250, 200, screen)
    colour = list(obstacle.obs_colour())
    shape = obstacle.obs_shape()
    case = random.randint(0, 2)

    run = True
    angle = 0
    while run:
        screen.fill((0, 0, 0))
        obstacle.draw(colour, shape, screen, case)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # rotated_part1 = pygame.transform.rotate(part1, angle)
        # rotated_part2 = pygame.transform.rotate(part2, angle)
        # rotated_part3 = pygame.transform.rotate(part3, angle)
        # rotated_part4 = pygame.transform.rotate(part4, angle)

        pygame.display.update()
        clock.tick(FPS)
        angle += 1


if __name__ == "__main__":
    main(screen)
