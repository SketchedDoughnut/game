'''
This is the FOMX system, which stands for:
File
Overwriting
Management
X-press

Its job is to apply patches that are not released as full updates. This is helpful because we want to keep 
full releases from being spammed, and instead we can spam releases on the patch agent (which isn't as messy for the user
because they will not typically be accessing the patches directly). 

FOMX is capable of a variety of things, such as these (in order of execution):
- detecting if a new patch is out
- showing patch info
- applying patch
    - pre cleanup
    - running commands from a file
    - verifying files
    - copying over files from patch
    - propogating elevator / crash handler if necessary
    - post cleanup

--------------------------------------------------------------------------------------------------------------------------------
This files adheres to the commenting guidelines :D
'''

# builtin modules
import os
import shutil
import time
import json
import sys

# external modules
import requests

# file imports
import tools

# all constants
# code to establish other constants is also done here
# to keep it organized :D
URL = 'https://api.github.com/repos/SketchedDoughnut/SDA-FOMX/releases/latest'
WDIR = os.path.dirname(os.path.abspath(__file__))
ABOVE_EVERYTHING_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(WDIR))))
# loading the current label from the local file
# and assigning it to a variable for later use
f = open(os.path.join(WDIR, 'version.json'))
CURRENT_LABEL = str(json.load(f))
f.close()
# get the label from the latest github release
# and also the body of the latest release
request_data = requests.get(URL).json()
body_data = str(request_data['body'])
split_data = body_data.split()
LATEST_LABEL = split_data[0]
split_data.remove(id)
BODY = ''
for word in split_data:
    BODY += word
    BODY += " "
TMP_PATH = os.path.join(WDIR, 'tmp') # for the tmp folder
ZIP_PATH = f'{TMP_PATH}/latest_release.zip' # for downloading the .zip online
COPY_LOCATION = f'{TMP_PATH}/SketchedDoughnut-SDA-FOMX-{LATEST_LABEL}/data' # for copying data
CMD_PATH = os.path.join(COPY_LOCATION, 'necessary/cmd.txt') # for locating command file
BOUNDS_PATH = f'{COPY_LOCATION}/necessary/bounds.json'# for accessing the instructions file (bounds)

# propagation data
# this contains the state on whether or not the FOMX
# system should propogate the crash handler, or propogate
# the elevator system
propagate_data = (False, False)

# start printing some information about what is going on
print(f"""---------------
FOMX: DATA
    - current commit label: {CURRENT_LABEL}
    - commit label of newest release: {LATEST_LABEL}
FOMX: comparing versions...""")

# compare the stored version to the online version
# if they are not equal, ask the user what they want to do
if CURRENT_LABEL != LATEST_LABEL:
    print('---------------\nFOMX: versions do not match.')

    # if they do want to see the info, display it
    # otherwise, skip
    if input('FOMX: do you want to see the info for this update? (y/n): ').lower() == 'y':
        print(f"""---------------
Info:
- {BODY}
---------------""")
    else: print('FOMX: skipping...\n---------------')

    # if they want to download the update, proceed
    # otherwise, exit (startup will continue on)
    if input('Download this update? This is highly recommended (y/n): ').lower() == 'y': pass
    else:
        print('FOMX: exiting...')
        time.sleep(1)
        sys.exit()
    print('---------------')

# if the labels match, then exit
# (startup will continue on)
else:
    print('FOMX: versions match. Continuing to launch.')
    time.sleep(1)
    sys.exit()

# try to clean up any previous files, such as any previous tmp folders
# this is redundancy because FOMX should clean up tmp
# however in the event it does not, this should fix that
print('FOMX: attempting to delete previous tmp...')
try:
    shutil.rmtree(TMP_PATH)
    print('FOMX: previous tmp deleted')
except: pass

# create a new tmp folder that will be deleted
# after done
print('FOMX: creating tmp...')
os.mkdir(TMP_PATH)

# download the .zip from online
# and save it to ZIP_PATH
print('FOMX: downloading .zip...')
tools.download_latest_release(URL, ZIP_PATH)
time.sleep(1) # ???

# extract the stuff from inside the .zip
# and put it into the tmp folder
print('FOMX: extracting...')
tools.extract(ZIP_PATH, TMP_PATH)

# read the bounds file, which tells FOMX what to do
# this includes features outlined at the top of the file
# such as executing remote commands
print('FOMX: reading bounds file...')
f = open(BOUNDS_PATH, 'r')
bounds = json.load(f)
f.close()
time.sleep(1)

# print the description of what files bounds
# will be effecting.
# also print the file paths (or names?) themselves
print(f"""FOMX: bounds description:
- {bounds['description']}
FOMX: files affected:
- {bounds['file_details']}""")

# i can not explain to you what happens here.
# i have tried cleaning it up, rewriting it, making it better
# in any and every way. I refuse to touch it, it works fine
# don't worry about it
print('FOMX: formatting data list...')
formatted_list = []
for path, file in zip(bounds['file_paths'], bounds['file_details']):
    formatted_list.append([file[1], os.path.join(COPY_LOCATION, file[0]), os.path.join(os.path.join(ABOVE_EVERYTHING_DIR, path), file[0]), file[0]])

# check for if the CMD file option is toggled
# if it is, then check for it and execute the commands it says
# this system works. source? trust me
print('---------------\nFOMX: Checking for CMD file...')
if bounds['cmd_exist'] == True:
    print('FOMX: CMD file found, running CMD...')
    propagate_data = tools.read_commands(ABOVE_EVERYTHING_DIR, CMD_PATH)

# verifying if all of the desination file exists
# if they did not exist before this patch, then the CMD reader comes in
# that is because it can make that file exist, which means it will then pass verification
# woah thats amazing!
print('---------------')
print('FOMX: verifying files exist...')
for data in formatted_list:
    print('- verifying:', data)
    
    # if destination does not exist, exit
    if not os.path.exists(data[1]):
        print('-- source does not exist.')
        input('FOMX: Enter anything to exit process: ')
        time.sleep(1)
        sys.exit()
print('FOMX: all files exist.')

# copy over the code from the extracted files over to the destination
# similar to the above formatting of the list, i have no idea how this works
# it is black magic, from what I am aware
# don't touch it, works fine- mhm!
print('---------------\nFOMX: Copying over code...')
time.sleep(1)
for file in formatted_list:
    # find out the mode
    # i believe this can either be json, normal, or binary
    # the mode dictates how the file is opened (normal or as binary)
    # or if its treated via json.load or json.dump
    mode = file[0]
    # get the source
    # this should be the path to the source file, I believe?
    source = file[1]
    # get the desination
    # this should be where to copy the contents of the source file to?
    dest = file[2]
    # set the modes for accessing files
    # op = open argument (so read or read binary)
    # wr = write argument (so write or write binary)
    # these depend on the set mode for that file
    if mode == 'normal' or mode == 'json':
        op = 'r'
        wr = 'w'
    elif mode == 'binary':
        op = 'rb'
        wr = 'wb'

    # read / write file contents
    # this applies to anything but json files
    # because they use a different method
    if mode != 'json':
        f = open(source, op)
        content = f.read()
        f.close()
        f = open(dest, wr)
        f.write(content)
        f.close()
        print(f'- wrote content from "{source}" to "{dest}"')

    # read / write file contents (but for json!)
    # this is the same as above, but works with json instead
    # just slightly modified
    elif mode == 'json':
        f = open(source, op)
        content = json.load(f)
        f.close()
        f = open(dest, wr)
        json.dump(content, f)
        f.close()
        print(f'- wrote content from "{source}" to "{dest}"')
    
# if the propogater is enabled, then this runs
# it goes through propogate_data, and sees what needs to be propogated
# I am not sure why this is in a for loop
# or why any of this is like this
# TODO: fix this code to not be bad, why is it in a for loop?
print('---------------')
for elem in propagate_data:
    if elem == True:
        print('FOMX: running propagator, crash, elevator flags are:', propagate_data)
        tools.propagate_master(ABOVE_EVERYTHING_DIR, propagate_data[0], propagate_data[1])
        print('---------------')
        break # ran propogator, dont want to run again

# after everything done, attempt to clean up the tmp folder
# if this fails, its fine as it will be cleaned up next time
# a patch needs to be applied
print('FOMX: cleaning up tmp...')
time.sleep(1)
try: shutil.rmtree(TMP_PATH)
except: pass

# update the local version so that it matches
# this is so the same patches dont get applied again
print('FOMX: updating local version...')
f = open(os.path.join(WDIR, 'version.json'), 'w')
json.dump(LATEST_LABEL, f)
f.close()
time.sleep(1)

# done!
# file exits afer user input
print('---------------')
print('FOMX process is done, Enter anything to continue on to launch: ')
input('--> ')
sys.exit()