import os
wDir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(wDir, 'main/top/starter.py')
os.system(f'python {path}')