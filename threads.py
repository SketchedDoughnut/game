import threading
import os
import time

def run_file(path):
    os.system(f'python {path}')

threading.Thread(target=lambda: run_file('gitignore/render/3d_terrain.py')).start()
print('------------------')
threading.Thread(target=lambda: run_file('main/setup/fiesta.exe')).start()

# print(threading.active_count())