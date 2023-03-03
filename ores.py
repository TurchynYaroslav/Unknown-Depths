import pygame
import os
pygame.init()

class Ores():
    def __init__(self, x, y, width, height, path,type):
        self.X = x
        self.Y = y
        self.WIDTH = width
        self.HEIGHT = height
        self.PATH = path
        self.TYPE = type
        self.load_image()
    def load_image(self):
        path = os.path.abspath(__file__ + "/..")
        path = path + self.PATH
        self.IMG = pygame.image.load(path)
        self.IMG = pygame.transform.scale(self.IMG, (self.WIDTH, self.HEIGHT))
    def show_image(self,screen):
        screen.blit(self.IMG, (self.X, self.Y)) 



