import pygame
import random
from Thing.Thing import Thing


class Wall(Thing):
    def __init__(self, window):
        super().__init__(32, 32)
        self.window = window
        self.color = (135, 163, 150)
        self.tile = pygame.image.load("Tiles/wall1.png")

    def render(self):
        self.window.blit(self.tile, self.hit_box)
