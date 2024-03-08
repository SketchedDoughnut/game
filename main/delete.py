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
read_file = open('main/delete.json', 'r')
             
# for run
#read_file = open('delete.json', 'r')

path = json.load(read_file)
path_content = path["remove_path"]

if ('main' in path_content) == False:
    print(f'No main found ({path_content}). exiting in 5s...')
    time.sleep(5)
    exit()

read_file.close()
print(f'Delete: JSON path: {path_content}/')

# deleting folder
print('Delete: deleting folder and everything within...')
shutil.rmtree(path_content)

print('Delete: Directory gone. Emptying data file.')

# - for codespace
write_file = open('main/delete.json', 'w')
             
# for run
#write_file = open('delete.json', 'w')

path["remove_path"] = ""
json.dump(path, write_file)
write_file.close()
exit()