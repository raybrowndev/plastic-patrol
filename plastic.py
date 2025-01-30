import pygame
from random import randint

class Plastic():

    def __init__(self, game):

        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load('assets/water-bottle.png')
        self.rect = self.image.get_rect()  

        #Where does it pop?
        self.rect.midtop = (randint(0,900), 0) #double-check if it should be midtop or something else
        self.y = float(self.rect.y)

    def update(self): 
        self.y -= self.settings.obstacle_speed
        self.rect.y = self.y

    def draw_plastic(self):
        self.screen.blit(self.image, self.rect)

