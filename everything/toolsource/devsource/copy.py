'''
This file merely copies from one place to another. Woo!
--------------------------------------------------------------------------------------------------------------------------------
This files adheres to the commenting guidelines :D
'''

# builtin moudules
import shutil

# the job of thsi function is to copy either a file or a folder
# from the source to the destination
# shrimple :D
def copy(source_dir, destination_dir, mode='folder'):
    if mode == 'folder':
        shutil.copytree(source_dir, destination_dir)
    if mode == 'file':
        shutil.copyfile(source_dir, destination_dir)