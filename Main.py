import npc_generator as npcgen
import sqlite3
from sqlite3 import Error

# Starting off as main class getting data from other classes

# Varaibles
availableGenerators = ['NPC generator', 'Store Generator']
selectedGenerator = None


# Creating the connection to the database
def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


# Presenting choices on what to generate
# Displaying the generator
# create_connection('data/FantasyGeneratorDB.db')

# Running the program
# TODO: Swtich to always on unless told to quit.

# print('Select a store type:\n')
# count = 1
# for gen in availableGenerators:
#     print(str(count) + ': ' + gen)
#     count += 1
#
# selectedGenerator = input('\nChoice as a number: ')
# selectedGenerator = int(selectedGenerator)
#
# if selectedGenerator == 1:
#     npcgen.main()
# elif selectedGenerator == 2:
#     storegen.main()
# else:
#     print('No such generator exists! Exiting for now...')

print('NPC Generator')
npcgen.main()
