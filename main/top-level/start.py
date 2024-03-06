import os

#run_path = 'python ../game_data/game_content/main.py'
# f = open('content_url.txt', 'r')
# run_path = f.read()
# f.close()

#run_path = 'main/top-level/game_data/main.py'
run_path = 'game_data/main.py'
print(f'Running game: {run_path['path']}')
os.system(f'python {run_path['path']}')
