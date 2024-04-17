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

#############################################################################
#############################################################################
#############################################################################

# FOR PYTHON
wDir = os.path.dirname(os.path.abspath(__file__))

# FOR COMPILE
#wDir = os.path.dirname(wDir)

# commit label, the random crap (in this case we ignore the bounds since we know we are installing full)
commit_label = requests.get("https://api.github.com/repos/SketchedDoughnut/development/releases/latest")
commit_label = commit_label.json()
commit_label = str(commit_label['body'])
commit_label = commit_label.split()
commit_label = commit_label[0]

# url for install
repo_url = "https://api.github.com/repos/SketchedDoughnut/development/releases/latest"

# tmp directory
tmp_path = f'{wDir}/tmp'

# zip directory for install
zip_path = f'{tmp_path}/latest-release.zip'

# extract path for install
extract_path = tmp_path

# copy path (source, destination) for install
copy_source = 
#############################################################################
#############################################################################
#############################################################################