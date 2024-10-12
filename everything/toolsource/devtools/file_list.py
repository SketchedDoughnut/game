'''
This is a tool used during build, which lists every file to exist.
It then dumps this data into a file, named file_list.json. This is important, because each file
in that json file is checked to make sure it exists. If any files do not exist, then that means the install went wrong.
Therefore, it is most important to call on this before releasing a build!
--------------------------------------------------------------------------------------------------------------------------------
This files adheres to the commenting guidelines :D
'''

# builtin modules
import os
import shutil
import time
import json

# set up lists resembling a variety of different paths
# file list contains the final product of paths
file_list = []
# blacklist contains all of the things that should be ignored
blacklist = [
    'everything\\main\\top\\container\\game_data\\src\\rhythm\\setup'
]
# direct filter includes things to be directly filtered out
direct_filter = [
    "__pycache__"
]
# this is the functoin that goes from a starting point,
# then iterates down. I won't explain in full how it works (because I don't
# really understand myself), but it lists every file that it should into a single
# outputted json.
def iter(path):
    files = []
    for filename in os.listdir(path):
        f = os.path.join(path, filename)
        if f not in blacklist:
            if os.path.isdir(f):
                files.extend(iter(f))
            elif os.path.isfile(f):
                files.append(f)
    return files

# this sets the filelist to the iter thing, which did what was described above
# and made a list of every filepath
file_list = iter('everything')
print('Indexed.')

# then this just cleans out stuff that did not get caught
# i dont know how it happens but it does tend to happen
for string in file_list:
    # print(string)
    for filtered in direct_filter:
        if filtered in string:
            print(f'removed {filtered} from {string}')
            file_list.remove(string)

# finally, the contents are dumped into the file, and all is done :D
f = open(r'everything\main\setup\file_list.json', 'w')
json.dump(file_list, f)
f.close()
print('Dumped.')