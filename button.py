import pygame.font


class Button:
    """A class designed to represent a button."""

    def __init__(self, ai_game, msg):
        """Button attributes initialization."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # defining button dimensions and properties
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # creating a button rect and centering it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # the message displayed by the button
        # only needs to be prepared once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Placing the message in the generated image and centering the
        text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # displaying an empty button and then a message on it
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
