from character import Character

char_lv0 = Character(0)
gear_string_lv0 = ''
for item in char_lv0.gear:
    gear_string_lv0+=f'{item}, '
char_default = Character()
char_lv1 = Character(1)

print('Level 0:')
print(f'Level {char_lv0.level} {char_lv0.ancestry}')
print(f'STR: {char_lv0.strength}\tINT: {char_lv0.intelligence}')
print(f'DEX: {char_lv0.dexterity}\tWIS: {char_lv0.wisdom}')
print(f'CON: {char_lv0.constitution}\tCHA: {char_lv0.charisma}')
print()
print(f'HP : {char_lv0.strength}\tAC : {char_lv0.intelligence}')
print(f'Carrying {gear_string_lv0}')
print('<--------------------------------->')
#print('Default: Should be level 1')
#print(char_default)
#print('<--------------------------------->')
#print('Level 1:')
#print(char_lv1)
#print('<--------------------------------->')
