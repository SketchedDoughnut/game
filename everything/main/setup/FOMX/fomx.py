'''
PLEASE REFER TO ./GUIDE.TXT FOR MORE INFO
'''

# builtins
import os 
import shutil
import time
import json
import sys

# external
import requests

# file imports
import tools.download as download
import tools.extract as extract

# ---------------------------------------------
url = 'https://api.github.com/repos/SketchedDoughnut/SDA-FOMX/releases/latest'
wDir = os.path.dirname(os.path.abspath(__file__))

def load_current_label(dir: str) -> str:
    path = os.path.join(dir, 'version.json')
    f = open(path, 'r')
    current = str(json.load(f))
    f.close()
    return current

def get_release_info(local_url: str) -> list:
    data = requests.get(local_url).json()
    data = str(data['body'])
    data = data.split()
    id = data[0]
    data.remove(id)
    n_word = ''
    for word in data: # re-assemble words with one-spacing
        n_word += word
        n_word += " "
    return [id, n_word]


current_label = load_current_label(wDir)
latest_label, content = get_release_info(url)
print('---------------')
print('FOMX: DATA')
print('    - current commit label:', current_label)
print('    - commit label of newest release:', latest_label)
print('FOMX: comparing versions...')
if current_label != latest_label:
    print('FOMX: versions do not match.')
    print('---------------')
    if input('FOMX: do you want to see the info for this update? (y/n): ').lower() == 'y':
        print('---------------')
        print('Info:')
        print('-', content)
        print('---------------')
    else:
        print('FOMX: skipping...')
        print('---------------')
    if input('Download this update? This is highly recommended (y/n): ').lower() == 'y':
        pass
    else:
        print('---------------')
        print('FOMX: exiting...')
        time.sleep(1)
        sys.exit()
print('---------------')
# vars
tmp_path = os.path.join(wDir, 'tmp')
zip_path = f'{tmp_path}/latest_release.zip'
bounds_json = f'{tmp_path}/SketchedDoughnut-SDA-FOMX-{latest_label}/data/bounds.json'




print('Attempting to delete previous tmp...')
try:
    shutil.rmtree(tmp_path)
except:
    pass
os.mkdir(tmp_path)

print('FOMX: downloading .zip...')
download.download_latest_release(url, zip_path)

print('FOMX: extracting...')
extract.extract(zip_path, tmp_path)

print('FOMX: reading bounds file...')
f = open(bounds_json, 'r')
bounds = json.load(f)
f.close()

print('FOMX: bounds data:')
print(bounds)