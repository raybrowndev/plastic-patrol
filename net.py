import pygame
from pygame.sprite import Sprite
from settings import Settings

class Net:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings
        
        self.image = pygame.image.load('assets/net.png')
        self.image_flipped = pygame.transform.flip(self.image, True, False)
        
        self.rect = self.image.get_rect()  
        self.rect.midtop = self.screen_rect.midtop
        self.rect.y = 1
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_right = False
        self.moving_left = False
        
        self.facing_right = True

        def blitme(self):
            if self.facing_right:
                self.screen.blit(self.image, self.rect)
            else:
                self.screen.blit(self.image_flipped, self.rect)