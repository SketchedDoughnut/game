# builtins
import os
import shutil
import json
import time

# packages
import requests

# file imports
from .tools import backup as b
from .tools import rollback as r
from .tools import download as d
from .tools import extract as ee
from .tools import copy as c
from .tools import verify as v



def update_handler_install(
    mode,
    tmp_path,
    zip_path,
    everything_path,
    extract_path,
    repo_url,
    commit_label,
    esif,
    vsif
    ):
    if mode == 'full-install':
        print('Update: Deleting previous tmp...')
        try:
            shutil.rmtree(tmp_path)
        except:
            print('Update: No prior tmp')
        print('Update: Creating new tmp...')
        os.mkdir(tmp_path)

        main_wDir = f'{everything_path}/main'
        setup_wDir = f'{everything_path}/main/setup'
        b.backup_handler(
            main_wDir = main_wDir,
            setup_wDir = setup_wDir,
            backOrLoad = 'back',
            target = 'full-redo'
        )
        
        print('Update: Downloading .zip...')
        d.download_latest_release(repo_url, zip_path) # changed tmp_path to zip_path

        print('Update: Extracting files...')
        ee.extract(zip_path, tmp_path)

        print('Update: Deleting previous everything...')
        try:
            shutil.rmtree(everything_path)
        except:
            print('Update: No prior everything')

        print('Update: Copying files...')
        c.copy(extract_path, everything_path)

        print('Update: Checking file integrity...')
        json_path = f'{everything_path}/main/setup/file_list.json'
        results = v.verify_files(
            json_path = json_path,
            everything_path = everything_path
        )

        if results:
            b.backup_handler(
                main_wDir = main_wDir,
                setup_wDir = setup_wDir,
                backOrLoad = 'load',
                target = 'full-redo'
            )
            r.decide(True)

        print('Update: Reaching into data.json...')
        f = open(esif, 'r')
        td = json.load(f)
        f.close()
        td['shortcut'] = True
        print('Update: Dumping into data.json...')
        f = open(esif, 'w')
        json.dump(td, f)
        f.close()
        print('Update: Reaching into version.json...')
        print('Update: Dumping into version.json...')
        f = open(vsif, 'w')
        json.dump(commit_label, f)
        print('Update: Cleaning up tmp...')
        shutil.rmtree(tmp_path)
        print('Update: Full re-install done!')
        print('---------------')
        input('Enter anything to exit: ')
        exit()