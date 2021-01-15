import random
from Map import Map
from Thing.Wall import Wall
from Thing.Monster import Monster
from Thing.Item.HealthPotion import HealthPotion
from Thing.Item.ManaPotion import ManaPotion
from Thing.Door import Door
from Thing.Button import Button


class Room:
    def __init__(self, window):
        self.window = window
        self.objects = {
            "M": [],
            "G": [],
            "D": [],
            "I": [],
            "C": []
        }
        self.monster_count = random.randint(0, 3)
        self.item_count = random.randint(0, 2)
        self.actual_map = Map()
        self.actual_stage = 0

    def loading_map(self):
        self.objects = {
            "M": [],
            "G": [],
            "D": [],
            "I": [],
            "C": []
        }

        self.actual_map.random_map()

        # Rendering the map
        for key, line in enumerate(self.actual_map.tile):
            for key1, letter in enumerate(line):
                if letter == "G":
                    new_wall = Wall(self.window)
                    new_wall.hit_box[0] = new_wall.hit_box[0] * key1
                    new_wall.hit_box[1] = new_wall.hit_box[1] * key
                    self.objects[letter].append(new_wall)
                elif letter == "M":
                    new_monster = Monster(self.window)
                    if self.actual_stage == 5:
                        new_monster.set_to_boss()
                    new_monster.hit_box[0] = new_monster.hit_box[0] * key1
                    new_monster.hit_box[1] = new_monster.hit_box[1] * key
                    self.objects[letter].append(new_monster)
                elif letter == "I":
                    new_item = random.choice([HealthPotion(self.window), ManaPotion(self.window)])
                    new_item.hit_box[0] = new_item.hit_box[0] * key1
                    new_item.hit_box[1] = new_item.hit_box[1] * key
                    self.objects[letter].append(new_item)
                elif letter == "D":
                    new_door = Door(self.window)
                    new_door.hit_box[0] = new_door.hit_box[0] * key1
                    new_door.hit_box[1] = new_door.hit_box[1] * key
                    self.objects[letter].append(new_door)
                elif letter == "C":
                    new_button = Button(self.window)
                    new_button.hit_box[0] = new_button.hit_box[0] * key1
                    new_button.hit_box[1] = new_button.hit_box[1] * key
                    self.objects[letter].append(new_button)
        self.render()

    def render(self):
        for obj in self.objects.values():
            for obj1 in obj:
                obj1.render()
