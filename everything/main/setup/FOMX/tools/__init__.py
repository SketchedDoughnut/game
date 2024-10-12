'''
This just extends everything from the individual files into the tools folder.
It is not necessarily needed, but it makes it easier to code as these modules are recognized
by VSCode when writing more Python code.
--------------------------------------------------------------------------------------------------------------------------------
This files adheres to the commenting guidelines :D
'''

from .cmd_reader import read_commands
from .download import download_latest_release
from .extracter import extract
from .propagator import propagate_master