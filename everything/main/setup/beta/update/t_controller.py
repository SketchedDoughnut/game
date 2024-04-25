import os
import shutil
import json
import time

# packages
import requests
 
# file imports
import update.tools.download as d
import update.tools.extract as ee
import update.tools.copy as c
import update.tools.verify as v


def update_handler(main_wDir, setup_wDir):

    # setup the vars provided here
    mode = 'top',
    zip_download_path = f"{setup_wDir}/tmp/latest_release.zip",
    ext_download_path = f"{setup_wDir}/tmp",
    copy_location = f'{main_wDir}/top',
    json_path = os.path.join(setup_wDir, 'file_list.json'),
    everything_path = os.path.dirname(main_wDir)
    repo_url = "https://api.github.com/repos/SketchedDoughnut/development/releases/latest"
    copy_source = f"{ext_download_path}/SketchedDoughnut-development-{release_version}/everything/main/top"
    state = False

    # commit label
    release_version = requests.get("https://api.github.com/repos/SketchedDoughnut/development/releases/latest")
    release_version = release_version.json()
    release_version = str(release_version['body'])
    release_version = release_version.split()
    release_version = release_version[0]

    

    if mode == 'top':
        print('Update: installing top')
        print('If you want to backup your top, copy the directory now.')
        print(f'The directory is: {main_wDir}/top')
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

        print('---------------')
        print('Update: Cleaning tmp...')
        try:
            shutil.rmtree(f'{setup_wDir}/tmp')
        except:
            print('Update: No prior tmp')
        print('Update: Making tmp...')
        os.mkdir(f'{setup_wDir}/tmp')
        print('Update: deleting previous top...')
        try:
            shutil.rmtree(f"{main_wDir}/top")
        except Exception as e:
            print('Update: No prior top:', e)
        print('Update: Downloading .zip...')
        d.download_latest_release(repo_url, zip_download_path)
        print('Update: Extracting files...')

        # https://www.geeksforgeeks.org/unzipping-files-in-python/
        ee.extract(zip_download_path, ext_download_path)

        print('Update: Getting commit label...')
        print(f'Update: Copying files to {copy_location}...')

        # https://pynative.com/python-copy-files-and-directories/
        c.copy(copy_source, copy_location)

        print('Update: Cleaning up tmp...')
        try:
            shutil.rmtree(f'{setup_wDir}/tmp')
        except:
            print('Update: No tmp')

        print('Update: Checking install path...')
        if os.path.exists(f'{main_wDir}/top/container/game_data'):
            pass
        else:
            print('!!! UPDATE ERROR: The installed directory does not exist. Cancelling.')
            input('Enter anything to exit: ')
            exit()

        print('Update: Checking file integrity...')
        v.verify_files(json_path, everything_path)
            
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

        time.sleep(1)
        print('Update: Reaching to version.json...')
        print(f'Update: Path: {main_wDir}/top/container/version.json')
        f = open(f'{main_wDir}/top/container/version.json', 'w')
        print('Update: Dumping version...')
        json.dump(release_version, f)
        f.close()

        time.sleep(0.25)
        print('Update: Reaching to state.json...')
        print(f'Update: Path: {main_wDir}/top/container/version.json')
        f = open(f'{main_wDir}/top/container/state.json', 'w')
        print('Update: Dumping state...')
        json.dump(state, f)
        f.close()

        print('Update: top update complete!')
        print('---------------')
        input('Enter anything to exit: ')
        exit()