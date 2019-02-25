class GameStats():
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.high_score_2 = 0
        self.high_score_3 = 0

        #Start Alien Invasion in an active state.
        self.game_active = False

        #High score should never be reset.
        self.high_score = 0

        # Keep track of whether or not the game has run for the first time already
        self.first_playthrough = False
        self.game_ends = False
        self.high_scores_button_clicked = False

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1