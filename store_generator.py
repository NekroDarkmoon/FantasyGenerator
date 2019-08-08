# Information
# store array is a string array that goes in the following order
#  Store Name , Store description, Npcs


# Imports
import npc_generator
import math

# Store generator
# Varaibles
storeTypes = ['General Store']
selectedStore = []
generatedStore = []


def generateStore(selectedStore):
    # Create name of the store
    # Generating a name for the store
    storeName = 'Names to be added'
    generatedStore.append(storeName)

    # Give the store a description
    storeDescription = 'To be added'
    generatedStore.append(storeDescription)

    # Give the store npc's
    # Generate an NPC
    generatedStore.append(npc_generator.main())

    # Generate items for the store
    # Getting the number of items requested
    item_count = selectedStore[1]

    # Generating items

    # Send all the information to a beautifier
    # Send data back to main to be printed

    return None


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
