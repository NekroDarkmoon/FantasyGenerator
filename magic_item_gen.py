import random
from numpy.random import choice

# TABLES

table_a = ['Potion of healing', 'Spell scroll (cantrip)', 'Potion of climbing',
           'Spell scroll (1st level)', 'Spell scroll (2nd level)',
           'Potion of healing (greater)', 'Bag of holding', 'Driftglobe']

table_b = ['Potion of healing (greater)', 'Potion of fire breath', 'Potion of resistance',
           'Ammunition, +1', 'Potion of animal friendship', 'Potion of hill giant strength',
           'Potion of growth', 'Potion of water breathing', 'Spell scroll (2nd level)',
           'Spell scroll (3rd level)', 'Bag of holding', 'Keoghtom’s ointment',
           'Oil of slipperiness', 'Dust of disappearance' 'Dust of dryness',
           'Dust of sneezing and choking', 'Elemental gem', 'Philter of love',
           random.choice(['Alchemy jug', 'Cap of water breathing','Cloak of the manta ray',
           'Driftglobe', 'Goggles of night', 'Helm of comprehending languages',
           'Immovable rod', 'Lantern of revealing', 'Mariner’s armor',
           'Mithral armor', 'Potion of poison','Ring of swimming','Robe of useful items',
           'Rope of climbing','Saddle of the cavalier', 'Wand of magic detection',
           'Wand of secrets'])]


#
# 01–15 	Potion of healing (greater)
# 16–22 	Potion of fire breath
# 23–29 	Potion of resistance
# 30–34 	Ammunition, +1
# 35–39 	Potion of animal friendship
# 40–44 	Potion of hill giant strength
# 45–49 	Potion of growth
# 50–54 	Potion of water breathing
# 55–59 	Spell scroll (2nd level)
# 60–64 	Spell scroll (3rd level)
# 65–67 	Bag of holding
# 68–70 	Keoghtom’s ointment
# 71–73 	Oil of slipperiness
# 74–75 	Dust of disappearance
# 76–77 	Dust of dryness
# 78–79 	Dust of sneezing and choking
# 80–81 	Elemental gem
# 82–83 	Philter of love
# 84 	Alchemy jug
# 85 	Cap of water breathing
# 86 	Cloak of the manta ray
# 87 	Driftglobe
# 88 	Goggles of night
# 89 	Helm of comprehending languages
# 90 	Immovable rod
# 91 	Lantern of revealing
# 92 	Mariner’s armor
# 93 	Mithral armor
# 94 	Potion of poison
# 95 	Ring of swimming
# 96 	Robe of useful items
# 97 	Rope of climbing
# 98 	Saddle of the cavalier
# 99 	Wand of magic detection
# 00 	Wand of secrets
#


# GET INPUT TIME AND MONEY
money_spent = int(input("Money invested: "))
time_spent = int(input("Weeks spent: "))
charisma_roll = int(input("Charisma check: "))

# ITEM DESIRED CODE

#
# Common: 10+
# Uncommon: 15+
# Rare: 20+
# Very rare: 25+
# Legendary: 30+

# ADDING THE MODIFIERS TO THE ROLL
mon_mod = int((money_spent / 100) - 1)
time_mod = int(time_spent - 1)

final_mod = charisma_roll + mon_mod + time_mod

# SELECTING THE APPROPRIATE TABLE
selected_table = 'A'

if final_mod > 5:
    selected_table = 'B'

if final_mod > 10:
    selected_table = 'C'

if final_mod > 15:
    selected_table = 'D'

if final_mod > 20:
    selected_table = 'E'

if final_mod > 25:
    selected_table = 'F'

if final_mod > 30:
    selected_table = 'G'

if final_mod > 35:
    selected_table = 'H'

if final_mod > 40:
    selected_table = 'I'


# Getting data from the table

if selected_table == 'A':
    gen_no = random.randint(0, 6)
    dice_roll = random.randint(1, 100)
    draw = choice(table_a, gen_no, p=[0.5, 0.1, 0.1, 0.2, 0.04, 0.04, 0.01, 0.01])

if selected_table == 'B':
    gen_no = random.randint(0, 4)
    dice_roll = random.randint(1, 100)
    draw = choice(table_a, gen_no, p=[0.15, 0.07, 0.07, 0.05, 0.05, 0.05, 0.05, 0.05,0.05,0.05,0.03,0.03,0.02,0.02,0.02,0.02,0.02,0.02,0.1])


if selected_table == 'C':
    gen_no = random.randint(0, 4)
    dice_roll = random.randint(1, 100)
    draw = choice(table_a, gen_no, p=[0.5, 0.1, 0.1, 0.2, 0.04, 0.04, 0.01, 0.01])

if selected_table == 'D':
    gen_no = random.randint(0, 4)
    dice_roll = random.randint(1, 100)
    draw = choice(table_a, gen_no, p=[0.5, 0.1, 0.1, 0.2, 0.04, 0.04, 0.01, 0.01])

if selected_table == 'E':
    gen_no = random.randint(0, 4)
    dice_roll = random.randint(1, 100)
    draw = choice(table_a, gen_no, p=[0.5, 0.1, 0.1, 0.2, 0.04, 0.04, 0.01, 0.01])

if selected_table == 'F':
    gen_no = random.randint(0, 4)
    dice_roll = random.randint(1, 100)
    draw = choice(table_a, gen_no, p=[0.5, 0.1, 0.1, 0.2, 0.04, 0.04, 0.01, 0.01])

if selected_table == 'G':
    gen_no = random.randint(0, 4)
    dice_roll = random.randint(1, 100)
    draw = choice(table_a, gen_no, p=[0.5, 0.1, 0.1, 0.2, 0.04, 0.04, 0.01, 0.01])

if selected_table == 'H':
    gen_no = random.randint(0, 4)
    dice_roll = random.randint(1, 100)
    draw = choice(table_a, gen_no, p=[0.5, 0.1, 0.1, 0.2, 0.04, 0.04, 0.01, 0.01])

if selected_table == 'I':
    gen_no = random.randint(0, 4)
    dice_roll = random.randint(1, 100)
    draw = choice(table_a, gen_no, p=[0.5, 0.1, 0.1, 0.2, 0.04, 0.04, 0.01, 0.01])

print(draw)
