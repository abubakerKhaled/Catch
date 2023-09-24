import sys
import pygame


def check_events(character):
    """Responds to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # If the key down
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                character.moving_right = True
            if event.key == pygame.K_LEFT:
                character.moving_left = True

        # If the key up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                character.moving_right = False

            if event.key == pygame.K_LEFT:
                character.moving_left = False


def update_screen(c_settings, screen, character):
    """Update images on the screen and flip to the new screen."""
    screen.fill(c_settings.bg_color)
    character.blitme()
    pygame.display.flip()
