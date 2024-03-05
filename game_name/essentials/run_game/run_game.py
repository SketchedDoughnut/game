import os

#run_path = 'python ../game_data/game_content/main.py'
f = open('content_url.txt', 'r')
run_path = f.read()
f.close()

print(f'Running game: {run_path}')
os.system(run_path)