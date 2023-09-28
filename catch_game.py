# Import syntax
import pygame

# import sys
from settings import Settings
from character import Character
import game_functions as gf
from ball import Ball
from pygame.sprite import Group


def run_game():
    pygame.init()

    c_settings = Settings()

    screen = pygame.display.set_mode(
        (c_settings.screen_width, c_settings.screen_height)
    )
    pygame.display.set_caption("Catch")

    # Make a character
    character = Character(c_settings, screen)

    # Make a group stores the ball in.
    balls = Group()
    new_ball = Ball(c_settings, screen)
    balls.add(new_ball)

    while True:
        gf.check_events(c_settings, screen, character, new_ball)
        character.update()
        new_ball.update()

        # Check if the ball has go down to the screen.
        if new_ball.rect.y > c_settings.screen_height:
            new_ball.kill()
            new_ball = Ball(c_settings, screen)
            balls.add(new_ball)

        gf.update_screen(c_settings, screen, character, new_ball)


if __name__ == "__main__":
    run_game()
