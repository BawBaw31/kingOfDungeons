import pygame
from Thing.Thing import Thing


class Button(Thing):
    def __init__(self, window):
        super().__init__(32, 32)
        self.window = window
        self.color = (255, 255, 0)
        self.tile = pygame.image.load("Tiles/inventory1.png")

    def render(self):
        self.window.blit(self.tile, self.hit_box)
