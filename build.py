'''
This file is ran to make the building process more efficient.
Yay!
--------------------------------------------------------------------------------------------------------------------------------
This files adheres to the commenting guidelines :D
'''

# builtin modules
import os

# external modules
from rich import print

# get the current working directory for future use
PYTHON_PATH = r'D:/VScode/SDA/game/.venv/Scripts/python.exe'
WDIR = os.path.dirname(os.path.abspath(__file__))

# this is a function responsible for running the file lsit
def do_file_list(): 
    print('[purple] Listing all files...')
    os.system(f"{PYTHON_PATH} {WDIR + r'/everything/toolsource/devtools/file_list.py'}")

# this is a function responsible for running the propagation
def do_propagate(): 
    print('[purple] Propagating files...')
    os.system(f"{PYTHON_PATH} {WDIR + r'/everything/toolsource/devtools/propagator.py'}")

# this is a function responsible for freezing pip
def do_pip_freeze(): 
    print('[purple] Generating requirements.txt...')
    os.system('pip freeze > requirements.txt')

# this is a function responsible for generating pipfile.lock
def do_gen_pipfile():
    print('[purple] Generating Pipfile.lock...')
    os.system('pipenv lock')

do_pip_freeze() # generates requirement.txt in root
do_gen_pipfile() # generates pipfile.lock in root
do_propagate() # propagates crash handler / elevator templates (NOTE: BEFORE COMPILING)
# do_file_list() # lists all files existing (NOTE: DO AFTER COMPILING)