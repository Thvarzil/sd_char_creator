import random

from constants import LANGUAGES
def ancestral_mutator(mutee):
    match (random.randint(1,6)):
        case 1:
            mutee.ancestry = 'Dwarf'
            mutee.languages += ['Dwarvish']
            mutee.feats += 'Stout. +2 maximum hit points. Roll hit points per level with advantage.'
            mutee.hit_points += 2

        case 2:
            mutee.ancestry = 'Elf'
            mutee.languages += ['Elvish', 'Sylvan']
            mutee.feats += 'Farsight. You get a +1 bonus to attack rolls with ranged weapons or a +1 bonus to spellcasting checks.'
        
        case 3:
            mutee.ancestry = 'Goblin'
            mutee.languages += ['Goblin']
            mutee.feats += 'Keen Eyes. You cant be surprised.'
        
        case 4:
            mutee.ancestry = 'Half-Orc'
            mutee.languages += ['Orcish']
            mutee.feats += 'Mighty. You have a +1 bonus to attack and damage rolls with melee weapons.'
        
        case 5:
            mutee.ancestry = 'Halfling'
            mutee.feats += 'Stealthy. Once per day, you can become invisible for 3 rounds'
        
        case 6:
            mutee.ancestry = 'Human'
            mutee.languages += LANGUAGES[random.randint(0,8)]
            mutee.feats += 'Ambitious. You gain one additional talent roll at 1st level.'
            
