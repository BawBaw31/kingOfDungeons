import pygame
from Thing.Thing import Thing


class Monster(Thing):
    def __init__(self, window):
        super().__init__(32, 32)
        self.window = window
        self.color = (255, 0, 0)
        self.tile = pygame.image.load("Tiles/monster1.png")

        # Stats
        self.max_health = 50
        self.health = self.max_health
        self.max_mana = 50
        self.mana = self.max_mana
        self.mana_cost = 15
        self.speed = 10
        self.atk_dmg = 10
        self.magic_dmg = 15
        self.lvl = 1
        self.xp = 0
        self.description = []
        self.boss = False

    def render(self):
        self.window.blit(self.tile, self.hit_box)

    def setting_xp(self):
        self.description = ["You win"]
        self.description.append(str("You win " + str(self.xp) + " XP"))
        # Append loot
        self.description.append("Click ENTER to continue")

    def battle_stats(self):
        sentence = (("PV ", str(self.health), "Mana ", str(self.mana)),
                    ("Atk Dmg ", str(self.atk_dmg), "Magic Dmg ", str(self.magic_dmg)),
                    ("Speed ", str(self.speed) + " ", "Lvl ", str(self.lvl)))
        return sentence

    def attack(self, player):
        player.health -= self.atk_dmg - self.atk_dmg * player.armor / 100
        print(player.armor)
        print("b")

    def cast_spell(self, player):
        self.mana -= self.mana_cost
        player.health -= self.magic_dmg
        print(player.armor)
        print("m")

    def set_to_boss(self):
        # Boss stats
        self.tile = pygame.image.load("Tiles/boss1.png")
        self.max_health *= 250/100
        self.health = self.max_health
        self.max_mana *= 200/100
        self.mana = self.max_mana
        self.mana_cost *= 110/100
        self.speed *= 110/100
        self.atk_dmg *= 110/100
        self.magic_dmg *= 110/100
        self.lvl += 1
        self.xp *= 600/100
        self.boss = True
