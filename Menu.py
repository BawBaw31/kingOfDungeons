import pygame


class Menu:
    def __init__(self, window):
        self.window = window
        self.display = pygame.Surface((608, 448))
        self.display_color = (103, 86, 91)
        self.font_name = 'Fonts/8-BIT WONDER.TTF'
        self.previous_state = "main"
        self.state = "main"
        self.static = "rules"
        self.cursor = "battle"
        self.item_selector = 0
        self.stuff_selector = "L"

    def menu_manager(self, player, enemy):
        if self.state == "main":
            self.main_menu()
        elif self.state == "static":
            self.static_menu(enemy)
        elif self.state == "game":
            return
        elif self.state == "battle":
            self.battle_menu()
        elif self.state == "battling":
            self.battling_menu(player, enemy)
        elif self.state == "inventory":
            self.inventory_menu(player)

    def main_menu(self):
        # Setting var
        choices = ("Load", "New Game", "Rules")

        # Background
        self.display.fill(self.display_color)

        # Title
        self.title("Main Menu")

        # Rect
        rect = (32, 64, 544, 350)
        pygame.draw.rect(self.display, (255, 255, 255), rect, 2)
        font = pygame.font.Font(self.font_name, 16)
        for key, text in enumerate(choices):
            text_surface = font.render(text, True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.midtop = (304, 130 + 100 * key)
            self.display.blit(text_surface, text_rect)

        # Cursor
        if self.cursor == "load":
            cursor_rect = (200, 130, 16, 16)
            pygame.draw.rect(self.display, (0, 0, 255), cursor_rect)
        elif self.cursor == "new":
            cursor_rect = (200, 230, 16, 16)
            pygame.draw.rect(self.display, (0, 0, 255), cursor_rect)
        elif self.cursor == "rules":
            cursor_rect = (200, 330, 16, 16)
            pygame.draw.rect(self.display, (0, 0, 255), cursor_rect)
        else:
            self.cursor = "load"

        # Blit
        self.window.blit(self.display, (16, 16))

    def inventory_menu(self, player):
        # Setting var
        spot_array = []
        item_spot_x = 32
        item_spot_y = 328

        # Background
        self.display.fill(self.display_color)

        # Title
        self.title("Inventory")

        # Player rect
        player_rect = (32, 64, 544, 100)
        pygame.draw.rect(self.display, (0, 0, 255), player_rect, 2)
        player_font = pygame.font.Font(self.font_name, 12)
        player_stats = player.battle_stats()
        for key, line in enumerate(player_stats):
            for key1, text in enumerate(line):
                player_stats_surface = player_font.render(text, True, (255, 255, 255))
                player_stats_rect = player_stats_surface.get_rect()
                player_stats_rect.midleft = (64 + 150 * key1, 80 + 32 * key)
                self.display.blit(player_stats_surface, player_stats_rect)

        # Text rect
        description_rect = (32, 196, 350, 100)
        pygame.draw.rect(self.display, (0, 255, 0), description_rect, 2)
        description_font = pygame.font.Font(self.font_name, 12)
        if self.item_selector >= 0:
            if player.inventory:
                player.inventory[self.item_selector].setting_description()
                for key, text in enumerate(player.inventory[self.item_selector].description):
                    description_text_surface = description_font.render(text, True, (255, 255, 255))
                    description_text_rect = description_text_surface.get_rect()
                    description_text_rect.midleft = (64, 212 + 16 * key)
                    self.display.blit(description_text_surface, description_text_rect)
        elif player.stuff[self.stuff_selector]:
            player.stuff[self.stuff_selector][0].setting_stuff_description()
            for key, text in enumerate(player.stuff[self.stuff_selector][0].description):
                description_text_surface = description_font.render(text, True, (255, 255, 255))
                description_text_rect = description_text_surface.get_rect()
                description_text_rect.midleft = (64, 212 + 16 * key)
                self.display.blit(description_text_surface, description_text_rect)
        else:
            fill_rect = (34, 198, 347, 97)
            pygame.draw.rect(self.display, self.display_color, fill_rect)

        # Stuff rect
        h_rect = (479, 186, 32, 32)
        pygame.draw.rect(self.display, (0, 255, 0), h_rect, 2)
        b_rect = (479, 228, 32, 32)
        pygame.draw.rect(self.display, (0, 255, 0), b_rect, 2)
        l_rect = (479, 270, 32, 32)
        pygame.draw.rect(self.display, (0, 255, 0), l_rect, 2)
        rh_rect = (437, 218, 32, 32)
        pygame.draw.rect(self.display, (0, 255, 0), rh_rect, 2)
        lh_rect = (521, 218, 32, 32)
        pygame.draw.rect(self.display, (0, 255, 0), lh_rect, 2)

        # Stuff
        for stuff in player.stuff["H"]:
            stuff.inventory_rect = [479, 186, 33, 33]
            pygame.draw.rect(self.display, stuff.inventory_color, stuff.inventory_rect)
            self.display.blit(stuff.inventory_tile, stuff.inventory_rect)
        for stuff in player.stuff["B"]:
            stuff.inventory_rect = [479, 228, 33, 33]
            pygame.draw.rect(self.display, stuff.inventory_color, stuff.inventory_rect)
            self.display.blit(stuff.inventory_tile, stuff.inventory_rect)
        for stuff in player.stuff["RH"]:
            stuff.inventory_rect = [437, 218, 33, 33]
            pygame.draw.rect(self.display, stuff.inventory_color, stuff.inventory_rect)
            self.display.blit(stuff.inventory_tile, stuff.inventory_rect)
        for stuff in player.stuff["LH"]:
            stuff.inventory_rect = [521, 218, 33, 33]
            pygame.draw.rect(self.display, stuff.inventory_color, stuff.inventory_rect)
            self.display.blit(stuff.inventory_tile, stuff.inventory_rect)
        for stuff in player.stuff["L"]:
            stuff.inventory_rect = [479, 270, 33, 33]
            pygame.draw.rect(self.display, stuff.inventory_color, stuff.inventory_rect)
            self.display.blit(stuff.inventory_tile, stuff.inventory_rect)

        # Items grid
        while item_spot_y < 396:
            while item_spot_x < 576:
                spot_rect = (item_spot_x, item_spot_y, 32, 32)
                spot_array.append(spot_rect)
                item_spot_x += 32
            item_spot_x = 32
            item_spot_y += 32
        for spot in spot_array:
            pygame.draw.rect(self.display, (255, 255, 255), spot, 4)

        # Items
        for key, item in enumerate(player.inventory):
            item.inventory_rect = [32, 328, 30, 30]
            if 0 <= key <= 16:
                item.inventory_rect[0] += 32 * key
            elif 16 < key <= 33:
                item.inventory_rect[1] += 32
                item.inventory_rect[0] += 32 * (key - 17)
            elif 33 < key <= 50:
                item.inventory_rect[1] += 64
                item.inventory_rect[0] += 32 * (key - 34)
            pygame.draw.rect(self.display, item.inventory_color, item.inventory_rect)
            self.display.blit(item.inventory_tile, item.inventory_rect)


        # Cursor
        if player.inventory and self.item_selector >= 0:
            cursor_rect = player.inventory[self.item_selector].inventory_rect
            pygame.draw.rect(self.display, (0, 0, 0), cursor_rect, 2)

        # Stuff Cursor
        if self.item_selector == -1:
            cursor_rect = [479, 270, 33, 33]
            if self.stuff_selector == "L":
                cursor_rect = [479, 270, 33, 33]
            elif self.stuff_selector == "B":
                cursor_rect = [479, 228, 33, 33]
            elif self.stuff_selector == "LH":
                cursor_rect = [521, 218, 33, 33]
            elif self.stuff_selector == "RH":
                cursor_rect = [437, 218, 33, 33]
            elif self.stuff_selector == "H":
                cursor_rect = [479, 186, 33, 33]

            pygame.draw.rect(self.display, (0, 0, 0), cursor_rect, 3)

        # Blit
        self.window.blit(self.display, (16, 16))

    def battle_menu(self):
        # Setting var
        choices = ("Battle", "Run")

        # Background
        self.display.fill(self.display_color)

        # Title
        self.title("Fight")

        # Rect
        rect = (32, 64, 544, 350)
        pygame.draw.rect(self.display, (255, 255, 255), rect, 2)
        font = pygame.font.Font(self.font_name, 16)
        for key, text in enumerate(choices):
            text_surface = font.render(text, True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.midtop = (304, 200 + 100 * key)
            self.display.blit(text_surface, text_rect)

        # Cursor
        if self.cursor == "battle":
            cursor_rect = (200, 200, 16, 16)
            pygame.draw.rect(self.display, (0, 0, 255), cursor_rect)
        elif self.cursor == "run":
            cursor_rect = (200, 300, 16, 16)
            pygame.draw.rect(self.display, (0, 0, 255), cursor_rect)
        else:
            self.cursor = "battle"

        # Blit
        self.window.blit(self.display, (16, 16))

    def battling_menu(self, player, enemy):
        # Setting var
        choices = ("Attack", "Cast spell", "Inventory")

        # Background
        self.display.fill(self.display_color)

        # Title
        self.title("Fight")

        # Enemy rect
        enemy_rect = (32, 64, 544, 100)
        pygame.draw.rect(self.display, (255, 0, 0), enemy_rect, 2)
        enemy_font = pygame.font.Font(self.font_name, 12)
        enemy_stats = enemy.battle_stats()
        for key, line in enumerate(enemy_stats):
            for key1, text in enumerate(line):
                enemy_stats_surface = enemy_font.render(text, True, (255, 255, 255))
                enemy_stats_rect = enemy_stats_surface.get_rect()
                enemy_stats_rect.midleft = (64 + 150 * key1, 80 + 32 * key)
                self.display.blit(enemy_stats_surface, enemy_stats_rect)
        self.display.blit(enemy.tile, (288, 82))

        # Player rect
        player_rect = (32, 196, 544, 100)
        pygame.draw.rect(self.display, (0, 0, 255), player_rect, 2)
        player_font = pygame.font.Font(self.font_name, 12)
        player_stats = player.battle_stats()
        for key, line in enumerate(player_stats):
            for key1, text in enumerate(line):
                player_stats_surface = player_font.render(text, True, (255, 255, 255))
                player_stats_rect = player_stats_surface.get_rect()
                player_stats_rect.midleft = (64 + 150 * key1, 212 + 32 * key)
                self.display.blit(player_stats_surface, player_stats_rect)
        self.display.blit(player.tile, (288, 232))
        for stuff in player.stuff["H"]:
            self.display.blit(stuff.custom_tile, (288, 232))
        for stuff in player.stuff["B"]:
            self.display.blit(stuff.custom_tile, (288, 232))
        for stuff in player.stuff["L"]:
            self.display.blit(stuff.custom_tile, (288, 232))
        for stuff in player.stuff["RH"]:
            self.display.blit(stuff.custom_tile, (288, 232))
        for stuff in player.stuff["LH"]:
            self.display.blit(stuff.custom_tile, (288, 232))

        # Action rect
        action_rect = (32, 328, 544, 100)
        pygame.draw.rect(self.display, (255, 255, 255), action_rect, 4)
        action_font = pygame.font.Font(self.font_name, 16)
        for key, text in enumerate(choices):
            action_surface = action_font.render(text, True, (255, 255, 255))
            action_rect = action_surface.get_rect()
            action_rect.center = (128 + 182 * key, 350 + 64)
            self.display.blit(action_surface, action_rect)

        # Cursor
        if self.cursor == "attack":
            cursor_rect = (120, 374, 16, 16)
            pygame.draw.rect(self.display, (0, 0, 255), cursor_rect)
        elif self.cursor == "cast spell":
            cursor_rect = (302, 374, 16, 16)
            pygame.draw.rect(self.display, (0, 0, 255), cursor_rect)
        elif self.cursor == "inventory":
            cursor_rect = (484, 374, 16, 16)
            pygame.draw.rect(self.display, (0, 0, 255), cursor_rect)
        else:
            self.cursor = "attack"

        # Blit
        self.window.blit(self.display, (16, 16))

    def static_menu(self, enemy):
        self.window.fill((0, 0, 0))

        # Background
        self.display.fill(self.display_color)

        if self.static == "rules":
            # Setting var
            rules_array = ["The rules are simple",
                           "Kill them all",
                           "And complete the max of dungeons you can",
                           "Be careful",
                           "You only have one life"]
            elements_array = ["Player", "Monster", "Item", "Door", "Wall"]

            # Title
            self.title("Rules")

            # Rect
            rect = (32, 64, 544, 350)
            pygame.draw.rect(self.display, (255, 255, 255), rect, 2)

            # Rules text
            for key, text in enumerate(rules_array):
                rules_font = pygame.font.Font(self.font_name, 12)
                rules_text_surface = rules_font.render(text, True, (255, 255, 255))
                rules_text_rect = rules_text_surface.get_rect()
                rules_text_rect.midleft = (64, 96 + 32 * key)
                self.display.blit(rules_text_surface, rules_text_rect)

            # Color code
            for key, text in enumerate(elements_array):
                elements_font = pygame.font.Font(self.font_name, 12)
                elements_text_surface = elements_font.render(text, True, (255, 255, 255))
                elements_text_rect = elements_text_surface.get_rect()
                elements_text_rect.midleft = (128, 256 + 32 * key)
                self.display.blit(elements_text_surface, elements_text_rect)

            # Color code
            player_rect = (64, 240, 32, 32)
            pygame.draw.rect(self.display, (0, 0, 255), player_rect)
            monster_rect = (64, 240 + 32, 32, 32)
            pygame.draw.rect(self.display, (255, 0, 0), monster_rect)
            item_rect = (64, 240 + 32 * 2, 32, 32)
            pygame.draw.rect(self.display, (255, 255, 255), item_rect)
            door_rect = (64, 240 + 32 * 3, 32, 32)
            pygame.draw.rect(self.display, (0, 255, 0), door_rect)
            wall_rect = (64, 240 + 32 * 4, 32, 32)
            pygame.draw.rect(self.display, (135, 163, 150), wall_rect)

        elif self.static == "game over":
            # Setting var
            game_over_array = ["You loose",
                           "I trusted you",
                           "Die in peace"]

            # Title
            self.title("Game Over")

            # Rect
            rect = (32, 64, 544, 350)
            pygame.draw.rect(self.display, (255, 255, 255), rect, 2)

            # Rules text
            for key, text in enumerate(game_over_array):
                rules_font = pygame.font.Font(self.font_name, 12)
                rules_text_surface = rules_font.render(text, True, (255, 255, 255))
                rules_text_rect = rules_text_surface.get_rect()
                rules_text_rect.midleft = (64, 96 + 32 * key)
                self.display.blit(rules_text_surface, rules_text_rect)

        elif self.static == "won":
            # Setting var

            # Title
            self.title("You win")

            # Rect
            rect = (32, 64, 544, 350)
            pygame.draw.rect(self.display, (255, 255, 255), rect, 2)

            # Rules text
            enemy.setting_xp()
            for key, text in enumerate(enemy.description):
                rules_font = pygame.font.Font(self.font_name, 12)
                rules_text_surface = rules_font.render(text, True, (255, 255, 255))
                rules_text_rect = rules_text_surface.get_rect()
                rules_text_rect.midleft = (64, 96 + 32 * key)
                self.display.blit(rules_text_surface, rules_text_rect)

        elif self.static == "end":
            # Setting var
            end_text_array = ["You finished the dungeon",
                              "You are so brave",
                              "Thank you for playing this shitty game",
                              "Hope you didn't loose too much time"
                              "Bye bye"]
            # Title
            self.title("End of Dungeon")

            # Rect
            rect = (32, 64, 544, 350)
            pygame.draw.rect(self.display, (255, 255, 255), rect, 2)

            # End text
            for key, text in enumerate(end_text_array):
                rules_font = pygame.font.Font(self.font_name, 12)
                rules_text_surface = rules_font.render(text, True, (255, 255, 255))
                rules_text_rect = rules_text_surface.get_rect()
                rules_text_rect.midleft = (64, 96 + 32 * key)
                self.display.blit(rules_text_surface, rules_text_rect)

        # Blit
        self.window.blit(self.display, (16, 16))

    def title(self, name):
        # Title
        font = pygame.font.Font(self.font_name, 22)
        text_surface = font.render(name, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (304, 32)
        self.display.blit(text_surface, text_rect)
