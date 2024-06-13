import math, random

def use_modifier(stat: int):
    return math.floor((stat-10)/2)

def generate_stat():
    return random.randint(1,6) + random.randint(1,6) + random.randint(1,6)

def generate_lv0_gear():
    # TODO
    return None