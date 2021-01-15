import random
from Thing.Stuff.Stuff import Stuff


class Artefact(Stuff):
    def __init__(self, window):
        super().__init__(window)
        self.name = "Shirt"
        self.place = "LH"
        self.effect = random.randint(5, 10)
        self.stat = "Armor"
        self.description = []
        self.inventory_rect = [32, 328, 32, 32]
        self.inventory_color = (255, 0, 255)

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
        player.armor += self.effect

    def take_stuff_off(self, player):
        player.armor -= self.effect
