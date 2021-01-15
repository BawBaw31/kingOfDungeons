import pygame
from CheckEvents import check_events
from Menu import Menu
from Thing.Monster import Monster


class GameManager:
    def __init__(self, window, player, room):
        self.window = window
        self.menu = Menu(self.window)
        self.player = player
        self.enemy = None
        self.room = room
        self.run = True
        self.state = "main"
        self.game_objects = []
        self.font_name = 'Fonts/8-BIT WONDER.TTF'
        self.inventory_click = False

    def state_manager(self):
        # Detecting monsters
        for monster in self.room.objects["M"]:
            if self.player.hit_box[0] == monster.hit_box[0] and self.player.hit_box[1] == monster.hit_box[1]:
                self.state = "battle"
                self.player.hit_box[0] -= 32

        # Detecting item
        if self.player.inventory_len() < self.player.max_length:
            for item in self.room.objects["I"]:
                if self.player.hit_box[0] == item.hit_box[0] and self.player.hit_box[1] == item.hit_box[1]:
                    self.state = "item"

        # Detecting door
        for door in self.room.objects["D"]:
            if self.player.hit_box[0] == door.hit_box[0] and self.player.hit_box[1] == door.hit_box[1]:
                if not self.room.objects["M"]:
                    self.state = "door"

        # Choosing the right loop
        if self.state == "main":
            self.main()
        elif self.state == "game":
            self.game()
        elif self.state == "inventory":
            self.inventory()
        elif self.state == "battle":
            self.battle()
        elif self.state == "item":
            self.pick_item()
        elif self.state == "door":
            self.passing_door()

        # Updating display
        pygame.display.update()

    def game(self):
        # Render
        self.window.fill((0, 0, 0))
        self.room.loading_map()
        check_events(self)
        self.player.render()

        # Checking statics
        if self.menu.state == "static":
            self.menu_loop()

    def main(self):
        self.window.fill((0, 0, 0))
        self.menu_loop()

    def battle(self):
        # Creating Monster
        if self.enemy is None or self.enemy.health <= 0:
            self.enemy = Monster(self.window)
            # Checking if it's Boss
            if self.room.actual_stage >= 5:
                self.enemy.set_to_boss()

        self.menu_loop()

    def inventory(self):
        self.menu_loop()

    def pick_item(self):
        for item in self.room.objects["I"]:
            if self.player.hit_box[0] == item.hit_box[0] and \
                    self.player.hit_box[1] == item.hit_box[1]:
                self.player.inventory.append(item)
                for key, line in enumerate(self.room.actual_map.tile):
                    for key1, letter in enumerate(line):
                        if key == item.hit_box[1] / 32:
                            if key1 == item.hit_box[0] / 32:
                                new_list = list(line)
                                new_list[key1] = " "
                                self.room.actual_map.tile[key] = "".join(new_list)
        self.room.objects["I"] = []
        self.menu.previous_state = self.menu.state
        self.menu.state = "game"
        self.state = "game"

    def passing_door(self):
        self.room.actual_stage += 1

        # Boss map
        if self.room.actual_stage == 5:
            self.room.actual_map.boss_map()
            self.player.reset_position()
            self.menu.previous_state = self.menu.state
            self.menu.state = "game"
            self.state = "game"

        # End of the game
        elif self.room.actual_stage > 5:
            self.room.actual_stage = 0
            self.room.actual_map.reset_map()
            self.player.reset_position()
            self.player.reset_stats()
            self.menu.previous_state = self.menu.state
            self.menu.state = "static"
            self.menu.static = "end"
            self.state = "main"

        # Normal door passed
        else:
            self.room.actual_map.reset_map()
            self.player.reset_position()
            self.menu.previous_state = self.menu.state
            self.menu.state = "game"
            self.state = "game"

    def menu_loop(self):
        actual_menu_state = self.menu.state

        while self.menu.state == actual_menu_state and self.run:
            check_events(self)
            self.menu.menu_manager(self.player, self.enemy)

            # Updating display
            pygame.display.update()
