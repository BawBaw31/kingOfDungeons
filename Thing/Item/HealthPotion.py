import random
import pygame
from Thing.Item.Item import Item


class HealthPotion(Item):
    def __init__(self, window):
        super().__init__(window)
        self.name = "Health Potion"
        self.effect = random.randint(25, 100)
        self.description = []
        self.inventory_rect = [32, 328, 32, 32]
        self.inventory_color = (0, 255, 0)
        self.inventory_tile = pygame.image.load("Tiles/health_potion.png")

    def setting_description(self):
        self.description = []
        self.description.append(self.name)
        self.description.append(str("Heals " + str(self.effect) + " Life Points"))
        self.description.append("Click ENTER to use")
        self.description.append("Click DELETE to delete")
        self.description.append("Click ESC to return")

    def condition(self, player):
        # Nice to change
        if player.health >= player.max_health:
            return False
        else:
            return True

    def apply_effect(self, player):
        player.health += self.effect
        if player.health > player.max_health:
            player.health = player.max_health
