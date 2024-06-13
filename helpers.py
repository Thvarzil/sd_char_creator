import math, random

from character import Character
from constants import BASIC_GEAR
from ancestries import ANCESTRIES

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