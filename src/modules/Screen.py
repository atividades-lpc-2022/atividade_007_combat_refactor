import pygame
from modules.Dimension import Dimension


class Screen:
    def __init__(self, dimension: Dimension, background_color: pygame.Color):
        self.surface = pygame.display.set_mode((dimension.width, dimension.height))
        self.dimension = dimension
        self.background_color = background_color

    def draw(self):  # Draw screen
        self.surface.fill(self.background_color)
