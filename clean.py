import os
import shutil

try:
    shutil.rmtree('README.md')
    shutil.rmtree('gitignore')
    shutil.rmtree('main/setup')
    print('file cleanup done')
except Exception as e:
    print(e)