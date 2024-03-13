import shutil
import os
import json
import time

#################################################################
# - for codespace
rules = open('main/setup/config.json', 'r')

# for run
#rules = open('config.json', 'r')

rules = json.load(rules)

# for run
if rules['env'] == 'run':
    temp = open('delete.json', 'r')

# - for codespace
else:
    temp = open('main/setup/delete.json', 'r')

delete_path = json.load(temp)
delete_path = delete_path["remove_path"]
temp.close()
print('---------------')
print(f'Un-installing game from the following directory: {delete_path}')

# get path from delete.json
print('Delete: Acquiring JSON path')

# for run
if rules['env'] == 'run':
    read_file = open('delete.json', 'r')

# - for codespace
else:
    read_file = open('main/setup/delete.json', 'r')

path = json.load(read_file)
path_content = path["remove_path"]

if ('game_name' in path_content) == False:
    print(f'No game name found ({path_content}). exiting in 5s...')
    time.sleep(5)
    exit()

read_file.close()
print(f'Delete: JSON path: {path_content}/')

# deleting folder
print('Delete: deleting folder and everything within...')
shutil.rmtree(path_content)

print('Delete: Directory gone. Emptying data file.')

# for run
if rules['env'] == 'run':
    write_file = open('delete.json', 'w')

# - for codespace
else:
    write_file = open('main/setup/delete.json', 'w')

path["remove_path"] = ""
json.dump(path, write_file)
write_file.close()
exit()