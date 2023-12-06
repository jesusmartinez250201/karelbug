import pygame

class Button:
    def __init__(self,x,y,image,screen):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.screen = screen
        self.clicked = False

    def draw(self):
        action = False


        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked is False:
                self.clicked = True
                action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        self.screen.blit(self.image, (self.rect.x, self.rect.y))

        return action