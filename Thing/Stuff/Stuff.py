import pygame
from Thing.Thing import Thing


class Stuff(Thing):
    def __init__(self, window):
        super().__init__(32, 32)
        self.window = window
        self.color = (255, 0, 255)
        self.kind = "stuff"

    def render(self):
        pygame.draw.rect(self.window, self.color, self.hit_box)
