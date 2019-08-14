# Imports
import random
import linecache

# Gonna start of with a simple npc generator and then over time make it more
# complex and sofisticated.

# Variables
f_names = 'data/name_dict2.txt'
gen_num = 0
npc = []


def get_name():
    # Generating a random number
    gen_num = random.randint(1, 48529)
    line = linecache.getlines(f_names, gen_num)
    print(line)
    return None


def generateNPC(gender):

    # Get a name for the npc
    get_name()
    return None


def main():
    # Get input on the type of NPC that is to be generated

    gender = input('Would you like the NPC to be (M)ale or (Female): ')
    print(generateNPC(gender))
