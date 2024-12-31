import pygame.font


class Scoreboard:
    """A class designed to present scoring information."""

    def __init__(self, ai_game):
        """Initialization of scoring attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # font settings for scoring information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # preparation of initial images with scoring
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        """Converting scores to generated image."""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str,
                                            True,
                                            self.text_color,
                                            self.settings.bg_color)

        # displaying the score in the upper right corner of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Converting high score to generated image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str,
                                                 True,
                                                 self.text_color,
                                                 self.settings.bg_color)

        # displaying the high score in the game
        # in the middle of the screen at the top edge
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        """Displaying the scores on the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def check_high_score(self):
        """Checking if we have a new best score achieved in the game."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
