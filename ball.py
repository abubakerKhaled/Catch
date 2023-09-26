import pygame


class Ball:
    def __init__(self, c_settings, screen):
        """Initialize the ball and it's starting position."""

        self.c_settings = c_settings
        self.screen = screen

        # Load the ball image and get its rect
        self.image = pygame.image.load("images/ball.png")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start each ball at the top of the screen with random position.
        self.rect.top = self.screen_rect.top
        self.rect.centerx = self.screen_rect.centerx

    def blitme(self):
        """Draw the ball at the top of the screen."""
        self.screen.blit(self.image, self.rect)
