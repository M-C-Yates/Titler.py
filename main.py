import argparse
import json
import random

parser = argparse.ArgumentParser(description='a name generator')

parser.add_argument("-d", default='\u0020', type=str,
                    help="string delimiter, default: '\u0020', options: '\u0020', '\u2010', '\u005f'")
args = parser.parse_args()

with open('words.json', 'r') as inFile:
    words = json.load(inFile)
delimiter = args.d
amount = 5

for x in range(1, amount + 1):
    randAdjective = random.choice(words["adjectives"])
    randNoun = random.choice(words["nouns"])
    print(f"{randAdjective}{delimiter}{randNoun} {x}")
