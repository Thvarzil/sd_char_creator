import random

from helpers import use_modifier, generate_stat, generate_lv0_gear
from ancestries import ancestral_mutator

class Character():
    languages = ["Common",]
    gear = []
    talents = []
    feats = []
    hit_points = 0
    max_gear_slots = 10

    def __init__(self, *args):
        
    
        # raw attributes
        if (args): 
            self.level=args[0] 
        else: 
            self.level=1

        # TODO implement reroll if no stat is >=14
        self.strength = generate_stat()
        self.dexterity = generate_stat()
        self.constitution = generate_stat()
        self.intelligence = generate_stat()
        self.wisdom = generate_stat()
        self.charisma = generate_stat()

        # apply ancestral mutations
        ancestral_mutator(self)

        # derived stats
        self.hit_points += use_modifier(self.constitution) if use_modifier(self.constitution)>1 else 1 
        self.armor_class = 10+use_modifier(self.dexterity)
        if self.strength>10:
            self.max_gear_slots = self.strength

        # not numerically relevant
        self.background = None
        self.gear.append(generate_lv0_gear())
