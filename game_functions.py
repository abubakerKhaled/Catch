import sys
import pygame


def check_keydown_event(event, character):
    if event.key == pygame.K_RIGHT:
        character.moveing_right = True

    elif event.key == pygame.K_LEFT:
        character.moveing_left = True


def check_keyup_event(event, character):
    if event.key == pygame.K_RIGHT:
        character.moveing_right = False

    elif event.key == pygame.K_LEFT:
        character.moveing_left = False


def check_events(character):
    """Responds to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # If the key down
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, character)

        # If the key up
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, character)


def update_screen(c_settings, screen, character, ball):
    """Update images on the screen and flip to the new screen."""
    screen.fill(c_settings.bg_color)
    character.blitme()
    ball.blitme()
    pygame.display.flip()
