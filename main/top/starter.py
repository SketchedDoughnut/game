import os
import time
import json

## if file function is ever implemented
    # f = open('content_url.txt', 'r')
    # run_path = f.read()
    # f.close()

# hardcoded paths
# un_path = 'game_data/main.py'
# alt_path = 'main/top/game_data/main.py'

#################################################################
# for run
paths = open('start.json')

# - for codespace
#paths = open('main/top/start.json')

paths = json.load(paths)

# intended path
run_path = paths['run_path']
alt_path = paths['alt_path']


# prints what directory it is running
print(f'Running game: {run_path}')
print(f'Alt: {alt_path}')
print('----------------------')

# - for codespace
#os.system(f'python {alt_path}')

# for run 
os.system(f'python {run_path}')

#################################################################

#tries to run, if can't errors then quits
# try:
    # print('running main')
    # os.system(f'python {run_path}')
# 
# except:
    # try:
        # print('running alt')
        # os.system(f'python {alt_path}')
    # except Exception as e:
        # print(f'Error when running: {e}')
        # print('exiting in 30s...')
        # for i in range(29, 0, -1):
            # print(i)
            # time.sleep(1)
        # exit()