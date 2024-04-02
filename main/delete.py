import shutil
import os
import json
import time
'''
## - for codespace
# - for codespace
## for run
# for run
'''
#################################################################

# get path from delete.json
print('Delete: Acquiring JSON path')

## - for codespace
#read_file = open('main/setup.json', 'r')
             
## for run
read_file = open('setup.json', 'r')

path = json.load(read_file)
read_file.close()

rov = path['environment'] == 'run'

# checking if main in file path
if ('main' in path["remove_path"]) == False:
    print(f'Nn main found ({path["remove_path"]})... skipping')

# run if main is present in file path
else:
    print(f'Delete: JSON path: {path["remove_path"]}/')

    # deleting folder
    print('Delete: deleting folder and everything within...')
    shutil.rmtree(path["remove_path"])

# safety delay
time.sleep(0.5)

# deleting shortcut
print('Delete: deleting shortcut...')
try:
    os.remove(path["abs_shortcut_path"])
except Exception as e:
    print(f'Delete: Shortcut delete error: {e}')

# finished delete
print('Delete: Directory gone. Emptying data file.')

# for run
if rov:
    write_file = open('setup.json', 'w')

# - for codespace
else:
    write_file = open('main/setup.json', 'w')

# emptying both values with paths to files that have been now deleted
path["remove_path"] = ""
path["abs_shortcut_path"] = ""
json.dump(path, write_file)
write_file.close()
exit()