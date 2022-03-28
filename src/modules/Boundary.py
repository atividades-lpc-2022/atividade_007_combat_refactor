import pygame
from config import *


class Boundary:
    def __init__(self, color: tuple):
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (0, 55, Config.SCREEN_WIDTH, 20))
        pygame.draw.rect(screen, self.color, (0, 55, 20, (Config.SCREEN_HEIGHT - 55)))
        pygame.draw.rect(
            screen,
            self.color,
            ((Config.SCREEN_WIDTH - 20), 55, 20, (Config.SCREEN_HEIGHT - 55)),
        )
        pygame.draw.rect(
            screen,
            self.color,
            (20, (Config.SCREEN_HEIGHT - 20), (Config.SCREEN_WIDTH - 40), 20),
        )
