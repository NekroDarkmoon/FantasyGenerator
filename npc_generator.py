# Imports
import random
import linecache
import sqlite3
from sqlite3 import Error
import re

# Gonna start of with a simple npc generator and then over time make it more
# complex and sofisticated.

# Variables
f_names = 'data/name_dict2.txt'
gen_num = 0
npc = {
    'First Name': '',
    'Last Name': '',
    'Gender': '',
    'Race': '',
    'Age': '',
    'Hair color': '',
    'Height': '',
    'Weight': ''
}
norm_races = {
    'Human': 90,
    'Dwarf': 350,
    'Elf': 750,
    'Halfling': 250,
    'Dragonborn': 80,
    'Gnome': 500,
    'Half-Elf': 180,
    'Half-orc': 75,
    'Teifling': 100
}

all_races = []


def get_name():
    # Generating a random number
    # Generating the first name
    gen_num = random.randint(1, 48529)
    line = linecache.getline(f_names, gen_num)

    # Get gender in the future <3
    # Adding it to the main array
    npc['First Name'] = (line[3:-1])

    # Generating the last name
    gen_num = random.randint(1, 48529)
    npc['Last Name'] = (linecache.getline(f_names, gen_num)[3:-1])
    # DEBUG: print(npc)
    return None


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                                 NPC GENERATION
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# TODO: Randomize the default sleection as well
def generateNPC(gender, race):

    # Get a name for the npc
    get_name()

    # Generate various details for the NPC in the order
    # **************************************************
    # *   Race
    # *   Age
    # *   Hair color
    # *   Height
    # *   Weight
    # **************************************************

    # Generating Race
    # TODO: Allow for a larger selection of races
    npc['Race'] = race
    if len(race) == 0:
        race = random.choice(list(norm_races))
    npc['Race'] = race

    # Connecting to the dataase
    conn = sqlite3.connect('data/FantasyGeneratorDB.db')
    c = conn.cursor()
    # Generating age
    # TODO: Maybe setup a max age possible
    npc['Age'] = random.randint(10, norm_races[race])
    # TODO: Generate hair color
    # TODO: Generate Weight

    # TODO: Generate Height
    # Getting height data according to race and cleaning it up for use

    query = f"SELECT Base_Height FROM races WHERE Race = '{race}' "
    c.execute(query)
    base_height = str(c.fetchone())
    base_height = re.sub("[^0-9]", "", base_height)

    print(base_height)
    query = f"SELECT Height_Modfier FROM races WHERE Race = '{race}'"
    c.execute(query)
    mod_height = str(c.fetchone())
    mod_height = mod_height.strip("'(),")
    print(mod_height)

    # Calculating the actual age and appending to the dict
    base_height = int(base_height)
    x = mod_height[1]
    x = int(x)
    y = int(mod_height[3:])

    height = base_height + (x * random.randint(1, (y+1)))

    npc['Height'] = height

    # Closing the connection
    conn.close()

    # Returning the NPC
    return npc


def main():
    # Get input on the type of NPC that is to be generated

    gender = input('Would you like the NPC to be (M)ale or (Female): ')
    race = input('What race would you like to choose: ')
    print(generateNPC(gender, race))
