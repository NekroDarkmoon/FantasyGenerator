import store_generator as storegen
# import mysql.connector


# Starting off as main class getting data from other classes

# # Establishing a database
# mydb = mysql.connector.connect(
#     host="localhost",
#     user1="admin",
#     psswd="nada"
# )
#
# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE FantasyGenerator")
#

# Varaibles
availableGenerators = []
selectedGenerator = None

# Presenting choices on what to generate
# Displaying the generator
print('Select a generator from the following: \n' + '1. Shop Generator\n')
selectedGenerator = input('Choice as a number: ')
selectedGenerator = int(selectedGenerator)

if selectedGenerator == 1:
    storegen.main()
else:
    print('No such generator exists! Exiting for now...')
