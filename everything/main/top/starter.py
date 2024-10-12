'''
This is the starter that is designed to redirect into whichever application
you intend on using. It presents options (TODO) and you select which to go to.
Simple little guy!
--------------------------------------------------------------------------------------------------------------------------------
This files adheres to the commenting guidelines :D
'''
# the code god has spited me :c

# builtin modules
import os
import subprocess

# get the working directory and path to next file
wDir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(wDir, 'container/index.py')

# call on the file, continuing the callstack
print('----------------------------')
print(path)
print('Starter redirecting to index file...')
print('----------------------------')
c1 = r'{patth}'.format(patth=path) # calling string
# os.system(f'python {path}')
# os.system(c1)
subprocess.run(f'python "{c1}"')