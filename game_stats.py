class GameStats:
    """Monitoring statistical data in the game."""

    def __init__(self, ai_game):
        """Initialization of statistical data."""
        self.settings = ai_game.settings
        self.reset_stats()

        # launching the "Alien Invasion" game in inactive state
        self.game_active = False

    def reset_stats(self):
        """Initialization of statistical data that may change during
        the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
