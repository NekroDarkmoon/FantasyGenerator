# Imports
import random
import linecache

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


def gen_age(race):
    return None


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                                 NPC GENERATION
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# TODO: Randomize the default sleection as well
def generateNPC(gender="M", race="Human"):

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

    # Generating age
    # TODO: Create a seperate function to calculate age in accordance to race.
    npc['Age'] = random.randint(16, 80)

    # TODO: Generate hair color
    # TODO: Generate Weight
    # TODO: Generate Height

    # Returning the NPC
    return npc


def main():
    # Get input on the type of NPC that is to be generated

    gender = input('Would you like the NPC to be (M)ale or (Female): ')
    race = input('What race would you like to choose: ')
    print(generateNPC(gender, race))
