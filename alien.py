import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class representing a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initializing the alien and defining its initial position."""
        super().__init__()
        self.screen = ai_game.screen

        # loading an alien image and defining its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # placing a new alien near the top left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # the exact horizontal position of the alien stored as a float
        self.x = float(self.rect.x)
