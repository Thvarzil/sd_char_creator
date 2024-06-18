import random

from constants import LANGUAGES
def class_mutator(mutee):
    match (random.randint(1,4)):
        case 1:
            mutee.char_class = 'Fighter'
            mutee.hit_die = 8
            mutee.weapons = ['All']
            mutee.armor = ['All']
            mutee.is_spellcaster = False
        case 2:
            mutee.char_class = 'Priest'
            mutee.hit_die = 6
            mutee.weapons = ['Club', 'crossbow', 'Dagger', 'Mace', 'Longsword', 'Staff', 'Warhammer']
            mutee.armor = ['All']
            mutee.is_spellcaster = True
            languages = ['Celestial', 'Demonic', 'Primordial']
            mutee.languages += languages[random.randint(0,2)]
        case 3:
            mutee.char_class = 'Thief'
            mutee.hit_die = 4
            mutee.weapons = ['Club', 'Crossbow', 'Dagger', 'Shortbow', 'Shortsword']
            mutee.armor = ['Leather Armor', 'Mithral Chainmail']
            mutee.is_spellcaster = False
        case 4:
            mutee.char_class = 'Wizard'
            mutee.hit_die = 4
            mutee.weapons = ['Dagger', 'Staff']
            mutee.armor = []
            mutee.is_spellcaster = True
