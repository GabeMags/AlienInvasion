import pygame.font

class HighScoreWindow():

    def __init__(self, ai_settings, screen, stats):
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the properties of the high score screen
        self.window_width, self.window_height = 600, 500
        self.high_score_window_color = (46, 19, 56)
        self.text_color = (255, 255, 255)
        self.hs_message_font = pygame.font.SysFont('Courier New', 27, True)
        self.hs_font = pygame.font.SysFont('Courier New', 27)

        # Build the window rect object and center it
        self.hs_window_rect = pygame.Rect(0,0, self.window_width, self.window_height)
        self.hs_window_rect.centerx = self.screen_rect.centerx
        self.hs_window_rect.centery = self.screen_rect.centery

    def draw_high_score_window(self, stats):
        self.screen.fill(self.high_score_window_color, self.screen_rect)
        self.high_scores = self.hs_font.render(str(stats.high_score), True, self.text_color, None)
        self.high_scores_2 = self.hs_font.render(str(stats.high_score_2), True, self.text_color, None)
        self.screen.blit(self.high_scores, (100, 100))
        self.screen.blit(self.high_scores_2, (100, 200))




    # def show_high_scores(self):


