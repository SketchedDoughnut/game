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
import time
import shutil
import timeit
import sys
import json
import urllib.request 

# external modules
import requests




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
        def __init__(self, mode=0):
            
            # assigning self variables
            # if the program is in a folder
            self.in_folder = False

            # this is an outline of how paths are established
            # this just helps visualize it, because it is a nightmare
            # and compiling with pyinstaller makes paths act a bit differently
            # then they would act if it was a raw python script
            '''
            path behaviors (why do I have to do this UGH)
            
            - when in a setup folder: FAIL
                - file paths will not go back enough. Instead, main will go back into setup, making it main/setup.
                - setup will add one more setup, making it main/setup/setup.
                - these will not pass the folder requirement and will FALSELY claim that it is not in a folder.

            - when not in a setup folder: WORK
                - file paths do go back enough, making main into main/ (with desktop example, it makes it into desktop).
                - setup (using desktop example), becomes desktop/setup (not used, however, if it is detected properly).

            - so what we want to do:
                - get main path first
                - check for setup in main path (if __ in __)
                    - if yes, check if that path exists
                        - if yes, set that path to setup path
                        - rollback one more for main path
                
                    - if no, we know it is not in a setup folder
                        - make sure path exists
                            - if yes, set that to main AND setup 
                '''
            
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
                if split_wDir[-1] == 'internal':
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

            # now, we open the file
            # containing rules for what functions to run
            # these are in a different file so it does not get
            # hard-coded into the .exe when it is compiled,
            # and therefore making it hard to edit
            rulesFile = open(f'{self.setup_wDir}/config.json', 'r')
            self.rules: dict = json.load(rulesFile)
            rulesFile.close()

            # next, we check if anything is set to True 
            # within the rules. If nothing is true, then we can't do 
            # anything, so we just exit
            nonFalseFound = False
            for key in self.rules.keys():
                if self.rules[key] == True:
                    nonFalseFound = True
            
            # if this is true, then that means there is
            # at least something being executed. This means that
            # the code will continue. Otherwise, print an error
            # then exit
            if not nonFalseFound:
                print('---------------')
                print(f'Nothing in {self.setup_wDir}/config.json is set to True, exiting')
                print('---------------')
                input('-> ')
                sys.exit()

            # if the variable shortcut is set to True,
            # that means that the purpose of this file is simply to redirect
            # into the other files downstream. However, as this file is not for being
            # an installer and it is purely for redirecting / updating, 
            # shortcut is always set to True
            dataFile = open(f'{self.setup_wDir}/data.json', 'r')
            launchData = json.load(dataFile)
            dataFile.close()
            if launchData['shortcut']:


                if data_dict['update']:
                    """
                    NOTE
                        - THIS FILE IS NOT CAPABLE OF THE NEW UPDATE CAPABILITIES. IT IS IN BETA AND WILL NOT BE FUNCTIONING UNTIL FIXED.
                        DO NOT ACCESS THIS FILE IN THE BETA FOLDER FOR ANY REASON, AS IT WILL LIKELY NOT WORK.
                    """

                    from update import fr_controller_setup as frc
                    from update import t_controller as tc
                    from update import gd_controller as gdc
                    
                    print('---------------')
                    print('Installer is in update mode.')

                    if data_dict['bounds'] == 'full':
                        print('---------------')
                        print('Installer is in full mode.')
                        frc.update_handler_setup(
                            setup_wDir = self.setup_wDir,
                            mode = 'full-setup',
                            everything_path = os.path.dirname(self.main_wDir)
                        )
                        

                        
                    if data_dict['bounds'] == 'top':
                        print('---------------')
                        print('Installer is in top mode.')
                        tc.update_handler(
                            main_wDir = self.main_wDir,
                            setup_wDir = self.setup_wDir
                        )



                    if data_dict['bounds'] == 'game_data':
                        print('---------------')
                        print('Installer is in game_data mode.')
                        gdc.update_handler(
                            setup_wDir = self.setup_wDir,
                            main_wDir = self.main_wDir
                        )


                    else:
                        print('---------------')
                        print('Improper update bounds. Redirecting to starter file...')
                        
                        # FOR PYTHON
                        self.top_wDir = (os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

                        # FOR COMPILE
                        self.top_wDir = os.path.dirname(self.top_wDir)

                        self.top_wDir = os.path.join(self.top_wDir, 'top')
                        c1 = r'{path}/starter.py'.format(path=self.top_wDir) # calling string
                        # os.system(f'python {self.top_wDir}/starter.py')
                        # os.system(c1)
                        subprocess.run(f'python "{c2}"')
                        sys.exit() 




                else:
                    # FOR PYTHON
                    self.top_wDir = (os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

                    # FOR COMPILE
                    self.top_wDir = os.path.dirname(self.top_wDir)

                    print('---------------')
                    print('Installer running FOMX...')
                    c2 = '{path}/setup/FOMX/fomx.py'.format(path=self.top_wDir) # caling string
                    # print('going to path:', c2)
                    # os.system(f'python {self.top_wDir}/setup/FOMX/fomx.py')
                    # os.system(c2)
                    subprocess.run(f'python "{c2}"')
                    print('---------------')
                    self.top_wDir = os.path.join(self.top_wDir, 'top')
                    print('Installer redirecting to starter file...')
                    c2 = r'{path}/starter.py'.format(path=self.top_wDir) # calling string
                    # os.system(f'python {self.top_wDir}/starter.py')
                    # os.system(c2)
                    subprocess.run(f'python "{c2}"')
                    sys.exit() 


    ## ONLY TWO ACTING LINES OF CODE
    # initializes Install class
    install = Install()


    # calls on run function
    install.run()

except Exception as e:
    import os
    import traceback
    import setup_crash_handler
    setup_crash_handler.Crash_handler(
        error = traceback.format_exc()
    )