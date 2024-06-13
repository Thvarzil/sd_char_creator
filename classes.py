import random

class Character():
    languages = ["Common",]
    gear = []

    def __init__(self, level):
        # meta attributes
        self.ancestry = None
        self.char_class = None

        # raw attributes
        self.strength = random.randint(1,6)
        self.dexterity = random.randint(1,6)
        self.constitution = random.randint(1,6)
        self.intelligence = random.randint(1,6)
        self.wisdom = random.randint(1,6)
        self.charisma = random.randint(1,6)

        # derived attributes
        self.hit_points = use_modifier(self.constitution) if use_modifier(self.constitution)>1 else 1 
        self.armor_class = 10+use_modifier(self.dexterity)
        self.background = None

        