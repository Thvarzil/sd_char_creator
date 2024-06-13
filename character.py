import random

from helpers import use_modifier, generate_stat, generate_lv0_gear
from ancestries import ANCESTRIES

class Character():
    languages = ["Common",]
    gear = []
    talents = []
    feats = []
    hit_points = 0

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

        # apply ancestral mutations
        ANCESTRIES[random.randint(0,5)](self)

        # derived stats
        self.hit_points += use_modifier(self.constitution) if use_modifier(self.constitution)>1 else 1 
        self.armor_class = 10+use_modifier(self.dexterity)

        # not numerically relevant
        self.background = None
        self.gear.append(generate_lv0_gear())
