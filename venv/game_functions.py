import sys
from time import sleep
import sched

import pygame
from pygame.locals import *
from pygame import mixer

from bullet import Bullet
from alien import Alien, Alien_2, Alien_3
from UFO import UFO
from barrier import Barrier
from high_score_window import HighScoreWindow
import math

def update_high_scores(stats):
    if stats.score > stats.high_score and stats.score > stats.high_score_2:
        prev_first = stats.high_score
        prev_second = stats.high_score_2

        stats.high_score_2 = prev_first
        stats.high_score_3 = prev_second
        stats.high_score = stats.score

    elif stats.high_score_2 < stats.score < stats.high_score:
        temp = stats.high_score_2
        stats.high_score_2 = stats.score
        stats.high_score_3 = temp

    elif stats.high_score_3 < stats.score < stats.high_score_2:
        stats.high_score_3 = stats.score

    hs = open("high_scores.txt", "w")
    hs.write(str(stats.high_score) + '\n' + str(stats.high_score_2) + '\n' + str(stats.high_score_3))
    hs.close()

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    #respond to keyPRESSES
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):
    # create a new bullet and add it to the bullets group. also check for how many bullets the player should have
    for i in range(1):
        new_bullet = Bullet(ai_settings=ai_settings, screen=screen, ship=ship, yoffset=i* 0.5 * ship.rect.height)
        bullets.add(new_bullet)
        bullet_sound = pygame.mixer.Channel(0)
        bullet_sound.play(pygame.mixer.Sound('C:/Users/Gabriel/PycharmProjects/AlienGame/shoot.wav'), maxtime=600)
        bullet_sound.set_volume(0.2)
        bullets.update

def check_keyup_events(event, ship):
    #respond to key RELEASES
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens,
                 bullets, high_scores_button):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y, = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button,
                              ship, aliens, bullets, mouse_x, mouse_y)
            check_high_scores_button(ai_settings, screen, stats, mouse_x, mouse_y, high_scores_button)


def check_play_button(ai_settings, screen, stats, sb, play_button,
                      ship, aliens, bullets, mouse_x, mouse_y):
    """Start a new game when the player clicks Play!"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:

        stats.game_ends = False

        #Reset the game settings.
        ai_settings.initialize_dynamic_settings()

        #Hide the mouse cursor.
        pygame.mouse.set_visible(False)

        #Reset the game statistics.
        stats.reset_stats()
        stats.game_active = True

        #Reset the scoreboard images.
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        #Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()

        #Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

def check_high_scores_button(ai_settings, screen, stats, mouse_x, mouse_y, high_scores_button):
    """Show the high scores page when the player clicks the high scores button"""
    hs_button_clicked = high_scores_button.rect.collidepoint(mouse_x, mouse_y)
    if hs_button_clicked:
       stats.high_scores_button_clicked = True

def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, start_screen, play_button, ufo, barrier, high_scores_button):
    screen.fill(ai_settings.bg_color)
    """Update images on the screen and flip to the new screen."""

    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)
    barrier.blitme()
    ufo.blitme()

    # Draw the score information
    sb.show_score()

    if ai_settings.aliens_destroyed == 0:
        ai_settings.aliens_destroyed = ai_settings.aliens_destroyed + 1
        pygame.mixer.music.load('C:/Users/Gabriel/PycharmProjects/AlienGame/soundtrack.mp3')
        pygame.mixer.music.play(-1)
    elif ai_settings.aliens_destroyed == 15:
        speed_up = pygame.mixer.music
        speed_up.load('C:/Users/Gabriel/PycharmProjects/AlienGame/soundtrack_2.mp3')
        speed_up.play(-1)

    if not stats.game_active:
        start_screen.draw_start_screen()
        start_screen.draw_title_aliens()

        play_button.draw_button()
        high_scores_button.draw_hs_button()

    if stats.game_ends:
        end_screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
        screen_rect = end_screen.get_rect()
        play_button.draw_button()
        high_scores_button.draw_hs_button()
        pygame.display.update(screen_rect)

    # Draw the play button, high scores button and start screen if the game is inactive

    if stats.high_scores_button_clicked:
        # hs_screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
        # screen_rect = screen.get_rect()
        # pygame.display.update(screen_rect)
        high_score_window = HighScoreWindow(ai_settings, screen, stats)
        high_score_window.draw_high_score_window(stats)

    # Make the most recently drawn screen visible
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, high_score_window):
    """Update position of bullets and get rid of old bullets"""
    #update bullet positions
    bullets.update()

    # Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets, high_score_window)

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets, high_score_window):
    """Respond to bullet-alien collisions"""
    #Remove any bullets and aliens that have collided
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            for x in aliens:
                print(x.score)
                print("stats" , int(math.ceil((stats.score/3) / 10.0)) * x.score)
                ai_settings.aliens_destroyed += 1
                stats.score += x.score
                sb.prep_score()


        check_high_score(stats, sb, ai_settings, high_score_window)
        update_high_scores(stats)

    if len(aliens) == 0:
        #If the entire fleet is destroyed, start a new level
        bullets.empty()
        ai_settings.increase_speed()

        #Increase level.
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)

def get_number_aliens_x(ai_settings, alien_width):
    #determine the number of aliens that fit in a row
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    #determine the number of rows of aliens that fit on the screen
    available_space_y = (ai_settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    #create an alien and place it in the row
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 1 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 1 * alien.rect.height * row_number
    aliens.add(alien)

def create_alien_2(ai_settings, screen, aliens, alien_number, row_number):
    #create an alien and place it in the row
    alien = Alien_2(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 1 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 1 * alien.rect.height * row_number
    aliens.add(alien)

def create_alien_3(ai_settings, screen, aliens, alien_number, row_number):
    #create an alien and place it in the row
    alien = Alien_3(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 1 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 1 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    #create a full fleet of aliens.
    #create an alien and find the number of aliens in a row
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
                                  alien.rect.height)

    #create the fleet of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number,
                         1)
            create_alien_2(ai_settings, screen, aliens, alien_number,
                         2)
            create_alien_3(ai_settings, screen, aliens, alien_number,
                         3)

def check_fleet_edges(ai_settings, aliens):
    #respond appropriately if any aliens have reached an edge
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    #drop the entire fleet and change the fleet's direction
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets, high_score_window):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #Treat this the same as if the ship got hit.
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, high_score_window)
            break

def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets, high_score_window):
    """
    Check if the fleet is at an edge,
        and then update the positions of all aliens in the fleet.
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    #Look for alien-ship collisions.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, high_score_window)

    #Look for aliens hitting the bottom of the screen
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets, high_score_window)


def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, high_score_window):
    """Respond to ship being hit by alien."""
    if stats.ships_left > 0:
        #Decrement ships_left.
        stats.ships_left -= 1

        #Update scoreboard
        sb.prep_ships()

        #Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()

        #Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        #Pause
        sleep(0.5)

    else:
        pygame.mouse.set_visible(True)
        check_high_score(stats, sb, ai_settings, high_score_window)
        stats.game_active = False
        first_playthrough = True
        stats.game_ends = True

def check_high_score(stats, sb, ai_settings, high_score_window):
    """Check to see if there's a new high score"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score
        high_score_window.draw_high_score_window()

def update_ufo(ai_settings, screen, ufo):
    """Update the position of the ufo"""
    #update ufo position
    check_ufo_edges(ai_settings, ufo)
    ufo.update()

def check_ufo_edges(ai_settings, ufo):
    if ufo.check_edges():
        change_ufo_direction(ai_settings, ufo)

def change_ufo_direction(ai_settings, ufo):
    now = pygame.time.get_ticks()
    if now - ai_settings.last >= ai_settings.cooldown:
        ai_settings.last = now
        ai_settings.ufo_direction *= -1
