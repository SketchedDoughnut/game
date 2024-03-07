import os
import time

## when in codespace
    #run_path = 'main/top-level/game_data/main.py'

## if file function is ever implemented
    # f = open('content_url.txt', 'r')
    # run_path = f.read()
    # f.close()

#################################################################

# intended path
run_path = 'game_data/main.py'

# prints what directory it is running
print(f'Running game: {run_path}')

# tries to run, if can't errors then quits
try:
    os.system(f'python {run_path}')
    
except Exception as e:
    print(f'Error when running: {e}')
    print('exiting in 30s...')
    for i in range(29, 0, -1):
        print(i)
        time.sleep(1)
    exit()
