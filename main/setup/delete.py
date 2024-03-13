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
    temp = open('data.json', 'r')

# - for codespace
else:
    temp = open('main/setup/data.json', 'r')

delete_path = json.load(temp)
delete_path = delete_path["remove_path"]
temp.close()
print('---------------')
print(f'Delete: Un-installing game from the following directory: {delete_path}')
time.sleep(0.025)

# get path from delete.json
print('Delete: Acquiring JSON path...')
time.sleep(0.025)

# for run
if rules['env'] == 'run':
    read_file = open('data.json', 'r')

# - for codespace
else:
    read_file = open('main/setup/data.json', 'r')

path = json.load(read_file)
del_path = path["remove_path"]
shrt_path = path['abs_shortcut']

if ('game_name' in del_path) == False:
    print(f'No game name found ({del_path}). exiting in 5s...')
    time.sleep(5)
    exit()

read_file.close()
print(f'Delete: Directory path: {del_path}/')
print(f'Delete: Shortcut path: {shrt_path}')
time.sleep(0.025)

# deleting folder
print('Delete: deleting directory...')
try:
    shutil.rmtree(del_path)
    print('Delete: Directory gone.')

except Exception as e:
    print(f'Delete: Directory error: {e}')

time.sleep(0.025)

print('Delete: Deleting shortcut...')
time.sleep(0.025)

try:
    os.remove(shrt_path)
    print('Delete: Shortcut gone.')
    time.sleep(0.025)

except Exception as e:
    print(f'Delete: Shortcut error: {e}')

print('Delete: Clearing data...')
time.sleep(0.025)

# for run
if rules['env'] == 'run':
    write_file = open('data.json', 'w')

# - for codespace
else:
    write_file = open('main/setup/data.json', 'w')

path["remove_path"] = ""
path["abs_shortcut"] = ""
json.dump(path, write_file)
write_file.close()
exit()