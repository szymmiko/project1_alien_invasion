import pygame


class Ship:
    """Class designed for ship management."""

    def __init__(self, ai_game):
        """Initialization of the ship and its initial position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # loading a ship image and getting its rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # each new ship appears in the center of the bottom edge of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Displaying the ship in its current position."""
        self.screen.blit(self.image, self.rect)
