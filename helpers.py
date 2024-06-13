import math, random

from character import Character
from constants import ANCESTRIES, BASIC_GEAR

def use_modifier(stat: int):
    return math.floor((stat-10)/2)

def generate_stat():
    return random.randint(1,6) + random.randint(1,6) + random.randint(1,6)

def generate_lv0_gear():
    iter = random.randint(1,4)
    gear = []
    for i in iter:
        gear.append(BASIC_GEAR[random.randint(1,12)])
    return

def use_ancestry_mutator(mutee: Character):
    # TODO
    # this will need to select a random entry from the ANCESTRIES constant, 
    # and apply the contained mutation to the passed in Character instance
    return