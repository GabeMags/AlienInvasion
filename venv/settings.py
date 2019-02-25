import pygame
class Settings():

    def __init__(self):
        """Initialize the game's static settings."""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (0, 0, 0)

        #Ship settings
        self.ship_limit = 0

        #Bullet settings
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (227, 48, 255)

        #Alien settings
        self.fleet_drop_speed = 5

        #Barrier settings
        self.barrier_number = 4

        #UFO settings
        self.ufo_speed_factor = 1

        self.last = pygame.time.get_ticks()
        self.cooldown = 5000

        #How quickly the game speeds up
        self.speedup_scale = 1.1

        #How quickly the alien point values increase
        self.score_scale = 1.5

        # Keep track of how many aliens I hit
        self.aliens_destroyed = 0

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 6
        self.alien_speed_factor = 1

        #fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        #ufo_direction of 1 represents right; -1 represents left.
        self.ufo_direction = 1

        #Scoring for all three types of aliens
        self.alien1_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien1_points = int(self.alien1_points * self.score_scale)