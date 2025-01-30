import pygame
from settings import *

class PlasticPatrol:
    def __init__(self):
        logger.info("About to initialize a pygame")
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Plastic Patrol")
        logger.info("pygame initialized")


