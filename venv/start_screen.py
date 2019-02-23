import pygame.font

class StartScreen():

    def __init__(self, ai_settings, screen, aliens, game_title, alien_1_score, alien_2_score, alien_3_score, ufo_score, creator_name):
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the properties of the start screen, game title, and scoring for aliens
        self.width, self.height = 400, 100
        self.start_screen_color = (46, 9, 56)
        self.text_color = (255, 255, 255)
        self.creator_credit_text_color = (131, 132, 135)
        self.font = pygame.font.SysFont('Impact', 84)
        self.score_font = pygame.font.SysFont('Courier New', 27)
        self.credit_font = pygame.font.SysFont('Courier New', 14)

        # Build the game title's rect object and center it at the top of the start screen
        self.title_rect = pygame.Rect(0,0, self.width, self.height)
        self.title_rect.centerx = 600
        self.title_rect.centery = 80

        # Build the alien scores TEXT OBJECTS
        self.alien_1_score_rect = pygame.Rect(0,0, self.width, self.height)
        self.alien_1_score_rect.centerx = 630
        self.alien_1_score_rect.centery = 200

        self.alien_2_score_rect = pygame.Rect(0,0, self.width, self.height)
        self.alien_2_score_rect.centerx = 640
        self.alien_2_score_rect.centery = 275

        self.alien_3_score_rect = pygame.Rect(0,0, self.width, self.height)
        self.alien_3_score_rect.centerx = 640
        self.alien_3_score_rect.centery = 350

        self.ufo_score_rect = pygame.Rect(0,0, self.width, self.height)
        self.ufo_score_rect.centerx = 640
        self.ufo_score_rect.centery = 425

        # Simple credit text
        self.creator_credit_rect = pygame.Rect(0,0, self.width, self.height)
        self.creator_credit_rect.centerx = self.screen_rect.centerx
        self.creator_credit_rect.centery = 680

        #Build the title aliens SPRITES
        # ALIEN 1 (SKULL)
        self.alien1_image = pygame.image.load('images/skull_1.png')
        self.alien1_rect = self.alien1_image.get_rect()
        self.alien1_rect.centerx = 540
        self.alien1_rect.centery = 200
        # ALIEN 2 (GHOST)
        self.alien2_image = pygame.image.load('images/alien2_0.png')
        self.alien2_rect = self.alien2_image.get_rect()
        self.alien2_rect.centerx = 540
        self.alien2_rect.centery = 275
        # ALIEN 3 (DEATH CLOUD)
        self.alien3_image = pygame.image.load('images/alien3_1.png')
        self.alien3_rect = self.alien3_image.get_rect()
        self.alien3_rect.centerx = 540
        self.alien3_rect.centery = 350
        # UFO
        self.ufo_image = pygame.image.load('images/ufo_1.png')
        self.ufo_rect = self.ufo_image.get_rect()
        self.ufo_rect.centerx = 540
        self.ufo_rect.centery = 425

        # The game title and title aliens needs to be prepped only once.
        self.prep_game_title(game_title, alien_1_score, alien_2_score, alien_3_score, ufo_score, creator_name)
        self.draw_title_aliens()

    def prep_game_title(self, game_title, alien_1_score, alien_2_score, alien_3_score, ufo_score, creator_name):
        self.title_image = self.font.render(game_title, True, self.text_color, None)
        self.title_image_rect = self.title_image.get_rect()
        self.title_image_rect.center = self.title_rect.center

        # Alien 1 score image
        self.alien_1_score_image = self.score_font.render(alien_1_score, True, self.text_color, None)
        self.alien_1_score_image_rect = self.alien_1_score_image.get_rect()
        self.alien_1_score_image_rect.center = self.alien_1_score_rect.center

        # Alien 2 score image
        self.alien_2_score_image = self.score_font.render(alien_2_score, True, self.text_color, None)
        self.alien_2_score_image_rect = self.alien_2_score_image.get_rect()
        self.alien_2_score_image_rect.center = self.alien_2_score_rect.center

        # Alien 3 score image
        self.alien_3_score_image = self.score_font.render(alien_3_score, True, self.text_color, None)
        self.alien_3_score_image_rect = self.alien_3_score_image.get_rect()
        self.alien_3_score_image_rect.center = self.alien_3_score_rect.center

        #UFO score image
        self.ufo_score_image = self.score_font.render(ufo_score, True, self.text_color, None)
        self.ufo_score_image_rect = self.ufo_score_image.get_rect()
        self.ufo_score_image_rect.center = self.ufo_score_rect.center

        # Creator credit image
        self.creator_credit_image = self.credit_font.render(creator_name, False, self.creator_credit_text_color, None)
        self.creator_credit_image_rect = self.creator_credit_image.get_rect()
        self.creator_credit_image_rect.center = self.creator_credit_rect.center

    def draw_start_screen(self):
        self.screen.fill(self.start_screen_color, self.screen_rect)
        self.screen.blit(self.title_image, self.title_image_rect)
        self.screen.blit(self.alien_1_score_image, self.alien_1_score_image_rect)
        self.screen.blit(self.alien_2_score_image, self.alien_2_score_image_rect)
        self.screen.blit(self.alien_3_score_image, self.alien_3_score_image_rect)
        self.screen.blit(self.ufo_score_image, self.ufo_score_image_rect)
        self.screen.blit(self.creator_credit_image, self.creator_credit_image_rect)

    def draw_title_aliens(self):
        self.screen.blit(self.alien1_image, self.alien1_rect)
        self.screen.blit(self.alien2_image, self.alien2_rect)
        self.screen.blit(self.alien3_image, self.alien3_rect)
        self.screen.blit(self.ufo_image, self.ufo_rect)




