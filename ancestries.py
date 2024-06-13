import random

from character import Character
from constants import LANGUAGES

def dwarf_mutator(mutee: Character):
    mutee.ancestry = 'Dwarf'
    mutee.languages += ['Dwarvish']
    mutee.feats += 'Stout. +2 maximum hit points. Roll hit points per level with advantage.'
    mutee.hit_points += 2

def elf_mutator(mutee: Character):
    mutee.ancestry = 'Elf'
    mutee.languages += ['Elvish', 'Sylvan']
    mutee.feats += 'Farsight. You get a +1 bonus to attack rolls with ranged weapons or a +1 bonus to spellcasting checks.'

def goblin_mutator(mutee: Character):
    mutee.ancestry = 'Goblin'
    mutee.languages += ['Goblin']
    mutee.feats += 'Keen Eyes. You cant be surprised.'

def half_orc_mutator(mutee: Character):
    mutee.ancestry = 'Half-Orc'
    mutee.languages += ['Orcish']
    mutee.feats += 'Mighty. You have a +1 bonus to attack and damage rolls with melee weapons.'

def halfling_mutator(mutee: Character):
    mutee.ancestry = 'Halfling'
    mutee.feats += 'Stealthy. Once per day, you can become invisible for 3 rounds'

def human_mutator(mutee: Character):
    mutee.ancestry = 'Human'
    mutee.languages += LANGUAGES(random.randint(0,8))
    mutee.feats += 'Ambitious. You gain one additional talent roll at 1st level.'

ANCESTRIES = [dwarf_mutator, elf_mutator, goblin_mutator, half_orc_mutator, halfling_mutator, human_mutator]
