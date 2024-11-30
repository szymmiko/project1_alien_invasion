class Settings:
    """Class for storing all game settings."""

    def __init__(self):
        """Initialization of game settings."""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed = 1.5