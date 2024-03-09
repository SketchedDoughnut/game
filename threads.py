import threading
import os
import time

def run_file(path):
    os.system(f'python {path}')


threading.Thread(target=lambda: run_file('gitignore/render/3d_terrain.py')).start()

threading.Thread(target=lambda: run_file('main/top-level/starter.py')).start()


# print(threading.active_count())