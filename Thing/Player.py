import random
import pygame
from Thing.Thing import Thing
from Thing.Stuff.Helmet import Helmet
from Thing.Stuff.Shirt import Shirt
from Thing.Stuff.Weapon import Weapon
from Thing.Stuff.Pant import Pant


class Player(Thing):
    def __init__(self, window):
        super().__init__(64, 64)
        self.window = window
        self.color = (0, 0, 255)
        self.tile = pygame.image.load("Tiles/player1.png")

        # Inventory
        self.inventory = [Helmet(window), Weapon(window), Pant(window), Shirt(window)]
        self.max_length = 51

        # Stuff
        self.stuff = {
            "H": [],
            "B": [],
            "L": [],
            "RH": [],
            "LH": []
        }

        # Bank
        self.money = 0

        # Stats
        self.max_health = 100
        self.health = self.max_health
        self.max_mana = 100
        self.mana = self.max_mana
        self.mana_cost = 20
        self.speed = 15
        self.atk_dmg = 20
        self.magic_dmg = 25
        self.armor = 0
        self.magic_res = 0
        self.lvl = 1
        self.xp = 0
        self.max_xp = 100
        self.monster_killed = 5
        self.dungeons = 1

    def render(self):
        self.window.blit(self.tile, self.hit_box)
        for stuff in self.stuff["H"]:
            self.window.blit(stuff.custom_tile, self.hit_box)
        for stuff in self.stuff["B"]:
            self.window.blit(stuff.custom_tile, self.hit_box)
        for stuff in self.stuff["L"]:
            self.window.blit(stuff.custom_tile, self.hit_box)
        for stuff in self.stuff["RH"]:
            self.window.blit(stuff.custom_tile, self.hit_box)
        for stuff in self.stuff["LH"]:
            self.window.blit(stuff.custom_tile, self.hit_box)

    # Battle functions
    def battle_stats(self):
        sentence = (("PV ", str(round(self.health)), "Mana ", str(round(self.mana))),
                    ("Atk Dmg ", str(round(self.atk_dmg)), "Magic Dmg ", str(round(self.magic_dmg))),
                    ("Speed ", str(round(self.speed)) + " ", "Lvl ", str(round(self.lvl))))
        return sentence

    def attack(self, enemy):
        if self.speed >= enemy.speed:
            enemy.health -= self.atk_dmg
            if enemy.health >= 0:
                self.take_dmg(enemy)
        elif self.speed < enemy.speed:
            self.take_dmg(enemy)
            if self.health >= 0:
                enemy.health -= self.atk_dmg

    def cast_spell(self, enemy):
        if self.mana >= self.mana_cost:
            if self.speed >= enemy.speed:
                self.mana -= self.mana_cost
                enemy.health -= self.magic_dmg
                if enemy.health >= 0:
                    self.take_dmg(enemy)

            elif self.speed < enemy.speed:
                self.take_dmg(enemy)
                if self.health >= 0:
                    self.mana -= self.mana_cost
                    enemy.health -= self.magic_dmg

    def take_dmg(self, enemy):
        atk_type = random.choice(["b", "m"])
        if enemy.mana <= 0:
            atk_type = "b"
        if atk_type == "b":
            enemy.attack(self)
        elif atk_type == "m":
            enemy.cast_spell(self)

    def checking_death(self, enemy, room, menu, game):
        if self.health <= 0:
            # Resetting player stats
            self.reset_stats()
            self.reset_position()

            menu.previous_state = menu.state
            menu.state = "static"
            menu.static = "game over"
            game.state = "main"
            return

        elif enemy.health <= 0:
            # Loot
            # XP
            self.gain_xp(enemy)

            # Deleting monsters
            for monster in room.objects["M"]:
                if self.hit_box[0] + 32 == monster.hit_box[0] and \
                        self.hit_box[1] == monster.hit_box[1]:
                    for key, line in enumerate(room.actual_map.tile):
                        for key1, letter in enumerate(line):
                            if key == monster.hit_box[1] / 32:
                                if key1 == monster.hit_box[0] / 32:
                                    new_list = list(line)
                                    new_list[key1] = "K"
                                    room.actual_map.tile[key] = "".join(new_list)
            menu.previous_state = menu.state
            menu.state = "static"
            menu.static = "won"
            game.state = "game"
            return

    # General game stats functions
    # def main_stats(self):
    #     sentence = (("PV ", str(self.health), "Mana ", str(self.mana)),
    #                 ("Atk Dmg ", str(self.atk_dmg), "Magic Dmg ", str(self.magic_dmg)),
    #                 ("Speed ", str(self.speed) + " ", "Lvl ", str(self.lvl)),
    #                 ("Monsters killed ", str(self.monster_killed), "Dungeons completed ", str(self.dungeons)))
    #     return sentence

    def gain_xp(self, enemy):
        self.xp += enemy.xp
        if self.xp + enemy.xp > self.max_xp:
            self.xp -= self.max_xp
            self.lvl += 1
            self.gain_lvl()

    def gain_lvl(self):
        self.max_xp *= 2
        # More stats

    def reset_stats(self):
        self.health = self.max_health
        self.max_mana = self.max_mana
        self.inventory = []
        self.stuff = {
            "H": [],
            "B": [],
            "L": [],
            "RH": [],
            "LH": []
        }

    def reset_position(self):
        self.hit_box[0] = 64
        self.hit_box[1] = 64

    # Inventory and stuff functions
    def inventory_len(self):
        return len(self.inventory)

    def apply_item(self, selector):
        self.inventory[selector].apply_effect(self)
        del self.inventory[selector]

    def equip_stuff(self, selector):
        self.inventory[selector].put_stuff(self)
        if self.stuff[self.inventory[selector].place]:
            self.stuff[self.inventory[selector].place][0].take_stuff_off(self)
            self.inventory.append(self.stuff[self.inventory[selector].place][0])
            del self.stuff[self.inventory[selector].place][0]
            self.stuff[self.inventory[selector].place].append(self.inventory[selector])
            del self.inventory[selector]
        else:
            self.stuff[self.inventory[selector].place].append(self.inventory[selector])
            del self.inventory[selector]

    def takeoff_stuff(self, selector):
        if self.inventory_len() < self.max_length:
            self.stuff[selector][0].take_stuff_off(self)
            self.inventory.append(self.stuff[selector][0])
            del self.stuff[selector][0]
        else:
            return

    def del_item(self, selector):
        del self.inventory[selector]
