import pygame


class Character:
    def __init__(self, c_settings, screen):
        """Initialize the character and set its starting position."""

        self.screen = screen
        self.c_settings = c_settings

        # Load the character image and get its rect.
        self.image = pygame.image.load("images/character1.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new character at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Movement flags
        self.moveing_right = False
        self.moveing_left = False

    def update(self):
        """Update the character's movements based on the movement flags."""
        if self.moveing_right:
            self.rect.centerx += 1
        if self.moveing_left:
            self.rect.centerx -= 1

    def blitme(self):
        """Draw the character in its current position."""
        self.screen.blit(self.image, self.rect)
