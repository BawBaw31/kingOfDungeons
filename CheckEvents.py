import pygame


def check_events(self):
    # Checking events
    for event in pygame.event.get():

        # Variables
        next_x = 0
        next_y = 0
        key_pressed = False

        # Quit click
        if event.type == pygame.QUIT:
            self.run = False
            break

        # Game Mouse Click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.menu.state != "static":
                # Click inventory
                for button in self.room.objects["C"]:
                    if pygame.Rect(button.hit_box).collidepoint(pygame.mouse.get_pos()):
                        if not self.inventory_click:
                            if self.state == "game":
                                self.menu.previous_state = self.menu.state
                                self.menu.state = "inventory"
                                self.state = "inventory"
                                self.inventory_click = True
                        else:
                            self.menu.previous_state = self.menu.state
                            self.menu.state = "game"
                            self.state = "game"
                            self.inventory_click = False

        if event.type == pygame.KEYDOWN:
            # Main Events
            if self.menu.state == "main":
                if not key_pressed:
                    # Up
                    if event.key == pygame.K_UP:
                        if self.menu.cursor == "load":
                            self.menu.cursor = "rules"
                        elif self.menu.cursor == "new":
                            self.menu.cursor = "load"
                        elif self.menu.cursor == "rules":
                            self.menu.cursor = "new"
                    # Down
                    if event.key == pygame.K_DOWN:
                        if self.menu.cursor == "load":
                            self.menu.cursor = "new"
                        elif self.menu.cursor == "new":
                            self.menu.cursor = "rules"
                        elif self.menu.cursor == "rules":
                            self.menu.cursor = "load"
                    # Enter
                    if event.key == pygame.K_RETURN:
                        # if self.menu.cursor == "load":
                        #     self.menu.previous_state = self.menu.state
                        #     self.menu.state = "data"
                        if self.menu.cursor == "new":
                            self.menu.previous_state = self.menu.state
                            self.menu.state = "game"
                            self.state = "game"
                        elif self.menu.cursor == "rules":
                            self.menu.previous_state = self.menu.state
                            self.menu.state = "static"
                            self.menu.static = "rules"
                            key_pressed = True

            # Static Events
            if self.menu.state == "static":
                if event.key == pygame.K_RETURN:
                    if self.menu.static == "rules" or self.menu.static == "game over" or self.menu.static == "end":
                        if not key_pressed:
                            self.menu.previous_state = self.menu.state
                            self.menu.state = "main"
                if self.menu.static == "won":
                    if not key_pressed:
                        self.menu.previous_state = self.menu.state
                        self.menu.state = "game"
                # if self.menu.static == "game over":
                #     if event.key == pygame.K_RETURN:
                #         if not key_pressed:
                #             self.menu.previous_state = self.menu.state
                #             self.menu.state = "main"

            # Game Events
            if self.state == "game":
                # Left
                if event.key == pygame.K_LEFT:
                    if self.player.hit_box[0] > 0:
                        next_x -= self.player.vel
                        key_pressed = True
                # Right
                if event.key == pygame.K_RIGHT:
                    if self.player.hit_box[0] < 608:
                        next_x += self.player.vel
                        key_pressed = True
                # Up
                if event.key == pygame.K_UP:
                    if self.player.hit_box[1] > 0:
                        next_y -= self.player.vel
                        key_pressed = True
                # Down
                if event.key == pygame.K_DOWN:
                    if self.player.hit_box[1] < 448:
                        next_y += self.player.vel
                        key_pressed = True

                # Checking wall
                for wall in self.room.objects["G"]:
                    if self.player.hit_box[0] + next_x == wall.hit_box[0] and \
                            self.player.hit_box[1] + next_y == wall.hit_box[1]:
                        return

                # Moving player
                self.player.hit_box[0] += next_x
                self.player.hit_box[1] += next_y

                # Detecting monsters
                for monster in self.room.objects["M"]:
                    if self.player.hit_box[0] == monster.hit_box[0] and \
                            self.player.hit_box[1] == monster.hit_box[1]:
                        self.menu.previous_state = self.menu.state
                        self.menu.state = "battle"
                        self.state = "battle"

                # Go to inventory
                if self.menu.state != "static":
                    if event.key == pygame.K_ESCAPE:
                        self.menu.previous_state = self.menu.state
                        self.menu.state = "inventory"
                        self.state = "inventory"
                        key_pressed = True
                        self.inventory_click = True

            # Inventory events
            if self.menu.state == "inventory":
                if self.menu.item_selector >= 0:
                    # Left
                    if event.key == pygame.K_LEFT:
                        if self.menu.item_selector > 0:
                            self.menu.item_selector -= 1
                        elif self.menu.item_selector == 0:
                            self.menu.item_selector -= 1
                            self.menu.stuff_selector = "L"
                        key_pressed = True
                    # Right
                    if event.key == pygame.K_RIGHT:
                        if self.menu.item_selector < self.player.inventory_len() - 1:
                            self.menu.item_selector += 1
                        key_pressed = True
                else:
                    if not key_pressed:
                        # Left
                        if event.key == pygame.K_LEFT:
                            if self.menu.stuff_selector == "L":
                                self.menu.stuff_selector = "B"
                            elif self.menu.stuff_selector == "B":
                                self.menu.stuff_selector = "LH"
                            elif self.menu.stuff_selector == "LH":
                                self.menu.stuff_selector = "RH"
                            elif self.menu.stuff_selector == "RH":
                                self.menu.stuff_selector = "H"
                        # Right
                        if event.key == pygame.K_RIGHT:
                            if self.menu.stuff_selector == "H":
                                self.menu.stuff_selector = "RH"
                            elif self.menu.stuff_selector == "RH":
                                self.menu.stuff_selector = "LH"
                            elif self.menu.stuff_selector == "LH":
                                self.menu.stuff_selector = "B"
                            elif self.menu.stuff_selector == "B":
                                self.menu.stuff_selector = "L"
                            elif self.menu.stuff_selector == "L":
                                self.menu.item_selector += 1

                # Enter
                if event.key == pygame.K_RETURN:
                    if self.player.inventory:
                        if self.player.inventory[self.menu.item_selector].kind == "item":
                            if self.player.inventory[self.menu.item_selector].condition(self.player):
                                self.player.apply_item(self.menu.item_selector)
                                if self.menu.previous_state == "battling":
                                    self.player.take_dmg(self.enemy)
                                    self.player.checking_death(self.enemy, self.room, self.menu, self)
                                    self.state = "battle"
                                    self.menu.previous_state = self.menu.state
                                    self.menu.state = "battling"
                                    key_pressed = True
                                if self.menu.item_selector > self.player.inventory_len() - 1:
                                    self.menu.item_selector -= 1
                        elif self.player.inventory[self.menu.item_selector].kind == "stuff":
                            if self.menu.previous_state != "battling":
                                if self.menu.item_selector >= 0:
                                    self.player.equip_stuff(self.menu.item_selector)
                                    key_pressed = True
                                    if self.menu.item_selector > self.player.inventory_len() - 1:
                                        self.menu.item_selector -= 1

                    # Take off stuff
                    if not key_pressed:
                        if self.player.stuff:
                            if self.menu.item_selector < 0:
                                if self.player.stuff[self.menu.stuff_selector]:
                                    self.player.takeoff_stuff(self.menu.stuff_selector)

                # Delete
                if self.player.inventory:
                    if event.key == pygame.K_DELETE:
                        self.player.del_item(self.menu.item_selector)
                        self.menu.item_selector -= 1
                # Escape
                if not key_pressed:
                    if event.key == pygame.K_ESCAPE:
                        if self.menu.previous_state == "battling":
                            self.state = "battle"
                            self.menu.previous_state = self.menu.state
                            self.menu.state = "battling"
                        else:
                            self.state = self.menu.previous_state
                            self.menu.previous_state = self.menu.state
                            self.menu.state = self.state
                        self.inventory_click = False

            # Battle Menu events
            if self.state == "battle":
                # Prebattle menu
                if self.menu.state == "battle":
                    if not key_pressed:
                        # Up
                        if event.key == pygame.K_UP:
                            if self.menu.cursor == "battle":
                                self.menu.cursor = "run"
                            elif self.menu.cursor == "run":
                                self.menu.cursor = "battle"
                        # Down
                        if event.key == pygame.K_DOWN:
                            if self.menu.cursor == "battle":
                                self.menu.cursor = "run"
                            elif self.menu.cursor == "run":
                                self.menu.cursor = "battle"
                        # Enter
                        if event.key == pygame.K_RETURN:
                            if self.menu.cursor == "battle":
                                self.menu.previous_state = self.menu.state
                                self.menu.state = "battling"
                            elif self.menu.cursor == "run":
                                self.menu.previous_state = self.menu.state
                                self.menu.state = "game"
                                self.state = "game"

                # Battling menu
                elif self.menu.state == "battling":
                    # Right
                    if event.key == pygame.K_RIGHT:
                        if self.menu.cursor == "attack":
                            self.menu.cursor = "cast spell"
                        elif self.menu.cursor == "cast spell":
                            self.menu.cursor = "inventory"
                        elif self.menu.cursor == "inventory":
                            self.menu.cursor = "attack"
                    # Left
                    if event.key == pygame.K_LEFT:
                        if self.menu.cursor == "attack":
                            self.menu.cursor = "inventory"
                        elif self.menu.cursor == "cast spell":
                            self.menu.cursor = "attack"
                        elif self.menu.cursor == "inventory":
                            self.menu.cursor = "cast spell"
                    # Enter
                    if event.key == pygame.K_RETURN:
                        if not key_pressed:
                            if self.menu.cursor == "attack":
                                self.player.attack(self.enemy)
                                self.player.checking_death(self.enemy, self.room, self.menu, self)
                            elif self.menu.cursor == "cast spell":
                                self.player.cast_spell(self.enemy)
                                self.player.checking_death(self.enemy, self.room, self.menu, self)
                            elif self.menu.cursor == "inventory":
                                self.menu.previous_state = self.menu.state
                                self.menu.state = "inventory"
                                self.state = "inventory"
