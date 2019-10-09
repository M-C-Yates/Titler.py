import argparse
import json
import random

with open('words.json', 'r') as inFile:
    words = json.load(inFile)

randAdjective = random.choice(words["adjectives"])
randNoun = random.choice(words["nouns"])
delimiter = " "

print(f"{randAdjective}{delimiter}{randNoun}")
