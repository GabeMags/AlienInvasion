import pygame

from pygame.sprite import Sprite

class Barrier():
    #A class to represent a single barrier shield

    def __init__(self, ai_settings, screen):
        #Initialize the barrier and set its position in the game
        self.screen = screen
        self.ai_settings = ai_settings

        #Load the barrier image and set its rect attribute
        self.barrier1_image = pygame.image.load('images/barrier_1.png')
        self.barrier2_image = pygame.image.load('images/barrier_1.png')
        self.barrier3_image = pygame.image.load('images/barrier_1.png')
        self.barrier4_image = pygame.image.load('images/barrier_1.png')

        self.barrier1_rect = self.barrier1_image.get_rect()
        self.barrier2_rect = self.barrier1_image.get_rect()
        self.barrier3_rect = self.barrier1_image.get_rect()
        self.barrier4_rect = self.barrier1_image.get_rect()

        #Place each barrier near the bottom of the screen (numbered from right to left)
        # BARRIER 1
        self.barrier1_rect.centerx = 200
        self.barrier1_rect.centery = 500
        # BARRIER 2
        self.barrier2_rect.centerx = 400
        self.barrier2_rect.centery = 500
        # BARRIER 3
        self.barrier3_rect.centerx = 600
        self.barrier3_rect.centery = 500
        # BARRIER 4
        self.barrier4_rect.centerx = 800
        self.barrier4_rect.centery = 500


    def blitme(self):
        #blit the barriers onto the screen
        self.screen.blit(self.barrier1_image, self.barrier1_rect)
        self.screen.blit(self.barrier2_image, self.barrier2_rect)
        self.screen.blit(self.barrier3_image, self.barrier3_rect)
        self.screen.blit(self.barrier4_image, self.barrier4_rect)






















