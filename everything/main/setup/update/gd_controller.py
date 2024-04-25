import os
import shutil
import json
import time

# packages
import requests

# file imports 
import download as d
import extract as ee
import copy as c
import verify as v

def update_handler(
        mode,
        main_wDir,
        setup_wDir,
        zip_download_path,
        ext_download_path,
        copy_source,
        copy_location,
        json_path,
        everything_path,


    ):

    '''
    variables here
    - repo_url
    - release_version
    '''

    if mode == 'game_data':
        print('Update: installing game_data')
        print('If you want to backup your game_data, copy the directory now.')
        print(f'The directory is: {main_wDir}/top/container/game_data')
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
        print('Update: deleting previous game_data...')
        try:
            shutil.rmtree(f"{main_wDir}/top/container/game_data")
        except:
            print('Update: No prior game_data')
        print('Update: Downloading .zip...')
        repo_url = "https://api.github.com/repos/SketchedDoughnut/development/releases/latest"
        zip_download_path = f"{setup_wDir}/tmp/latest_release.zip"  # Change the path if needed
        d.download_latest_release(repo_url, zip_download_path)
        ext_download_path = f"{setup_wDir}/tmp"
        print('Update: Extracting files...')

        # https://www.geeksforgeeks.org/unzipping-files-in-python/
        ee.extract(zip_download_path, ext_download_path)

        print('Update: Getting commit label...')
        #release_version = ((requests.get(("https://api.github.com/repos/SketchedDoughnut/development/releases/latest")).json()['body']))
        release_version = requests.get("https://api.github.com/repos/SketchedDoughnut/development/releases/latest")
        release_version = release_version.json()
        release_version = str(release_version['body'])
        release_version = release_version.split()
        release_version = release_version[0]
        copy_source = f"{ext_download_path}/SketchedDoughnut-development-{release_version}/everything/main/top/container/game_data"
        copy_location = f'{(main_wDir)}/top/container/game_data'
        print(f'Update: Copying files to {copy_location}')

        # https://pynative.com/python-copy-files-and-directories/
        c.copy(copy_source, copy_location)

        print('Update: Cleaning up tmp...')
        try:
            shutil.rmtree(f'{setup_wDir}/tmp')
        except:
            print('Update: No tmp')
        
        print('Update: Checking install path...')
        if os.path.exists(f'{setup_wDir}/top/container/game_data'):
            pass
        else:
            print('!!! UPDATE ERROR: The installed directory does not exist. Cancelling.')
            input('Enter anything to exit: ')
            exit()

        print('Update: Checking file integrity...')
        import update.verify as verify_agent
        json_path = os.path.join(setup_wDir, 'file_list.json')
        everything_path = os.path.dirname(main_wDir)
        verify_agent.verify_files(json_path, everything_path)
        
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

        print('Update: Reaching to version.json...')
        print(f'Update: Path: {main_wDir}/top/container/version.json')
        #print(release_version)
        print('Update: Dumping version...')
        f = open(f'{main_wDir}/top/container/version.json', 'w')
        #print(release_version)
        json.dump(release_version, f)
        f.close()

        print('Update: Reaching to state.json...')
        print(f'Update: Path: {main_wDir}/top/container/state.json')
        f = open(f'{main_wDir}/top/container/state.json', 'r')
        tmp = json.load(f)
        f.close()
        f = open(f'{main_wDir}/top/container/state.json', 'w')
        tmp = False
        json.dump(tmp, f)
        f.close()
        
        print('Update: Game data update complete!')
        print('---------------')
        input('Enter anything to exit: ')
        exit()