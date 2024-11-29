import sys

import pygame

class AlienInvasion():
    """A class designed to manage resources and game operations."""

    def __init__(self):
        """Initialization of the game and its resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien invasion")

    def run_game(self):
        """Starting the main game loop."""
        while True:
            #waiting for a key or mouse button to be pressed
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    sys.exit()

        #displaying the last modified screen
        pygame.display.flip()

if __name__ == '__main__':
    #creating a game instance and running it
    ai = AlienInvasion()
    ai.run_game()