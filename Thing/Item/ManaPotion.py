import random
import pygame
from Thing.Item.Item import Item


class ManaPotion(Item):
    def __init__(self, window):
        super().__init__(window)
        self.name = "Mana Potion"
        self.effect = random.randint(25, 50)
        self.description = []
        self.inventory_rect = [32, 328, 32, 32]
        self.inventory_color = (0, 0, 255)
        self.inventory_tile = pygame.image.load("Tiles/mana_potion.png")

    def setting_description(self):
        self.description = []
        self.description.append(self.name)
        self.description.append(str("Gives " + str(self.effect) + " Mana Points back"))
        self.description.append("Click ENTER to use")
        self.description.append("Click DELETE to delete")
        self.description.append("Click ESC to return")

    def condition(self, player):
        # Nice to change
        if player.mana >= player.max_mana:
            return False
        else:
            return True

    def apply_effect(self, player):
        player.mana += self.effect
        if player.mana > player.max_mana:
            player.mana = player.max_mana
