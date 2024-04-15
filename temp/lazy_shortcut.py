import os
wDir = os.path.dirname(os.path.abspath(__file__))

# py path
#path = os.path.join(wDir, 'main/top/starter.py')

# exe path
path = os.path.join(wDir, 'main/top/starter.exe')
os.system(f'python {path}')