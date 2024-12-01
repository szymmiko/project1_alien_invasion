import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class designed to manage the fired bullets by the ship."""

    def __init__(self, ai_game):
        """Creating a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # creating a bullet rect at point (0, 0)
        self.rect = pygame.Rect(0, 0,
                                self.settings.bullet_width,
                                self.settings.bullet_height)
        # defining the appropriate position for bullet
        self.rect.midtop = ai_game.ship.rect.midtop

        # vertical position of the bullet stored as a float
        self.y = float(self.rect.y)

    def update(self):
        """Bullet movement around the screen."""
        # update of bullet position
        self.y -= self.settings.bullet_speed
        # update of bullet rectangle position
        self.rect.y = self.y

    def draw_bullet(self):
        """Drawing the bullet on the screen."""
        pygame.draw.rect(self.screen, self.settings.bullet_color, self.rect)
