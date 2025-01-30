import pygame
from settings import *
from plastic import Plastic
from net import Net

class PlasticPatrol:

    def __init__(self):
        """Overall class to manage game assets and behavior."""

        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.SCREEN_WIDTH,self.settings.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.plastic = pygame.sprite.Group()
        self.net = Net(self)
        self.background = pygame.transform.scale(pygame.image.load('assets/underwater.png'),(self.settings.SCREEN_WIDTH,self.settings.SCREEN_HEIGHT))


    def run_game(self):
        """Start the main loop for the game."""
        while True:
        # Process player inputs.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit

    # Do logical updates here.
    # ...

            self.screen.fill("blue")  # Fill the display with a solid color
            self.screen.blit(self.background,game.screen.get_rect())
            plastic = Plastic(self)
            plastic.draw_plastic()
            
            

    # Render the graphics here.
    # ...

            pygame.display.flip()  # Refresh on-screen display
            self.clock.tick(60)


if __name__ == '__main__':
    # game = PlasticPatrol()
    # Make a game instance, and run the game.
    game = PlasticPatrol()
    game.run_game()