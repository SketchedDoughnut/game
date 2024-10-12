'''
This file is ran to make the building process more efficient.
Yay!
--------------------------------------------------------------------------------------------------------------------------------
This files adheres to the commenting guidelines :D
'''

# builtin modules
import os
import subprocess

WDIR = os.path.dirname(os.path.abspath(__file__))

# this is a function responsible for running the file lsit
def do_file_list():
    subprocess.call(os.path.join(WDIR, '/everything/toolsource/devtools/file_list.py'))

# this is a function responsible for running the propagation
def do_propagate(): 
    subprocess.call(os.path.join(WDIR, '/everything/toolsource/devtools/propagator.py'))


do_file_list()
do_propagate()