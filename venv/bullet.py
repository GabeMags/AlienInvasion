import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    #this class manages bullets fired from the ship
    def __init__(self, ai_settings, screen, ship, yoffset=0):
        #create a bullet object at the ship's current position
        super(Bullet, self).__init__()
        self.screen = screen

        #create a bullet rect at (0,0) and then set correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top - yoffset

        #store the bullet's position as a decimal value
        self.y = float(self.rect.y - yoffset)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        #move the bullet up to the screen
        self.y -= self.speed_factor

        #update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        #draw the bullet to the screen
        pygame.draw.rect(self.screen, self.color, self.rect)