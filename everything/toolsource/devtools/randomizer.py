'''
This file generates randomized folder names for storage and whatnot.
It can also be used to generate labels and whatnot for other things.
General use! Yay!
--------------------------------------------------------------------------------------------------------------------------------
This files adheres to the commenting guidelines :D
'''

# builtin modules
import random

# establish strings containing characters
# that can be used for randomized labels
lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = lowercase.upper()

def genLabel(length: int = 10) -> str:
    label = ''
    for _ in range(length):
        zoneSelection = random.randint(0, 150)
        if zoneSelection <= 50: label += uppercase[random.randint(0, len(uppercase) - 1)]
        elif zoneSelection >= 51 and zoneSelection <= 100: label += lowercase[random.randint(0, len(lowercase) - 1)]
        elif zoneSelection > 100 and zoneSelection <= 150: label += str(random.randint(0, 9))
    return label

print(genLabel())