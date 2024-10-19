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

# this is a function responsible for running the file lsit
def do_file_list(): 
    path = WDIR + r'/everything/toolsource/devtools/file_list.py'
    print('[purple]-------------------------\nListing all files...')
    time.sleep(0.25)
    subprocess.call(f'"{PYTHON_PATH}" "{path}"')

# this is a function responsible for running the propagation
def do_propagate(): 
    path = WDIR + r'/everything/toolsource/devtools/propagator.py'
    print('[purple]-------------------------\nPropagating files...')
    time.sleep(0.25)
    subprocess.call(f'"{PYTHON_PATH}" "{path}"')

# this is a function responsible for freezing pip
def do_pip_freeze(): 
    print('[purple]-------------------------\nGenerating requirements.txt...')
    time.sleep(0.25)
    os.system('pip freeze > requirements.txt')

# this is a function responsible for generating pipfile.lock
def do_gen_pipfile():
    print('[purple]-------------------------\nGenerating Pipfile.lock...')
    time.sleep(0.25)
    os.system('pipenv lock')

do_pip_freeze() # generates requirement.txt in root
check_time()
do_gen_pipfile() # generates pipfile.lock in root
check_time()
do_propagate() # propagates crash handler / elevator templates (NOTE: BEFORE COMPILING)
check_time()
# do_file_list() # lists all files existing (NOTE: DO AFTER COMPILING)

# print the final run time
print(f'[green]Total build time: {time.time() - START} seconds')