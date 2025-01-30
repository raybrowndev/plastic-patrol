import pygame
from settings import *

class PlasticPatrol:
    def __init__(self):

        pygame.init()
        settings = Settings()
        screen = pygame.display.set_mode((settings.SCREEN_WIDTH,settings.SCREEN_HEIGHT))

        clock = pygame.time.Clock()

        while True:
        # Process player inputs.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit

    # Do logical updates here.
    # ...

            screen.fill("blue")  # Fill the display with a solid color

    # Render the graphics here.
    # ...

            pygame.display.flip()  # Refresh on-screen display
            clock.tick(60)


if __name__ == '__main__':
    game = PlasticPatrol()
