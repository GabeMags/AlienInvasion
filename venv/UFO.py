import pygame
from pygame.sprite import Sprite

class UFO(Sprite):
    """a class to represent a single UFO"""

    def __init__(self, ai_settings, screen):
     """Initialize the UFO and set its starting position"""
     super(UFO, self).__init__()
     self.screen = screen
     self.ai_settings = ai_settings
     self.spawn_timer = 0
     self.spawn_frequency = 10000 #miliseconds

     #load the UFO image and set its rect attribute
     self.image = pygame.image.load('images/ufo_0.png')
     self.rect = self.image.get_rect()

     #start each UFO near the top right of the screen
     self.rect.x = 0 - self.rect.width
     self.rect.y = self.rect.height

     #Store the UFO's exact position
     self.x = float(self.rect.x)


    def blitme(self):
        """Draw the UFO at its current locatiom"""
        self.screen.blit(self.image, self.rect)


    def check_edges(self):
        """Return true if the UFO is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.left >= screen_rect.right:
            return True


    def update(self):
        """Move the UFO right or left"""
        self.rect.x = self.x
        self.x += (self.ai_settings.ufo_speed_factor *
                       self.ai_settings.ufo_direction)

