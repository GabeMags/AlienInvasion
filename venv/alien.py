import pygame
from pygame.sprite import Sprite
from spritesheet import Spritesheet
import math

class Alien(Sprite):
    #a class to represent a single alien in the fleet

    def __init__(self, ai_settings, screen):
        #initialize the alien and set its starting position
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = Spritesheet('images/spritesheet.png')
        self.images = []
        self.index = 0
        self.images.append(self.image.image_at((640, 0, 64, 64), colorkey=(0, 0, 0, 1)))
        self.images.append(self.image.image_at((704, 0, 64, 64), colorkey=(0, 0, 0, 1)))
        self.image = self.images[self.index]

        #load the alien image and set its rect attribute
        self.rect = self.image.get_rect()

        #start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the alien's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        #return true if alien is at edge of screen
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        #move the alien right or left
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x

        self.index += .02
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[math.floor(self.index)]

class Alien_2(Sprite):
    #a class to represent a single alien in the fleet

    def __init__(self, ai_settings, screen):
        #initialize the alien and set its starting position
        super(Alien_2, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = Spritesheet('images/spritesheet.png')
        self.images = []
        self.index = 0
        self.images.append(self.image.image_at((64, 0, 64, 64), colorkey=(0, 0, 0, 1)))
        self.images.append(self.image.image_at((128, 0, 64, 64), colorkey=(0, 0, 0, 1)))

        self.image = self.images[self.index]

        #load the alien image and set its rect attribute
        self.rect = self.image.get_rect()

        #start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the alien's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        #return true if alien is at edge of screen
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        #move the alien right or left
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x

        self.index += .02
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[math.floor(self.index)]

class Alien_3(Sprite):
    #a class to represent a single alien in the fleet

    def __init__(self, ai_settings, screen):
        #initialize the alien and set its starting position
        super(Alien_3, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = Spritesheet('images/spritesheet.png')
        self.images = []
        self.index = 0
        self.images.append(self.image.image_at((192, 0, 64, 64), colorkey=(0, 0, 0, 1)))
        self.images.append(self.image.image_at((256, 0, 64, 64), colorkey=(0, 0, 0, 1)))
        self.image = self.images[self.index]

        #load the alien image and set its rect attribute
        self.rect = self.image.get_rect()

        #start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the alien's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        #return true if alien is at edge of screen
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        #move the alien right or left
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x

        self.index += .02
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[math.floor(self.index)]
