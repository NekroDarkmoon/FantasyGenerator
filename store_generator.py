# Information
# store array is a string array that goes in the following order
#  Store Name , Store description, Npcs


# Imports
import npc_generator
import random

# Store generator
# Varaibles
storeTypes = ['General Store', 'Tavern']
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

def tavern_generator():
    # TODO: Tavern Name
    name_prefix = ['striped', 'irritate', 'instinctive', 'zealous', 'sleet',
                   'throat', 'death', 'fine', 'bouncy', 'sugar', 'slow', 'grade', 'adhesive',
                   'match', 'bath', 'racial', 'pigs', 'alluring', 'debt', 'well-made',
                   'superficial', 'snatch', 'debonair', 'annoyed', 'earn', 'notice', 'attract',
                   'arch', 'soda', 'battle', 'panoramic', 'destruction', 'scintillating',
                   'rainstorm', 'pen', 'dirt', 'puzzling', 'spade', 'boundary', 'frequent',
                   'ethereal', 'crime', 'ill', 'trip', 'turn', 'foregoing', 'tricky', 'young',
                   'knot', 'cumbersome', 'trust', 'vigorous', 'frame', 'houses', 'yummy',
                   'steep', 'deserve', 'suggest', 'face', 'discovery', 'disastrous',
                   'advertisement', 'terrify', 'rebel', 'sneaky', 'heavy', 'appreciate',
                   'billowy', 'argument', 'queen', 'three', 'historical', 'system', 'wobble',
                   'assorted', 'pancake', 'ice', 'week', 'dull', 'happy', 'beef', 'secret',
                   'remain', 'plant', 'acoustic', 'rightful', 'yielding', 'kettle', 'fact',
                   'nondescript', 'half', 'camp', 'tangible', 'agree', 'troubled', 'hang',
                   'magic', 'regret', 'teeth', 'square', 'resonant', 'bloody', 'doctor',
                   'thinkable', 'venomous', 'park', 'connect', 'amount', 'porter', 'angle',
                   'flock', 'wanting', 'concerned', 'concentrate', 'floor', 'tickle',
                   'defeated', 'word', 'wash', 'harmonious', 'abaft', 'sudden', 'creature',
                   'graceful', 'smell', 'nostalgic', 'hope', 'share', 'disillusioned', 'cough',
                   'poison', 'scrub', 'truck', 'different', 'tender', 'trick', 'minute',
                   'noiseless', 'tacit', 'card', 'rhetorical', 'roof', 'letters', 'windy',
                   'rejoice', 'prick', 'promise', 'force', 'uncle', 'wild', 'plant', 'belief',
                   'complete', 'profuse', 'kiss', 'valuable', 'rat', 'soup', 'addition',
                   'cloth', 'unsightly', 'balance', 'sister', 'ball', 'coast', 'shock', 'fat',
                   'include', 'tenuous', 'interfere', 'start', 'unwritten', 'parallel',
                   'stimulating', 'farm', 'expansion', 'calculate', 'point', 'spiky',
                   'unbecoming', 'zephyr', 'useful', 'humdrum', 'heap', 'ubiquitous', 'curve',
                   'groovy', 'bright', 'quizzical', 'wide-eyed', 'land', 'twist',
                   'dysfunctional', 'birds', 'colorful', 'weak', 'upbeat', 'equable', 'reduce',
                   'plants', 'plan', 'meek', 'limit', 'baseball', 'few', 'plastic', 'careless',
                   'food', 'introduce', 'dizzy', 'magical', 'mice', 'scarce', 'stitch',
                   'grandmother', 'confuse', 'phone', 'ludicrous', 'arrest', 'coach', 'damp',
                   'toy', 'aware', 'amuse', 'sneeze', 'page', 'squeeze', 'rain', 'double',
                   'superb', 'educated', 'songs', 'dance', 'electric', 'murky', 'silver',
                   'play', 'leg', 'advise', 'sail', 'adamant', 'lip', 'useless', 'wail',
                   'axiomatic', 'maddening', 'fireman', 'seal', 'drop', 'stereotyped', 'step',
                   'slimy', 'dime', 'salt', 'mighty', 'vagabond', 'fortunate', 'mysterious',
                   'rhythm', 'swanky', 'barbarous', 'great', 'grubby', 'peel', 'ripe', 'best',
                   'quilt', 'note', 'burn', 'flat', 'table', 'wiggly', 'furniture', 'dinner',
                   'simple', 'theory', 'flowery', 'wry', 'cows', 'mouth', 'broken', 'street',
                   'plough', 'hate', 'threatening', 'hesitant', 'rifle', 'toothsome',
                   'bedroom', 'pricey', 'insurance', 'frail', 'teeny-tiny', 'recognise',
                   'deliver', 'tremble', 'loose', 'blue-eyed', 'perform', 'badge', 'six',
                   'fearful', 'calendar', 'amusing', 'substantial', 'damage', 'scandalous',
                   'cave', 'unpack', 'account', 'order', 'fang', 'tense', 'afraid', 'repeat',
                   'flow', 'overwrought', 'bizarre', 'preserve', 'cannon', 'placid', 'meddle',
                   'noisy', 'form', 'versed', 'weather', 'longing', 'fish', 'tasteful',
                   'destroy', 'coal', 'sail', 'highfalutin', 'ban', 'cent', 'plain', 'lean',
                   'vivacious', 'use', 'tiger', 'oatmeal', 'cut', 'fool', 'thing',
                   'connection', 'form', 'fence', 'greasy']

    name_suffix = ['knee', 'airport', 'throne', 'trick', 'sugar', 'swing',
                   'apparatus', 'beds', 'tongue', 'anger', 'balance', 'arch',
                   'wealth', 'flavor', 'gun', 'wheel', 'silver', 'wool', 'jar',
                   'book', 'plastic', 'grandfather', 'house', 'rain', 'purpose'
                   , 'year', 'letter', 'account', 'bushes',
                   'use', 'egg', 'son', 'pets', 'wrench', 'mind', 'mom', 'pen',
                   'hand', 'stranger',
                   'crowd', 'copper', 'bucket', 'shock', 'rate', 'rat', 'amount',
                   'station', 'condition', 'trail', 'border', 'distribution',
                   'arm', 'protest', 'song', 'title', 'mass', 'shade',
                   'baseball', 'animal', 'income', 'spring',
                   'eggnog', 'government', 'behavior', 'canvas', 'dust',
                   'error', 'substance', 'flag', 'bait', 'cave', 'detail',
                   'representative',
                   'legs', 'grape', 'guitar', 'produce', 'education', 'tub', 'blow',
                   'grandmother', 'mouth', 'bath', 'mountain', 'person', 'look', 'car',
                   'cherry', 'slave', 'slip', 'box', 'cakes', 'haircut', 'writing',
                   'spark', 'building', 'noise', 'bed', 'sister', 'stomach']

    tavern_name = 'The '
    tavern_name += random.choice(name_prefix)
    tavern_name += ' ' + random.choice(name_suffix)
    print(tavern_name)

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

    # generateStore(selectedStore)
    tavern_generator()
    print(generatedStore)
