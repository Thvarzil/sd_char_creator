import random

from helpers import use_modifier, generate_stat, generate_lv0_gear

class Character():
    languages = ["Common",]
    gear = []
    talents = []

    def __init__(self, *args):
        # TODO find a more elegant way to do this
        if args:
            level = args()[0]
        else:
            level = 1

        # raw attributes
        self.level = level
        self.strength = generate_stat()
        self.dexterity = generate_stat()
        self.constitution = generate_stat()
        self.intelligence = generate_stat()
        self.wisdom = generate_stat()
        self.charisma = generate_stat()

        # above derived attributes in case ancestry affects an attribute
        self.ancestry = None

        # derived attributes
        self.hit_points = use_modifier(self.constitution) if use_modifier(self.constitution)>1 else 1 
        self.armor_class = 10+use_modifier(self.dexterity)

        # not numerically relevant
        self.background = None
        self.gear.append(generate_lv0_gear())
