class GameStats:
    def __init__(self, c_settings):
        self.c_settings = c_settings
        self.reset_stats()
        # Start catch game in an active state
        self.game_active = True

    def reset_stats(self):
        self.left_tryes = self.c_settings.left_tryes
