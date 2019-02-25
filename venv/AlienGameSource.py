import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from high_scores_button import HighScoresButton
from ship import Ship
from barrier import Barrier
from UFO import UFO
from start_screen import StartScreen
from high_score_window import HighScoreWindow

import game_functions as gf

def run_game():
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion!")

    # Make the play button and high scores button
    play_button = Button(ai_settings, screen, "Play!")
    high_scores_button = HighScoresButton(ai_settings, screen, "High Scores")

    # Create an instance to store game statistics and create a scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a ship, a group of bullets, and a group of aliens, a group of barriers, and a UFO
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    barrier = Barrier(ai_settings, screen)
    ufo = UFO(ai_settings, screen)
    hs_init = open("high_scores.txt", "r+")
    stats.high_score = int(hs_init.readline())
    stats.high_score_2 = int(hs_init.readline())
    stats.high_score_3 = int(hs_init.readline())
    hs_init.close()

    # Make the start screen
    start_screen = StartScreen(ai_settings, screen, aliens, "Alien Invasion!", "= 50", "= 100", "= 150", "= 300", "Gabriel Magallanes | For CPSC 386 (Video Game Design) | Cal State Fullerton | 2019")

    # Make the high score window
    high_score_window = HighScoreWindow(ai_settings, screen, stats)

    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Create a way to keep track of time (for the ufo spawn)
    time_elapsed = 0
    clock = pygame.time.Clock()

    # Start the main loop for the game
    while True:

        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, high_scores_button)

        if stats.game_active:
            ship.update()
            gf.update_ufo(ai_settings, screen, ufo)
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, high_score_window)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets, high_score_window)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, start_screen, play_button, ufo, barrier, high_scores_button)


run_game()