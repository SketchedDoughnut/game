import random
import json

print('Generating random numbers...')
# Generate a list of 350 numbers ranging from 0 to 3
numbers = [random.randint(0, 2) for _ in range(10740)]

print('Dumping...')
f = open("main\\top\game_data\src\\rhythm\setup\\nums\gen.json", 'w')
json.dump(numbers, f)
f.close()
#print(numbers)
print('Done.')