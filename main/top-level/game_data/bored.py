import random
import os

total = 0
div = 0
avg = 0

while True:
    os.system('clear')
    num = random.randint(1, 1000000)
    div += 1
    total += num
    avg = total / div
    print(f'avg: {avg}')
