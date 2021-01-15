import pygame
from Thing.Thing import Thing


class Item(Thing):
    def __init__(self, window):
        super().__init__(32, 32)
        self.window = window
        self.color = (255, 255, 255)
        self.tile = pygame.image.load("Tiles/item1.png")
        self.kind = "item"

    def render(self):
        self.window.blit(self.tile, self.hit_box)
