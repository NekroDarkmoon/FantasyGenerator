
# Imports

# Store generator
# Varaibles
storeTypes = ['General Store']
selectedStore = []


def generateStore(selectedStore):
    # Create name of the store
    # Generating a name for the store
    # Give the store a description
    # Give the store npc's
    # Generate items for the store
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

    selectedStore = input('Choice: ')

    selectedStore = str(
        input('How many items do you wish for the store to have: '))

    generateStore(selectedStore)
