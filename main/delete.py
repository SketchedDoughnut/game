import shutil
import os
import json
import time

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

#################################################################

'''
{
    "remove_path": ""
}
'''

# get path from delete.json
print('Delete: Acquiring JSON path')

# - for codespace
#read_file = open('main/setup.json', 'r')
             
# for run
read_file = open('setup.json', 'r')

path = json.load(read_file)
path["remove_path"]

if ('main' in path["remove_path"]) == False:
    print(f'No main found ({path["remove_path"]}). exiting in 5s...')
    time.sleep(5)
    exit()

read_file.close()
print(f'Delete: JSON path: {path["remove_path"]}/')

# deleting folder
print('Delete: deleting folder and everything within...')
shutil.rmtree(path["remove_path"])

time.sleep(0.5)

print('Delete; deleting shortcut...')
os.remove(path["abs_shortcut_path"])

print('Delete: Directory gone. Emptying data file.')

# - for codespace
#write_file = open('main/setup.json', 'w')
             
# for run
write_file = open('setup.json', 'w')

path["remove_path"] = ""
path["abs_shortcut_path"] = ""
json.dump(path, write_file)
write_file.close()
exit()