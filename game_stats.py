class GameStats():
    """Отслеживание статистики для игры Alen Invasion."""
    
    def __init__(self,ai_game):
        """Инициирует статистику."""
        self.settings=ai_game.settings
        self.reset_states()

        # Игра Alien Invasion запускается в неактивном состоянии.
        self.game_active=False

        # Рекорд не должен сбрасываться
        self.high_score=0

    def reset_states(self):
        """Инициирует статистику, изменяющуюся в ходе игры"""
        self.ships_limit=self.settings.ship_limit
        self.score=0
