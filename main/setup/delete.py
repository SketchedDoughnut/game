import shutil
import os
import json
import time

# get path from delete.json
print('Delete: Acquiring JSON path')

# for codespace
# try:
    # file = open('delete.json', 'r')
# except:
    # try:
        # file = open('main/setup/delete.json', 'r')
    # except Exception as e:
        # print(f'error: {e}')
        # print('vsc handling: exiting')
        # time.sleep(5)
        # exit()

## for codespace
file = open('main/setup/delete.json', 'r')
             
# for run
#file = open('delete.json', 'r')

path = json.load(file)
path = path["remove_path"]
file.close()
print(f'Delete: JSON path: {path}/delete.json')

# deleting folder
print('Delete: deleting folder and everything within...')
shutil.rmtree(path)
print('Delete: Directory gone. Finishing...')
exit()