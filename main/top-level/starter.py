import os

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
os.system(f'python {run_path}')
