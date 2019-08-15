# Information
# store array is a string array that goes in the following order
#  Store Name , Store description, Npcs


# Imports
import npc_generator
import random

# Store generator
# Varaibles
storeTypes = ['General Store']
selectedStore = []
generatedStore = []

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
#                          BLACKSMITH GENERATOR
#
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
#                         GENERAL STORE GENERATOR
#
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def generateStore(selectedStore):
    # Create name of the store
    # Generating a name for the store
    # Give the store a description
    # Give the store npc's

    # Selecting a random number of npcs to generate and generating them
    # TODO: Beautify this in the future
    num_of_npc = random.randint(1, 3)
    print(num_of_npc)
    while num_of_npc > 0:
        temp = npc_generator.generateNPC('', '')
        generatedStore.append(temp)
        num_of_npc -= 1

    # Generate items for the store
    # Getting the number of items requested
    # Generating items
    # Send all the information to a beautifier
    # Send data back to main to be printed
    return None

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
#                               TAVERN GENERATOR
#
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# TODO: Tavern Name
# TODO: Tavern's Tale
# TODO: The bartender
# TODO: Clientle
# TODO: Accomodations
# TODO: Food
# TODO: Drinks


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
#                                   MAIN
#
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def main():
    # Getting user input on specifics
    count = 1

    print('Select a store type:\n')
    for store in storeTypes:
        print(str(count) + ': ' + store + '\n')
        count += 1

    selectedStore.append(input('Choice: '))

    selectedStore.append(str(
        input('How many items do you wish for the store to have: ')))

    generateStore(selectedStore)
    print(generatedStore)
