# the code god has spited me :c

import os

wDir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(wDir, 'game_data/index.py')

print('Starter redirecting to index file...')
print('----------------------------')
os.system(f'python {path}')