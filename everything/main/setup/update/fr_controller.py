# builtins
import os
import shutil
import json
import time

# packages
import requests

# file imports
from .tools import backup as b
from .tools import download as d
from .tools import extract as ee
from .tools import copy as c
from .tools import verify as v



def update_handler_setup(
        setup_wDir,
        everything_path,
        mode
    ):

    '''
    flow for full re-install
    
        - deletes previous tmp folder in setup
        - creates new tmp folder
        - alerts that this installation requires user interaction
        - download .zip
        - extract .zip
        - copy "full-redo" into the directory ABOVE of main
        - get rid of tmp
        - reset data.json
        - provide further instructions on what to do
        done!
    '''

    # setup the vars provided here
    # commit label
    release_version = requests.get("https://api.github.com/repos/SketchedDoughnut/development/releases/latest")
    release_version = release_version.json()
    release_version = str(release_version['body'])
    release_version = release_version.split()
    release_version = release_version[0]

    # other vars
    ut2_wDir = os.path.dirname(os.path.dirname(os.path.dirname(setup_wDir)))
    zip_download_path = f"{setup_wDir}/tmp/latest_release.zip",
    ext_download_path = f"{setup_wDir}/tmp"
    copy_source = f"{ext_download_path}/SketchedDoughnut-development-{release_version}/everything/full-redo"
    repo_url = "https://api.github.com/repos/SketchedDoughnut/development/releases/latest"
    dump_location = f'{ut2_wDir}/full-redo'

    json_path = os.path.join(setup_wDir, 'file_list.json')
    v.verify_files(json_path, everything_path)

    
    if mode == 'full-setup':
        # FOR PYTHON
        print(ut2_wDir)

        # FOR COMPILE
        #os.path.dirname(ut2_wDir)

        # cancel if they want to
        print('Update: installing full')
        print('- This is a update that requires a re-installation of all game files.')
        print('  Nothing will be saved.')
        print('If you want to backup your files, copy the ENTIRE directory now.')
        print(f'The directory is: {ut2_wDir}/everything')
        if input('Continue? (y/n) ').lower() != 'y':
            print('---------------')
            print('Cancelling...')
            print('Update: Resetting data.json...')
            f = open(f'{setup_wDir}/data.json', 'r')
            td = json.load(f)
            f.close()
            td['bounds'] = 'x'
            td['update'] = False
            td['shortcut'] = True
            f = open(f'{setup_wDir}/data.json', 'w')
            json.dump(td, f)
            f.close()
            input('Enter anything to exit: ')
            exit()

        # clean tmp
        print('---------------')
        print('Update: Cleaning tmp...')
        try:
            shutil.rmtree(f'{setup_wDir}/tmp')
        except:
            print('Update: No prior tmp')

        # make tmp
        print('Update: Making tmp...')
        os.mkdir(f'{setup_wDir}/tmp')
        
        # delete previous full-redo
        print('Update: Cleaning full-redo...')
        try:
            shutil.rmtree(f'{ut2_wDir}/full-redo')
        except:
            print('Update: No prior full-redo')

        # download .zip
        print('Update: Downloading .zip...')
        d.download_latest_release(repo_url, zip_download_path)

        # extract files
        # https://www.geeksforgeeks.org/unzipping-files-in-python/
        print('Update: Extracting files...')
        time.sleep(1)
        ee.extract(zip_download_path, ext_download_path)
        
        # get commit label (teehee)
        print('Update: Getting commit label...')
        time.sleep(0.5)

        # copy full-redo folder ABOVE current installation main, so it is:
        # root: main, full-redo (in same dir)

        # copy files to new directory
        # https://pynative.com/python-copy-files-and-directories/
        print('Update: Copying control folder...')
        print(f'Update: Copying files to {dump_location}')
        c.copy(copy_source, dump_location)

        # clean up tmp
        print('Update: Cleaning up tmp...')
        try:
            shutil.rmtree(f'{setup_wDir}/tmp')
        except:
            print('Update: No tmp')

        # check install path
        print('Update: Checking install path...')
        if os.path.exists(f'{ut2_wDir}/full-redo'):
            pass
        else:
            print('!!! UPDATE ERROR: The installed directory does not exist. Cancelling.')
            input('Enter anything to exit: ')
            exit()

        # start second part of update
        print('---------------')
        print(f"""Update: Part 1/2 of update is done.
    This installer is incapable of finishing this update, as it will require deleting itself. 
    In order to finish this install, please go to --
    > {ut2_wDir}/full-redo/
    -- and run the file named "full-redo.exe". It will run you through the process to finish this update.""")
        print('---------------')
        input('Enter anything to exit: ')
        exit()