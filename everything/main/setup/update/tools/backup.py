import shutil
import time
import os
import json
import requests

'''
flow
    - when invoked, an update has failed
    - load files from backup file (given mode top or game_data)
    - put them in respective locations
    - return an error message about potentially damaged files (offer full-redo re-install)
        - if yes, do full-redo
        - if no, warn them again but reset data.json
'''

# this function is invoked:
#   - BEFORE A DELETION OF THE DIRECTORY BEING UPDATED IS DONE, 
#   - IF AN UPDATE FAILS, 
#   - AFTERWARDS FOR CLEANUP 
#       - (MUST BE AUTHORIZED, GIVE THEM A CHOICE TO SAVE)

def backup_handler(
        main_wDir, 
        setup_wDir, 
        backOrLoad, 
        target
    ):

    # if game_data
    if target == 'game_data':
        # set up vars
        copy_source = f'{main_wDir}/top/container/game_data'
        copy_destination = f'{setup_wDir}/update/tools/backup/game_data'

        if backOrLoad == 'back':
            print('Update: Backing up top...')
            print('- source:', copy_source)
            print('- destination:', copy_destination)
            shutil.copytree(copy_source, copy_destination)
            print('Update: Files are backed up')
        
        elif backOrLoad == 'load':
            print('Update: Cleaning failed installation...')
            shutil.rmtree(copy_source)
            print('Update: Reloading backup of game_data...')
            shutil.copytree(copy_destination, copy_source)

    # if top
    elif target == 'top':
        # set up vars
        copy_source = f'{main_wDir}/top'
        copy_destination = f'{setup_wDir}/update/tools/backup/top'

        if backOrLoad == 'back':
            print('Update: Backing up top...')
            print('- source:', copy_source)
            print('- destination:', copy_destination)
            shutil.copytree(copy_source, copy_destination)
            print('Update: Files are backed up')

        elif backOrLoad == 'load':
            print('Update: Cleaning failed installation...')
            shutil.rmtree(copy_source)
            print('Update: Reloading backup of top...')
            shutil.copytree(copy_destination, copy_source)

    # if full-redo
    elif target == 'full-redo':
        # set up vars
        copy_source = os.path.dirname(main_wDir)
        copy_destination = f'{setup_wDir}/update/tools/backup/everything'

        if backOrLoad == 'back':
            print('Update: Backing up everything...')
            print('- source:', copy_source)
            print('- destination:', copy_destination)
            shutil.copytree(copy_source, copy_destination)
            print('Update: Files are backed up')

        elif backOrLoad == 'load':
            print('Update: Cleaning failed installation...')
            shutil.rmtree(copy_source)
            print('Update: Reloading backup of everything...')
            shutil.copytree(copy_destination, copy_source)

    else:
        print('No valid target.')
        exit()