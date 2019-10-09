import argparse
import json
import random

parser = argparse.ArgumentParser(description='a name generator')

parser.add_argument("-d", default='\u0020',
                    choices=["\u0020", "\u2010", "\u005f"],
                    help="string delimiter, default: '\u0020'",
                    required=False, type=str,)

parser.add_argument(
    '-a', default=1, help="amount of names to generate. default: 1", required=False, type=int)


args = parser.parse_args()

with open('words.json', 'r') as inFile:
    words = json.load(inFile)
delimiter = args.d
amount = args.a

for x in range(1, amount + 1):
    randAdjective = random.choice(words["adjectives"])
    randNoun = random.choice(words["nouns"])
    print(f"{randAdjective}{delimiter}{randNoun}")
