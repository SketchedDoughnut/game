'''
This file is ran to make the building process more efficient.
Yay!
--------------------------------------------------------------------------------------------------------------------------------
This files adheres to the commenting guidelines :D
'''

# builtin modules
import os
import subprocess

# get the current working directory for future use
PYTHON_PATH = r'D:/VScode/SDA/game/.venv/Scripts/'
WDIR = os.path.dirname(os.path.abspath(__file__))

# this is a function responsible for running the file lsit
def do_file_list():
    callpath = WDIR + r'/everything/toolsource/devtools/file_list.py'
    subprocess.call(f"python {callpath}", cwd=PYTHON_PATH)

# this is a function responsible for running the propagation
def do_propagate(): 
    callpath = WDIR + r'/everything/toolsource/devtools/propagator.py'
    subprocess.call(f"python {callpath}", cwd=PYTHON_PATH)


do_file_list()
do_propagate()