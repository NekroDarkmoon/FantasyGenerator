# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
#                               TAVERN GENERATOR
#
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Imports
import random
import npc_generator

# Variables
tavern = []


def tavern_generator():

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # TAVERN NAME

    name_prefix = ['faulty', 'wasteful', 'tacky', 'tart', 'voiceless',
                   'resolute', 'fierce', 'zany', 'hysterical', 'foolish',
                   'exclusive', 'full', 'boiling', 'great', 'painful',
                   'moldy', 'didactic', 'awesome', 'economic', 'better',
                   'even', 'tightfisted', 'feigned', 'roomy', 'capricious',
                   'inconclusive', 'solid', 'wretched', 'eight',
                   'draconian', 'fascinated', 'wide', 'acid', 'overt',
                   'eager', 'ruthless', 'spectacular', 'wild', 'public',
                   'separate', 'mindless', 'ossified', 'magnificent',
                   'flagrant', 'thick', 'ritzy', 'elfin', 'paltry',
                   'groovy', 'psychotic', 'fantastic', 'heavy', 'lame',
                   'halting', 'stereotyped', 'curious', 'aquatic',
                   'omniscient', 'elegant', 'bewildered', 'cute',
                   'unwritten', 'ill', 'cooing', 'grateful', 'assorted',
                   'absurd', 'parched', 'measly', 'damaging', 'upset',
                   'tense', 'phobic', 'fine', 'aggressive', 'extra-large',
                   'acrid', 'cowardly', 'breakable', 'alive', 'wide-eyed',
                   'brawny', 'mushy', 'holistic', 'pumped', 'bad', 'brash',
                   'round', 'languid', 'shallow', 'divergent', 'mellow',
                   'intelligent', 'whimsical', 'flawless', 'jealous',
                   'abundant', 'thinkable', 'remarkable', 'feeble', 'slutty',
                   'lusty', 'lavish']

    name_suffix = ['lamp', 'crowd', 'fly', 'spark', 'hair',
                   'purpose', 'flower', 'smash', 'voyage', 'paper',
                   'hospital', 'plants', 'division', 'force',
                   'quiver', 'acoustics', 'wax', 'jeans', 'laborer',
                   'control', 'apparatus', 'eyes', 'head', 'account',
                   'sheep', 'kiss', 'stomach', 'join', 'camp',
                   'bait', 'property', 'religion', 'pen', 'grain',
                   'whip', 'humor', 'dress', 'porter', 'badge',
                   'foot', 'spade', 'rainstorm', 'taste', 'mass',
                   'dust', 'relation', 'touch', 'sweater', 'bath',
                   'plane', 'chess', 'face', 'brick', 'low', 'step',
                   'snow', 'toys', 'van', 'vein', 'waves', 'sisters',
                   'horn', 'watch', 'zebra', 'cannon', 'riddle', 'board',
                   'honey', 'bit', 'corn', 'woman', 'legs', 'wash',
                   'angle', 'adjustment', 'pest', 'maid', 'dime', 'cake',
                   'trouble', 'cats', 'roof', 'slip', 'liquid',
                   'cover', 'back', 'wave', 'cave', 'grade',
                   'development', 'tramp', 'railway', 'chalk',
                   'stretch', 'pets', 'mitten', 'finger',
                   'health', 'bird', 'drain']

    tavern_name = 'The '
    tavern_name += random.choice(name_prefix)
    tavern_name += ' ' + random.choice(name_suffix)
    # TODO: delete debug
    print(tavern_name)
    tavern.append(tavern_name)

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # TAVERN'S TALE
    # TODO: Tavern's Tale
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # BARTENDER
    # TODO: The bartender
    bartender = [npc_generator.generateNPC('', '')]
    print(bartender)
    # TODO: Clientle
    # TODO: Accomodations
    # TODO: Food
    # TODO: Drinks


def main():
    tavern_generator()
    return tavern
