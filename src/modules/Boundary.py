import pygame
from modules.Screen import Screen


class Boundary:
    def __init__(self, color: tuple):
        self.color = color

    def draw(self, screen: Screen):
        pygame.draw.rect(
            screen.surface, self.color, (0, 55, screen.dimension.width, 20)
        )
        pygame.draw.rect(
            screen.surface, self.color, (0, 55, 20, (screen.dimension.height - 55))
        )
        pygame.draw.rect(
            screen.surface,
            self.color,
            ((screen.dimension.width - 20), 55, 20, (screen.dimension.height - 55)),
        )
        pygame.draw.rect(
            screen.surface,
            self.color,
            (20, (screen.dimension.height - 20), (screen.dimension.width - 40), 20),
        )
