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
WDIR = os.path.dirname(os.path.abspath(__file__))

# this is a function responsible for running the file lsit
def do_file_list():
    callpath = WDIR + '/everything/toolsource/devtools/file_list.py'
    subprocess.call(callpath)

# this is a function responsible for running the propagation
def do_propagate(): 
    callpath = WDIR + '/everything/toolsource/devtools/propagator.py'
    subprocess.call(callpath)


do_file_list()
do_propagate()