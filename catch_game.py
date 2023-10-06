import pygame
from settings import Settings
from character import Character
import game_functions as gf
from ball import Ball
from pygame.sprite import Group
from game_stats import GameStats
from time import sleep


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

    stats = GameStats(c_settings)

    while True:
        gf.check_events(c_settings, screen, character)

        if stats.game_active:
            character.update()
            new_ball.update()
            # Check if the character collides with any ball in the group.
            # If so, get rid of the ball and regenerate it again.
            # Otherwise, check if the ball has go down to the screen.
            # If so, decrement tries left and reset the game.
            if pygame.sprite.spritecollideany(character, balls):
                new_ball.kill()
                new_ball = Ball(c_settings, screen)
                balls.add(new_ball)
            if new_ball.rect.y > c_settings.screen_height:
                # Decrement tryes left.
                if stats.left_tryes > 0:
                    stats.left_tryes -= 1

                    new_ball.kill()
                    new_ball = Ball(c_settings, screen)
                    balls.add(new_ball)

                    character.character_center()

                    character.update()
                    new_ball.update()

                    sleep(0.5)

                else:
                    stats.game_active = False

        gf.update_screen(c_settings, screen, character, new_ball)


if __name__ == "__main__":
    run_game()
