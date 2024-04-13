import pygame
from pygame.locals import *
print('----------------------------')
import json
import os
import requests
import time
import threading

# overruling exit var
exit = False

def check_version():
    # release destination, working directory, loading version
    dest = 'https://api.github.com/repos/SketchedDoughnut/development/releases/latest' # link format: https://api.github.com/repos/{owner}/{repo}/releases/latest
    wDir = os.path.dirname(os.path.abspath(__file__))
    response = requests.get(dest)
    # print(response.json()["name"])

    # check if version file exists (how to handle if not?)
    if os.path.exists(os.path.join(wDir, 'version.json')):
        print('File found: Comparing versions...')

        # loads version
        f = open(f'{wDir}/version.json', 'r')
        version = json.load(f)
        f.close()

        # seeing if there is a difference
        if str(version) != response.json()["name"]:
            print('Name decrepancy: Prompting for update...')

        elif str(version) == response.json()["name"]:
            print('No decrepancy:   Exiting...')
            time.sleep(3)
            exit = True

check_version()