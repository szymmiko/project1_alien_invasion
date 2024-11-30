import pygame


class Ship:
    """Class designed for ship management."""

    def __init__(self, ai_game):
        """Initialization of the ship and its initial position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # loading a ship image and getting its rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # each new ship appears in the center of the bottom edge of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # horizontal position of the ship stored as a float
        self.x = float(self.rect.x)

        # options indicating the movement of the ship
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """
        Updating the ship's position based on
        the options indicating its movement.
        """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # updating rect object based on self.x value
        self.rect.x = self.x

    def blitme(self):
        """Displaying the ship in its current position."""
        self.screen.blit(self.image, self.rect)
