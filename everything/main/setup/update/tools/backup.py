import shutil
import time
import os
import json
import requests

'''
flow
    - when invoked, an update has failed
    - load files from backup file (given mode top or game_data)
    - put them in respective locations
    - return an error message about potentially damaged files (offer full-redo re-install)
        - if yes, do full-redo
        - if no, warn them again but reset data.json
'''