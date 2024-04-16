import shutil

def copy(source_dir, destination_dir):
    shutil.copytree(source_dir, destination_dir)