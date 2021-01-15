import random
import pygame
from Thing.Stuff.Stuff import Stuff


class Weapon(Stuff):
    def __init__(self, window):
        super().__init__(window)
        self.name = "Weapon"
        self.place = "RH"
        self.effect = random.randint(5, 10)
        self.stat = "Attack"
        self.description = []
        self.inventory_rect = [32, 328, 32, 32]
        self.inventory_color = (255, 0, 255)
        self.inventory_tile = pygame.image.load("Tiles/weapon1.png")
        self.custom_tile = pygame.image.load("Tiles/custom_weapon.png")

    def setting_description(self):
        self.description = []
        self.description.append(self.name)
        self.description.append(str("Gives " + str(self.effect) + str(self.stat)))
        self.description.append("Click ENTER to dress")
        self.description.append("Click DELETE to delete")
        self.description.append("Click ESC to return")

    def setting_stuff_description(self):
        self.description = []
        self.description.append(self.name)
        self.description.append(str("Gives " + str(self.effect) + str(self.stat)))
        self.description.append("Click ENTER to undress")
        self.description.append("Click DELETE to delete")
        self.description.append("Click ESC to return")

    def put_stuff(self, player):
        player.atk_dmg += self.effect

    def take_stuff_off(self, player):
        player.atk_dmg -= self.effect
