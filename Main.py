import store_generator as storegen
import npc_generator as npcgen
import sqlite3
from sqlite3 import Error

# Starting off as main class getting data from other classes

# Varaibles
availableGenerators = []
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
print('Select a generator from the following: \n' + '1. Shop Generator\n')
selectedGenerator = input('Choice as a number: ')
selectedGenerator = int(selectedGenerator)

if selectedGenerator == 1:
    storegen.main()
elif selectedGenerator == 2:
    npcgen.main()
else:
    print('No such generator exists! Exiting for now...')
