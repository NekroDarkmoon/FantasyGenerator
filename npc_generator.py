# Imports
import random
import linecache
import sqlite3
import re

# Gonna start of with a simple npc generator and then over time make it more
# complex and sofisticated.

# Variables
f_names = 'data/name_dict2.txt'
gen_num = 0
npc_number = 1
npc = {
    'First Name': '',
    'Last Name': '',
    'Gender': '',
    'Race': '',
    'Age': '',
    'Height': '',
    'Weight': '',
    'Type': '',
    'Abilities': []
}
norm_races = {
    'Human': 90,
    'Dwarf': 350,
    'Elf': 750,
    'Halfling': 250,
    'Dragonborn': 80,
    'Gnome': 500,
    'Half-Elf': 180,
    'Half-Orc': 75,
    'Tiefling': 100
}


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
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                                 NPC GENERATION                              #
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def generateNPC(gender, race, is_adventurer):

    # Get a name for the npc
    get_name()

    # Connecting to the dataase
    conn = sqlite3.connect('data/FantasyGeneratorDB.db')
    c = conn.cursor()


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                                 GENDER GENERATION
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    if len(gender) == 0:
        x = random.randint(1, 7)
        if x < 3:
            npc['Gender'] = 'Male'
        else:
            npc['Gender'] = 'Female'
    else:
        npc['Gender'] = gender

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                                 RACE GENERATION
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Generating Race
    # TODO: Allow for a larger selection of races
    npc['Race'] = race
    if len(race) == 0:
        race = random.choice(list(norm_races))
    npc['Race'] = race

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                                 AGE GENERATION
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    # Generating age
    # TODO: Maybe setup a max age possible
    npc['Age'] = random.randint(10, norm_races[race])


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                                 WEIGHT GENERATION
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Getting weight data according to race and cleaning it up for use

    query = f"SELECT Base_Weight FROM races WHERE Race = '{race}'"
    c.execute(query)
    base_weight = str(c.fetchone())
    base_weight = re.sub("[^0-9]", "", base_weight)

    query = f"SELECT Weight_Modfier FROM races WHERE Race = '{race}'"
    c.execute(query)
    mod_weight = str(c.fetchone())
    mod_weight = mod_weight.strip("'(),")

    # Calculating weight and appending to dict

    base_weight = int(base_weight)

    if mod_weight == '*1':
        weight = base_weight + (random.randint(-11, 11))
    else:
        x = mod_weight[1]
        x = int(x)
        y = int(mod_weight[3:])
        weight = base_weight + (x * random.randint(1, (y + 1)))

    npc['Weight'] = weight


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                                 HEIGHT GENERATION
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    # Generating Height
    # Getting height data according to race and cleaning it up for use

    query = f"SELECT Base_Height FROM races WHERE Race = '{race}' "
    c.execute(query)
    base_height = str(c.fetchone())
    base_height = re.sub("[^0-9]", "", base_height)

    query = f"SELECT Height_Modfier FROM races WHERE Race = '{race}'"
    c.execute(query)
    mod_height = str(c.fetchone())
    mod_height = mod_height.strip("'(),")

    # Calculating the actual age and appending to the dict
    base_height = int(base_height)
    x = mod_height[1]
    x = int(x)
    y = int(mod_height[3:])

    height = base_height + (x * random.randint(1, (y + 1)))

    npc['Height'] = height

    # Closing the connection
    conn.close()


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                              ABILITY GENERATION
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    # Seeing if the npc is an adventurer

    if is_adventurer == 0:
        print(is_adventurer)
        npc['Type'] = 'Commoner'
        # TODO: Randomize this
        npc['Abilities'] = 'Str(10) Dex(10) Con(10) Int(10) Wis(10) Char(10)'
    else:
        print(is_adventurer)
        npc['Type'] = 'Adventurer'

        abilities = ['Str', 'Dex', 'Con', 'Int', 'Wis', 'Char']
        for x in range(0, 6):
            abilities[x] = f"{abilities[x]} ({random.randint(8, 20)})"

        # npc['abilities'] = ['Str', 'Dex', 'Con', 'Int', 'Wis', 'Char']
        # npc['Abilities'] = [stat for stat in abilities]
        npc['Abilities'] = abilities

        # TODO: Add level of char depending on total stat roll

    # --------------------------------------------------------------------------
    # Returning the NPC
    return npc
    # --------------------------------------------------------------------------


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                                   MAIN
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def main():

    # Get input on the type of NPC that is to be generated

    # Getting npc life status
    is_adventurer = '-'
    while ((is_adventurer.lower() != 'y') and (is_adventurer.lower() != 'n') and (is_adventurer != '')):
        is_adventurer = input('Is the npc an is_adventurer? (y/n): ')

    # Setting up life status for function
    if is_adventurer == 'y':
        is_adventurer = 1
    elif is_adventurer == 'n':
        is_adventurer = 0
    else:
        is_adventurer = random.randint(0, 1)

    # Getting npc gender
    gender = '-'
    while ((gender.lower() != 'm') and (gender.lower() != 'f') and (gender != '')):
        gender = input('Would you like the NPC to be (M)ale or (F)emale: ')

    # Getting race choise

    choice_exists = False
    while choice_exists is False:
        print('What race would you like to choose? Leave empty for random: ')
        for race in norm_races:
            print(race)
        chosen_race = input('Choice: ')

        for race in norm_races:
            if (chosen_race == race) | (len(chosen_race) == 0):
                choice_exists = True
                break

        if choice_exists is False:
            print("Chosen race doesn't exist...\n\n")

    npc_number = input("Number of npc's to generate: ")

    # Loop condition satisfier
    if(len((npc_number)) == 0):
        npc_number = 1
    else:
        npc_number = int(npc_number)

    pos = 0
    while pos < npc_number:
        generateNPC(gender, chosen_race, is_adventurer)
        print(f"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Name:       {npc['First Name']} {npc['Last Name']}
Gender:     {npc['Gender']}
Race:       {npc['Race']}
Age:        {npc['Age']}
Height:     {npc['Height']}cm
Weight:     {npc['Weight']}kg
Type:       {npc['Type']}
Abilities:  {npc['Abilities']}

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        """)
        pos += 1
