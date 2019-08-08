import StoreGenerator
# Starting off as main class getting data from other classes

# Varaibles
availableGenerators = []
selectedGenerator = None

# Presenting choices on what to generate
# Displaying the generator

print('Select a generator from the following: \n' + '1. Shop Generator\n')
selectedGenerator = input('Choice as a number: ')
selectedGenerator = int(selectedGenerator)

if selectedGenerator == 1:
    StoreGenerator.main()
else:
    print('No such generator exists! Exiting for now...')
