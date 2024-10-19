'''
This file is ran to make the building process more efficient.
Yay!
--------------------------------------------------------------------------------------------------------------------------------
This files adheres to the commenting guidelines :D
'''

# builtin modules
import subprocess
import os
import time

# external modules
from rich import print

# get the current working directory for future use
# as well as establish the Python interpreter path
# just in case
WDIR = os.path.dirname(os.path.abspath(__file__))
PYTHON_PATH = r'{}\\.venv\\Scripts\\python.exe'.format(WDIR)
PROPAGATE_CALLPATH = WDIR + r'/everything/toolsource/devtools/propagator.py'
FILELIST_CALLPATH = WDIR + r'/everything/toolsource/devtools/file_list.py'

# define a start time to time how long build takes
# and how long each process takes
START = time.time()
previous = time.time()

# this is a function that checks how long a time has passed
# then changes the counters
def check_time(doPrint: bool = True):
    global previous
    now = time.time()
    dif = now - previous
    if doPrint:
        print(f'[yellow]Time taken: {round(dif, 3)} seconds')
    previous = now

# generates requirement.txt in root
# which contains all of the dependencies
print('[purple]-------------------------\nGenerating requirements.txt...')
time.sleep(0.25)
os.system('pip freeze > requirements.txt')
check_time()

# generates Pipfile.lock in root
# and also Pipfile if it does not exist
# also contains dependencies but... different?
print('[purple]-------------------------\nGenerating Pipfile.lock...')
time.sleep(0.25)
os.system('pipenv lock')
check_time()

# propagates all template files (NOTE: BEFORE COMPILING)
print('[purple]-------------------------\nPropagating files...')
time.sleep(0.25)
subprocess.call(f'"{PYTHON_PATH}" "{PROPAGATE_CALLPATH}"')
check_time()

# lists all files existing (NOTE: DO AFTER COMPILING)
# print('[purple]-------------------------\nListing all files...')
# time.sleep(0.25)
# subprocess.call(f'"{PYTHON_PATH}" "{FILELIST_CALLPATH}"')
# check_time()

# print the final run time
build_time = time.time() - START
print(f'[green]Total build time: {round(build_time, 3)} seconds')