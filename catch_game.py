# Import syntax
import pygame

# import sys
from settings import Settings
from character import Character
import game_functions as gf


def run_game():
    pygame.init()

    c_settings = Settings()

    screen = pygame.display.set_mode(
        (c_settings.screen_width, c_settings.screen_height)
    )
    pygame.display.set_caption("Catch")

    # Make a character
    character = Character(c_settings, screen)

    while True:
        gf.check_events(character)
        character.update()
        gf.update_screen(c_settings, screen, character)


if __name__ == "__main__":
    run_game()
