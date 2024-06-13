from character import Character

def dwarf_mutator(mutee: Character):
    mutee.ancestry = 'Dwarf'
    mutee.languages += ['Dwarvish']
    mutee.feats += 'Stout. +2 maximum hit points. Roll hit points per level with advantage.'
    mutee.hit_points += 2

def elf_mutator(mutee: Character):
    mutee.ancestry = ''
    mutee.languages += []
    mutee.feats += ''
    return
def goblin_mutator(mutee: Character):
    mutee.ancestry = ''
    mutee.languages += []
    mutee.feats += ''
    return
def half_orc_mutator(mutee: Character):
    mutee.ancestry = ''
    mutee.languages += []
    mutee.feats += ''
    return
def halfling_mutator(mutee: Character):
    mutee.ancestry = ''
    mutee.languages += []
    mutee.feats += ''
    return
def human_mutator(mutee: Character):
    mutee.ancestry = ''
    mutee.languages += []
    mutee.feats += ''
    return

ANCESTRIES = [dwarf_mutator, elf_mutator, goblin_mutator, half_orc_mutator, halfling_mutator, human_mutator]
