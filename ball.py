import pygame
from pygame.sprite import Sprite
import random


class Ball(Sprite):
    """A class to manage the balls."""

    def __init__(self, c_settings, screen):
        """Initialize the ball and it's starting position."""

        super(Ball, self).__init__()

        self.c_settings = c_settings
        self.screen = screen
        self.speed_factor = self.c_settings.ball_speed_factor
        self.color = c_settings.ball_color

        # Load the ball image and get its rect
        self.rect = pygame.Rect(0, 0, c_settings.ball_width, c_settings.ball_height)
        self.screen_rect = self.screen.get_rect()

        # Start each ball at the top of the screen with random position.
        self.top_position = random.randint(1, self.c_settings.screen_width)
        self.rect.top = self.screen_rect.top
        self.rect.centerx = self.top_position

        # Store the ball's position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        """Move the ball down the screen."""
        # Update the decimal position of the bullet.
        self.y += self.speed_factor
        # Update the rect position
        self.rect.y = self.y

    def blitme(self):
        """Draw the ball at the top of the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
