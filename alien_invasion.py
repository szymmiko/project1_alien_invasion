import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion():
    """A class designed to manage resources and game operations."""

    def __init__(self):
        """Initialization of the game and its resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Starting the main game loop."""
        while True:
            #waiting for a key or mouse button to be pressed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #screen refreshing during each loop iteration
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            #displaying the last modified screen
            pygame.display.flip()

if __name__ == '__main__':
    #creating a game instance and running it
    ai = AlienInvasion()
    ai.run_game()