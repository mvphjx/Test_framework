import pygame
from pygame.sprite import Group

from learn_and_try.python_book_src.chapter_12.settings import Settings
from learn_and_try.python_book_src.chapter_12.ship import Ship
import learn_and_try.python_book_src.chapter_12.game_functions as gf

def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Set the background color.
    bg_color = (230, 230, 230)
    
    # Make a ship.
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in.
    bullets = Group()

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
