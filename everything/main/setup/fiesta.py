'''
This is one of the two original pieces of this whole project.
The job of this piece is to be used for starting the program as normal. It is the main, core component.
It also manages updates whenever those occur, so it is truly crucial.
--------------------------------------------------------------------------------------------------------------------------------
This files adheres to the commenting guidelines :D
'''

# builtin modules
import os
import subprocess
import sys
import json

# external modules
from rich import print

# file imports
from update import fr_controller_setup as frc
from update import t_controller as tc
from update import gd_controller as gdc




# everything is inside of a try / except
# this is to catch and crashes and log them
# however, if a crash happens this high up, then it
# is likely a fatal issue that would require a manual
# recovery of files (or reverting to a previous, working version)
try:

    # this is the main class,
    # containing all functions for updating, redirecting,
    # etc
    class Install:

        # this it the init class, called on
        # when the class is being initialized into an object
        # conveniently, this also does everything!
        def __init__(self):
            
            # assigning self variables
            # if the program is in a folder
            self.in_folder = False
            
            # here, we just establish the current working directory
            internal_wDir = os.path.dirname(os.path.abspath(__file__))

            # we split the path by its path dividers
            if '/' in internal_wDir: split_wDir = internal_wDir.split('/')
            elif '\\' in internal_wDir: split_wDir = internal_wDir.split('\\')

            # this variable, in_folder, represents if the current file
            # is in a setup folder or not
            # if it is not in a setup folder, this will be false
            # theoretically since this is always used for normal operation,
            # it should be in a setup folder. However, you never know I guess?
            in_setup_folder = False

            # now, we remove anything extra from the internal_wDir
            # this is not done in the most efficient way but oh well
            # the goal of this is to get the proper paths of directories
            while True:

                # if the path still has _internal, we remove that
                if split_wDir[-1] == '_internal':
                    split_wDir.pop(-1)
                
                # if the last entry in the path is "setup",
                # then we assign the appropriate variables then break
                if split_wDir[-1] == 'setup':
                    in_setup_folder = True
                    joined_wDir = ''
                    for path_section in split_wDir:
                        joined_wDir += path_section
                        joined_wDir += '\\'
                    joined_wDir = joined_wDir.removesuffix('\\')
                    self.setup_wDir = joined_wDir

                    # to get the main path, we need to remove the 
                    # "setup" that is at the end
                    self.main_wDir = self.setup_wDir.removesuffix('\\setup')

                    # then we break
                    break

                # if the last entry is not setup, we check if it is "main"
                # if it is, then we assign the appropriate variables then break
                if split_wDir[-1] == 'main':
                    joined_wDir = ''
                    for path_section in split_wDir:
                        joined_wDir += path_section
                        joined_wDir += '\\'
                    joined_wDir = joined_wDir.removesuffix('\\')
                    self.setup_wDir = os.path.join(joined_wDir, 'setup')
                    self.main_wDir = joined_wDir

                    # then we break
                    break
                
            # just some printing that is now just cosmetic,
            # but eh we keep it in :3
            if in_setup_folder:
                print('It appears this file is in a setup folder. Defaulting to those paths.')
            
            elif not in_setup_folder:
                print('It appears this file is not within a setup folder. Defaulting to those paths.')
            print(self.main_wDir)
            print(self.setup_wDir)

            # here the path for the virtual environment
            # is created, so we can run python properly
            # with the right dependencies
            self.PYTHON_VENV_PATH = f'{self.setup_wDir}/venv/Scripts/python.exe'

            # load the data from the data.json file
            data_path = os.path.join(self.setup_wDir, 'data.json')
            dataFile = open(data_path, 'r')
            launchData: dict = json.load(dataFile)
            dataFile.close()

            # if the variable shortcut is set to True,
            # that means that the purpose of this file is simply to redirect
            # into the other files downstream. However, as this file is not for being
            # an installer and it is purely for redirecting / updating, 
            # shortcut is always set to True
            if launchData['shortcut']:

                # if the update toggle is set to True,
                # then we have to see what type of update is being
                # invoked
                if launchData['update']:
                    print('---------------')
                    print('Installer is in update mode.')

                    # if the full re-install is being invoked,
                    # do the appropriate actions
                    if launchData['bounds'] == 'full':
                        print('---------------')
                        print('Installer is in full mode.')
                        frc.update_handler_setup(
                            setup_wDir = self.setup_wDir,
                            mode = 'full-setup',
                            everything_path = os.path.dirname(self.main_wDir)
                        )

                    # if the top re-install is being invoked,
                    # do the appropriate actions                        
                    if launchData['bounds'] == 'top':
                        print('---------------')
                        print('Installer is in top mode.')
                        tc.update_handler(
                            main_wDir = self.main_wDir,
                            setup_wDir = self.setup_wDir
                        )

                    # if the game_data re-install is being invoked,
                    # do the appropriate actions
                    if launchData['bounds'] == 'game_data':
                        print('---------------')
                        print('Installer is in game_data mode.')
                        gdc.update_handler(
                            setup_wDir = self.setup_wDir,
                            main_wDir = self.main_wDir
                        )

                    # if the update bounds are wrong,
                    # then the code just continues on to redirecting
                    # into files downstream
                    else:
                        print('---------------')
                        print('Improper update bounds. Continuing...')

                # if the file is not in update mode,
                # then continue on with calling things 
                # such as FOMX, then files downstream
                else:

                    # first, we call on FOMX to apply patches and whatnot
                    print('---------------')
                    FOMX_callpath = r'{path}/FOMX/fomx.py'.format(path=self.setup_wDir)
                    print(f'Installer running FOMX... ({FOMX_callpath})')
                    subprocess.run(f'{self.PYTHON_VENV_PATH} "{FOMX_callpath}"')
                    print('---------------')

                    # next, we call on the starter file which handles things from here
                    starter_callpath = r'{path}/starter.py'.format(path=os.path.join(self.main_wDir, 'top'))
                    print(f'Installer redirecting to starter file... ({starter_callpath})')
                    subprocess.run(f'{self.PYTHON_VENV_PATH} "{starter_callpath}"')
                    sys.exit() 

            # if thef iel is not in shortcut mode,
            # nothing can be done so the file just exists
            # this should not be possible or done inentionally,
            # but I suppose we prepare for any / all eventualities?
            else:
                print('---------------')
                print(f'Shortcut is not set to true in {data_path}, so this program can not do anything.')
                input('Enter anything to exit: ')
                sys.exit()


    ## ONLY TWO ACTING LINES OF CODE
    # initializes Install class
    # and also runs all of the code
    install = Install()

# in the event of an error, this logs that error
# in a file and crashes gracefully
except Exception as e:
    import os
    import traceback
    import setup_crash_handler
    setup_crash_handler.Crash_handler(
        error = traceback.format_exc()
    )