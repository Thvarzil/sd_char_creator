import math, random

from constants import BASIC_GEAR

def use_modifier(stat: int):
    return math.floor((stat-10)/2)

def generate_stat():
    return random.randint(1,6) + random.randint(1,6) + random.randint(1,6)

def generate_lv0_gear():
    iter = random.randint(1,4)
    gear = []
    for i in range(1,iter):
        gear.append(BASIC_GEAR[random.randint(0,11)])
    return gear