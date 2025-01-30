#import sys
import pygame
import random
#import time
#import math
from settings import Settings
from net import Net
from plastic import Plastic
from fish import Fish
from button import Button

class PlasticPatrol:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        #self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.user = Net(self)
        self.plastic = pygame.sprite.Group()

        self.distance = 0 #double-check

        self.fish = pygame.sprite.Group()

        pygame.display.set_caption("Tech Fighters")
        # Game states
        self.game_active = False  # Track whether the game is running
        self.button = Button(self, "Start")  # Create a start button

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.game_active:
                self.plastic.update()
                self.fish.update()
                self.net.update()
                self._load_obstacle()
                self._delete_obstacle()
                self._load_fish()
                self._collision() 
                self._score()
                self.settings.plastic_speed =  1 + self.distance / 1000
                self.settings.fish_speed = 1+  self.distance / 1000 
                if self.settings.plastic_load > 10:
                    self.settings.plastic_load = 100 #-  10 * math.ceil(self.distance / 1000) 
                print(self.settings.plastic_load)
             

                self.end_game()

            self._update_screen()
            #self.clock.tick(60)


##below is not yet checked
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and self.game_active:
                if event.key == pygame.K_RIGHT:
                    self.user.moving_right = True
                    self.user.facing_right = True
                elif event.key == pygame.K_LEFT:
                    self.user.moving_left = True
                    self.user.facing_right = False
            elif event.type == pygame.KEYUP and self.game_active:
                if event.key == pygame.K_RIGHT:
                    self.user.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.user.moving_left = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.button.rect.collidepoint(mouse_pos) and not self.game_active:
                    # Start the game
                    self.time_started = time.time
                    self.game_active = True

    def _update_screen(self):
        self.screen.fill(self.settings.bg_colour)

        if self.game_active:
            for obstacle in self.obstacles.sprites():
                obstacle.draw_obstacle()
            for life in self.lives.sprites():
                life.draw_life()
            self.user.blitme()
            self._score()
            
        else:
            self.button.draw()  # Draw the start button when the game is inactive
        pygame.display.flip()
    
    def _load_obstacle(self):
        if random.randint(0, self.settings.obstacle_load) == 3:
            new_obstacle = Obstacle(self)
            self.obstacles.add(new_obstacle)

    def _delete_obstacle(self):
        for obstacle in self.obstacles.copy():
            if obstacle.rect.bottom <= 0:
                self.obstacles.remove(obstacle)

#Lives
    def _load_life(self):
        if random.randint(0,200) == 3:
            new_life = Life(self)
            self.lives.add(new_life)

    def _delete_life(self):
        for life in self.lives.copy():
            if life.rect.bottom <= 0:
                self.lives.remove(life)
    
    def _collision(self):
        if pygame.sprite.spritecollide(self.user, self.obstacles, True):
            self.user.collision(50)
        if pygame.sprite.spritecollide(self.user, self.lives, True):
            self.user.collision(-50)
    
   #score 
    def _score(self):
        self.distance += self.settings.speed
        font = pygame.font.Font(None, 36)  # Use default font, size 36
        distance_text = font.render(f"Distance: {self.distance}", True, (255, 255, 255))  # White color
        self.screen.blit(distance_text, (10, 10))  # Top-left corner
        
    def end_game(self):
        if self.user.rect.y >= 800:
            print("THIS SHOULD BE GAME OVER")
            font = pygame.font.Font(None, 74)  # Create a font object (None uses default font)
            game_over_text = font.render(f"Game Over", True, (255, 0, 0))  # Render the text in red
            score_text = font.render(f"Score: {self.distance}", True, (255, 0, 0))
            game_over_rect = game_over_text.get_rect(center=(self.settings.screen_width // 2, self.settings.screen_height // 2))
            score_rect = score_text.get_rect(center=(self.settings.screen_width // 2, self.settings.screen_height // 1.7))
            self.screen.blit(game_over_text, game_over_rect)  # Draw text at the center of the screen
            self.screen.blit(score_text, score_rect)  # Draw text at the center of the screen
            pygame.display.flip()
            pygame.time.delay(3000)  # Pause for 3 seconds before exiting

            self.distance = 0
            self.user.rect.y = 1
            self.user.moving_left = False
            self.user.moving_right = False
            self.settings.obstacle_speed = 1.0
            self.settings.life_speed = 1.0
            self.game_active = False
    
if __name__ == '__main__':
    # Make a game instance, and run the game.
    game = TechFighters()
    game.run_game()
