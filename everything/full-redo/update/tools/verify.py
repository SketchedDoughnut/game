'''
This is a tool used by the controller for updates.
It verifies the installed files against every file that should be installed.
If there are any issues, then the backup will be restored.
--------------------------------------------------------------------------------------------------------------------------------
This files adheres to the commenting guidelines :D
'''

# builtin modules
import os
import json
# import py_compile # interesting thing

# the main function for verifying that all files exist
# its just that shrimple!
def verify_files(json_path, everything_path):
    
    # setting up variables
    failed = False
    failed_count = 0

    # load the data from the json file (file_list.json)
    f = open( json_path, 'r')
    files = json.load(f)
    f.close()

    # for each path in that json, make sure it exists
    # if it does not exist, increase failcount
    # once counter is over threshold, raise error then return the state
    # that state decides if the backup is restored
    for file in files:
        assemble = os.path.join(os.path.dirname(everything_path), file)
        if os.path.exists(assemble):
            #print(f'- verified {files.index(file) + 1}/{len(files)} - {assemble}')
            pass
        else:
            print(f'- FILE DOES NOT EXIST: {assemble}')
            failed_count += 1
    if failed_count > 0:
        failed = True
        print('------------------------------------')
        print('- It appears that 1 or more files are missing. This update will cancel, and instead reload your backup.')
        print('------------------------------------')
        # break
    return failed