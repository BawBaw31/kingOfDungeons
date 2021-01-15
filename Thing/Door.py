import pygame
from Thing.Thing import Thing


class Door(Thing):
    def __init__(self, window):
        super().__init__(32, 32)
        self.window = window
        self.color = (0, 255, 0)
        self.tile = pygame.image.load("Tiles/door1.png")

    def render(self):
        self.window.blit(self.tile, self.hit_box)
