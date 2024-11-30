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

        # options indicating the movement of the ship
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """
        Updating the ship's position based on
        the options indicating its movement.
        """
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        """Displaying the ship in its current position."""
        self.screen.blit(self.image, self.rect)
