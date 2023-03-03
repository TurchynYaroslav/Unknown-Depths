import pygame
pygame.font.init()

class Text:
    def __init__(self,x,y,size,font,text,color):
        self.X = x
        self.Y = y
        self.SIZE = size
        self.FONT = font
        self.TEXT = text
        self.COLOR = color
        self.text = None
    def load_text(self):
        font = pygame.font.SysFont(self.FONT,self.SIZE)
        self.text = font.render(self.TEXT,False,self.COLOR)
    def show_text(self,screen):
        screen.blit(self.text,(self.X,self.Y))
