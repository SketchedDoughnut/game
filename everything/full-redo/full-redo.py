'''
The goal of this file is to be used as a temporary file, positioned above main,
that will re-install ALL files. This is if fiesta.exe needs an update.
'''

# imports
import os
import shutil
import requests

# SHIT WE DONT HAVE THE OTHER FILES RAHHHHHHH
# nvm I copied them
# file imports
import update.download as f_download
import update.copy as f_copy
import update.extract as f_extract

print('Welcome to part 2/2 of the update.')
print('The update will continue when you authorize it.')
input('Enter anything to continue: ')
print('---------------')
'''
flow

    - clean up any previous tmp (redundancy)
    - delete previous game_name
    - establish all variables and paths
    - download
    - extract (in same dir, /tmp)
    - copy "game_name" and put it where the previous one was
'''

print('Update: Setting up variables...')

# FOR COMPILE
wDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# FOR PYTHON
#wDir = os.path.dirname(os.path.abspath(__file__))

commit_label = requests.get("https://api.github.com/repos/SketchedDoughnut/development/releases/latest")
commit_label = commit_label.json()
commit_label = str(commit_label['body'])
commit_label = commit_label.split()
commit_label = commit_label[0]