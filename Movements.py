import pygame

class Move:
    def __init__(self,x,y,image,screen):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.screen = screen
        self.clicked = False

    def draw(self):

        self.screen.blit(self.image, (self.rect.x, self.rect.y))

