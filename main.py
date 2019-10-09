import json
import argparse


with open('words.json', 'r') as inFile:
    wordsDict = json.load(inFile)

# for adjective in wordsDict["adjectives"]:
#     print(adjective)
