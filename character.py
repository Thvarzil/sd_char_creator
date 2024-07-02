import random, math

from helpers import use_modifier, generate_stat, generate_lv0_gear
from ancestries import ancestral_mutator
from classes import class_mutator

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
        
        #level 1 exclusives
        if self.level>0:
            #apply class
            class_mutator(self)
            
            self.hit_points = random.randint(1, self.hit_die)
            if self.constitution>10:
                self.hit_points+=use_modifier(self.constitution)
            else:
                self.hit_points+=1
            #TODO implement talents

        # not numerically relevant
        # TODO implement backgrounds
        self.background = None
        self.gear.append(generate_lv0_gear())
