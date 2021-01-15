from Thing.Thing import Thing
import random


class Map(Thing):
    def __init__(self):
        super().__init__(32, 32)

        self.tile = ["CGGGGGGGGGGGGGGGGGGG",
                     "G  WW WWTWW WWTWW BG",
                     "G                  G",
                     "G  WW WWTWW WWTWW  G",
                     "G  WWTWW WWIWW WW  G",
                     "G      R     R     G",
                     "G  WW WW WW WW WW  G",
                     "G RWW WWTWW WWTWW  G",
                     "G         R     R  G",
                     "G  WWTWW WW WWTWW  G",
                     "G  WW WW WWTWW WW  G",
                     "G    R     R       G",
                     "G  WWTWW WW WW WW  G",
                     "G  WW WWTWW WWTWW DG",
                     "GGGGGGGGGGGGGGGGGGGG"]

    def reset_map(self):

        self.tile = ["CGGGGGGGGGGGGGGGGGGG",
                 "G  WW WWTWW WWTWW BG",
                 "G                  G",
                 "G  WW WWTWW WWTWW  G",
                 "G  WWTWW WWIWW WW  G",
                 "G      R     R     G",
                 "G  WW WW WW WW WW  G",
                 "G RWW WWTWW WWTWW  G",
                 "G         R     R  G",
                 "G  WWTWW WW WWTWW  G",
                 "G  WW WW WWTWW WW  G",
                 "G    R     R       G",
                 "G  WWTWW WW WW WW  G",
                 "G  WW WWTWW WWTWW DG",
                 "GGGGGGGGGGGGGGGGGGGG"]

    def boss_map(self):

        self.tile = ["CGGGGGGGGGGGGGGGGGGG",
                 "G  WW WW WW WW WW  G",
                 "G                  G",
                 "G  WW WW WW WW WW  G",
                 "G  WW WW WW WW WW  G",
                 "G                  G",
                 "G  WWWWWWWWWWWWWW  G",
                 "G  WWWWWWWWWWWWWW  G",
                 "G        M WWWWWW  G",
                 "G  WWWWWWWWWWWWWW  G",
                 "G  WWWWWWWWWWWWWW  G",
                 "G                  G",
                 "G  WW WW WW WW WW  G",
                 "G  WW WW WW WW WW DG",
                 "GGGGGGGGGGGGGGGGGGGG"]

    def random_map(self):
        for key, line in enumerate(self.tile):
            for key1, letter in enumerate(line):
                if letter == "R":
                    new_list = list(line)
                    new_list[key1] = random.choice(["M", " ", " "])
                    self.tile[key] = "".join(new_list)
                if letter == "T":
                    new_list = list(line)
                    new_list[key1] = random.choice(["I", " ", " ", " ", " ", " "])
                    self.tile[key] = "".join(new_list)
                if letter == "W":
                    new_list = list(line)
                    new_list[key1] = random.choice(["G", " "])
                    self.tile[key] = "".join(new_list)
                if letter == "B":
                    new_list = list(line)
                    new_list[key1] = random.choice(["D", " "])
                    self.tile[key] = "".join(new_list)