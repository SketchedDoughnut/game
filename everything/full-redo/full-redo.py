'''
The goal of this file is to be used as a temporary file, positioned above main,
that will re-install ALL files. This is if fiesta.exe needs an update.
'''

# import builtin
import os
import shutil
import time
import json

# import installed
import requests

# SHIT WE DONT HAVE THE OTHER FILES RAHHHHHHH
# nvm I copied them
# import files
import update.download as f_download
import update.copy as f_copy
import update.extract as f_extract

print('Welcome to part 2/2 of the update.')
print('The update will continue when you authorize it.')
input('Enter anything to continue: ')
print('---------------')
'''
flow

    - establish all variables and paths
    - clean up any previous tmp (redundancy)
    - delete previous game_name
    - download
    - extract (in same dir, /tmp)
    - copy "game_name" and put it where the previous one was
'''

print('Update: Setting up variables...')

#############################################################################
#############################################################################
#############################################################################

# FOR PYTHON
# wDir, folder above this (full-redo)
wDir = os.path.dirname(os.path.abspath(__file__))
 # a directory above full-redo
high_wDir = os.path.dirname(wDir)

# FOR COMPILE
# wDir, folder above this (full-redo)
wDir = os.path.dirname(wDir)
high_wDir = os.path.dirname(high_wDir) # changed from wDir to high_wDir

# commit label, the random crap (in this case we ignore the bounds since we know we are installing full)
commit_label = requests.get("https://api.github.com/repos/SketchedDoughnut/development/releases/latest")
commit_label = commit_label.json()
commit_label = str(commit_label['body'])
commit_label = commit_label.split()
commit_label = commit_label[0]

# url for install
repo_url = "https://api.github.com/repos/SketchedDoughnut/development/releases/latest"

# tmp directory
tmp_path = f'{wDir}/tmp' # changed from wDir to high_wDir

# zip directory for install
zip_path = f'{tmp_path}/latest-release.zip'

# extract path for install
extract_path = f"{tmp_path}/SketchedDoughnut-development-{commit_label}"

# everything path
everything_path = f'{high_wDir}/everything'

# copy paths (source, destination) for install
copy_source = zip_path
copy_destination = everything_path

# edit path
# variable to edit the data.json of the installed installer to: "shortcut": true
# edit setup installer file

esif = f'{everything_path}/main/setup/data.json' # added main
vsif = f'{everything_path}/main/top/container/version.json' # added main

print(wDir)
print(high_wDir)
print(commit_label)
print(repo_url)
print(tmp_path)
print(zip_path)
print(extract_path)
print(everything_path)
print(copy_source)
print(copy_destination)
print(esif)
print(vsif)
#############################################################################
#############################################################################
#############################################################################

def delay():
    time.sleep(0.25)

print('Update: Deleting previous tmp...')
try:
    shutil.rmtree(tmp_path)
except:
    print('Update: No prior tmp')
print('Update: Deleting previous everything...')
try:
    shutil.rmtree(everything_path)
except:
    print('Update: No prior everything')
print('Update: Creating new tmp...')
os.mkdir(tmp_path)
print('Update: Downloading .zip...')
f_download.download_latest_release(repo_url, tmp_path)
print('Update: Extracting files...')
f_extract.extract(zip_path, tmp_path)
print('Update: Copying files...')
f_copy.copy(extract_path, everything_path)
print('Update: Reaching into data.json...')
f = open(esif, 'r')
td = json.load(f)
f.close()
td['shortcut'] = True
print('Update: Dumping into data.json...')
f = open(esif, 'w')
json.dump(td, f)
f.close()
print('Update: Reaching into version.json...')
print('Update: Dumping into version.json...')
f = open(vsif, 'w')
json.dump(str(commit_label))
print('Update: Cleaning up tmp...')
shutil.rmtree(tmp_path)