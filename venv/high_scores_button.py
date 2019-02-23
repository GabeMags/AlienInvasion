import pygame.font

class HighScoresButton():

    def __init__(self, ai_settings, screen, hs_msg):
        """Initialize high scores button attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the dimensions and properties of the high scores button.
        self.width, self.height = 200, 50
        self.hs_button_color = (200, 100, 200)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)

        #Build the hs button's rect object and center it at the bottom below the play button
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.centerx = 600
        self.rect.centery = 610

        # The high score button message needs to be prepped only once
        self.prep_hs_msg(hs_msg)

    def prep_hs_msg(self, hs_msg):
        """Turn hs_msg into a rendered imaged and center text on the hs button"""
        self.hs_msg_image = self.font.render(hs_msg, True, self.text_color, self.hs_button_color)
        self.hs_msg_image_rect = self.hs_msg_image.get_rect()
        self.hs_msg_image_rect.center = self.rect.center

    def draw_hs_button(self):
        # Draw a blank hs button and then draw its message.
        self.screen.fill(self.hs_button_color, self.rect)
        self.screen.blit(self.hs_msg_image, self.hs_msg_image_rect)


