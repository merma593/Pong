import pygame
import sys
from pygame.locals import *

class Ball(object):

    def __init__(self, x, y, vx, vy, radius, colour):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.colour = colour

    def move(self):
        self.x += self.vx
        self.y += self.vy
        

class Game(object):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    #Initialising game object
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640,480))

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            self.draw()

    def draw(self):
        self.screen.fill(Game.WHITE)
        pygame.display.update()

if __name__ == "__main__":   
    Game().play()
