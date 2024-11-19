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

# external modules
import json
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
        # this detects if there are possible things to do,
        # as well as some data formatting
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

            # now, we open the file
            # containing rules for what functions to run
            # these are in a different file so it does not get
            # hard-coded into the .exe when it is compiled,
            # and therefore making it hard to edit
            config_path = os.path.join(self.setup_wDir, 'config.json')
            print(f'Loading config... ({config_path})')
            rulesFile = open(config_path, 'r')
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
                print(f'Nothing in {config_path} is set to True, exiting')
                print('---------------')
                input('Enter anything to exit: ')
                sys.exit()



















                        
                print('---------------')
                print("""
                Welcome to the open-source installer created by Sketched Doughnut! 
                    Code is written by Sketched Doughnut with snippets from others.
                    Sources are in: (install location)/gitignore/sources.txt.   
                """)
                path_loop = True
                while path_loop:
                    print(f"""---------------
                Input folder directory for install below (or type "delete" to delete).'
    Note: Must be absolute path from the root. For example, the absolute path of this folder is:
    - {os.getcwd()}
    The default file path, if nothing is entered, is set to Program Files.
    - {os.path.join(os.environ['SystemDrive'], '/Program Files')}""")
    # IMPORTANT: PLEASE DO NOT USE A FOLDER PATH WITH ANY SPACES IN IT.
                    self.install_path = input('--> ')

                    # checking for uninstall, doing uninstall if so
                    if self.install_path == "delete":
                        print('---------------')
                        if input('Are you sure you want to delete?  \nType: "confirm-delete", anything else to cancel \n--> ') == 'confirm-delete':

                            # for run
                            if self.rules['env'] == 'run':
                                c1 = r'{path}/delete.py'.format(path=self.main_wDir)
                                # os.system(f'python {self.main_wDir}/delete.py')
                                # os.system(c1)
                                subprocess.run(f'python "{c1}"')

                            # - for codespace
                            else:
                                c1 = r'main/setup/delete.py'
                                # os.system(f'python main/setup/delete.py')
                                # os.system(c1)
                                subprocess.run(f'python "{c1}"')

                            # final, then finishes
                            print('---------------')
                            # print('Delete done. This installer will exit in 30 seconds; afterwards, delete the folder it is in. Thank you for using this installer! :3')
                            # time.sleep(15)
                            # for i in range(15, 0, -1):
                            #     print(i)
                            #     time.sleep(1)
                            print('Delete done. You can now get rid of any installer files. Thank you for using this installer! :3')
                            input('Enter anything to exit: ')
                            sys.exit()
                    
                        # cancelling uninstall if wrong input
                        else:
                            print('Cancelling deletion, cancelling file in 5s...')
                            for i in range(5, 0, -1):
                                print(i)
                                time.sleep(1)
                            sys.exit()

                    else:

                        # formatting file path
                        try:
                            self.install_path = self.install_path_format(self.install_path)
                            path_loop = self.install_path[1]
                            self.install_path = self.install_path[0]

                        except Exception as e:
                            print('---------------')
                            print(f'Path formatting error: {e}')
                            print('Please restart installer and enter the correct path.')
                            input('Enter anything to exit: ')
                            sys.exit()
                        print('---------------')
                            


        # format install path
        def install_path_format(self, path):
            # try:
            #     programFiles = os.path.abspath("Program Files")
            #     if not path:
            #         print('Path is defaulting to Program Files.')
            #         path = programFiles
            #         path += '\game_name'
            #         return path

            if not path:
                print('Path is defaulting to Program Files.')
                try:
                    path = os.path.abspath("Program Files")
                    path = os.path.join(os.environ['SystemDrive'], '/Program Files')
                    ns = ''
                    next = False
                    for letter in path:
                        if next == False:
                            ns += letter

                        if next == True:
                            ns += '/'
                            ns += letter
                            next = False

                        if letter == ':':
                            next = True

                        else:
                            next = False
                    path = ns
            
                except Exception as e:
                    print(f'Default path error: {e}')

            new_string = ''
            list = []

            list = [str(i) for i in path]
            for i in list:
                if i == '\\':
                    new_string += '/'
                else:
                    new_string += i

            path = new_string
            path = [str(i) for i in path]
            if path[len(path) - 1] == '/':
                path.pop(len(path) - 1)

            else:
                pass

            new_string = ''
            for i in path:
                new_string += i
            path = new_string

            if os.path.exists(path):
                path += '/SDA_game_name' # used to be game_name
                return [path, False]
        
            else:
                print('---------------')
                print('That path does not exist. Please try again.')
                print('-->', path)
                return [path, True]
            

        # making sure they are sure of their choice
        def safety_check(self):
            print(f"""
                You are running the installer; this will overwrite pre-existing files created by the installer previously
                                            inside of {self.install_path}.
                                    To confirm, type "confirm" below. Otherwise, type anything else.
                """)
            
            # checking if input confirms proceeding, cancelling if not
            if input('--> ') == "confirm":
                print('---------------')
                pass

            # cancels program if doesn't confirm clearing
            else:
                print('Cancelling...')
                time.sleep(2)
                sys.exit()


        # cleaning before any running
        def pre_clean(self, run_error=''):
            if run_error == 'error':
            
                # removing install tree
                try:
                    shutil.rmtree(self.install_path)
                    print(f'Pre: ! install cleaned')
                except:
                    print(f'Pre: ! no install')

            else:
                print('Pre: Cleaning up directories before install')

                # removing install tree
                try:
                    print(f'Deleting from: {self.install_path}')
                    if input('Continue? (y/n) ').lower() == 'n':
                        print('Cancelling...')
                        time.sleep(5)
                        sys.exit()
                        
                    shutil.rmtree(self.install_path)
                    print(f'! install cleaned')
                except:
                    print(f'! no install')

                print('Pre: Done cleaning; continuing...')
                time.sleep(1)
                print('---------------')

        
        # getting info
        def setup(self):
            # getting inputs
            # https://github.com/BirdLogics/sb3topy
            #    self.url = input('Input repository URL: ')
            #    self.branch = input('Input respository branch: ')
            self.desktop_shortcut = (input('Do you want to add a desktop shortcut? (y/n) \n--> ').lower()) == 'y'
            
            # make sure they have python installed
            print('---------------')
            print("""Before we proceed, you need to have an installation of python installed. 
      This project has been built for python 3.11, and functionality can not be guaranteed with other versions.
                      If you already have one, enter 'y' to proceed. If you don't, enter 'n'""")
            choiceee = input('-> ')
            if choiceee.lower() == 'n':
                import update.install.python_helper as py_helper
                loader = py_helper.Python_helper(self.setup_wDir)
                loader.main()
                if loader.run_install == True:
                    loader.run_python_installer()
                else:
                    print('User has chosen not to run install, skipping...')
            # print("""
            #             Before we proceed, you need to have an installation of python installed.
            #     If you already have one, type "y" to proceed. If you don't, do the following instructions:
            #     - go to Microsoft Store
            #     - search "Python 3.11"
            #     - Install
            #     - You're done!
            #                 Once done doing these instructions, type 'y' (anything else to cancel).
            #             NOTE: FUNCTIONALITY CAN NOT BE GUARANTEED WITH ANY OTHER PYTHON VERSIONS.
            #     """)
            # if input('--> ').lower() != 'y':
            #     sys.exit()
            if False:
                pass

            else:
                state = ''
                loop1 = True
                loop2 = True

                while loop1:
                    print('---------------')
                    print(f"""Install info:
                        
            - location: {self.install_path}
            - shortcut: {self.desktop_shortcut}

    If these are incorrect, type the name of what you want to re-enter. For example:
    "shortcut" or "location"
    Otherwise, enter 'y' to continue.""")
                    
                    loop2 = True
                    while loop2:
                        choice = input('--> ').lower()
                        print('---------------')

                        if choice == 'y':
                            state = 'y'
                            loop1 = False
                            loop2 = False

                        elif choice == 'shortcut':
                            state = 'shortcut'
                            loop2 = False
                        
                        elif choice == 'location':
                            state = 'location'
                            loop2 = False

                        else:
                            print('Wrong input. Try again.')
                        
                    if state == 'y':
                        loop1 = False

                    elif state == 'shortcut':
                        print("input 'y' if you want a shortcut, 'n' if you don't.")
                        self.desktop_shortcut = input('--> ').lower() == 'y'
                        print(f'Shortcut changed to: {self.desktop_shortcut}')
                    
                    elif state == 'location':
                        print('input the absolute path to the installation location.')
                        self.install_path = self.install_path_format(input('--> '))[0]
                        print(f'path changed to: {self.install_path}')
                    

        # create temp dir and establish code file
        def create(self):

            # creating directories
            print(f'Creating directory: {self.install_path}')
            os.mkdir(self.install_path)

            # opening delete file and writing path
            print('Dumping delete path...')
            # for run
            if self.rules['env'] == 'run':
                data = open(f'{self.setup_wDir}/data.json', 'r')
            
            # - for codespace
            else:
                data = open('main/setup/data.json', 'r')

            data_content = json.load(data)
            data.close()
            data_content["remove_path"] = self.install_path

            # for run
            if self.rules['env'] == 'run':
                data = open(f'{self.setup_wDir}/data.json', 'w')

            # - for codespace
            else:
                data = open('main/setup/data.json', 'w')

            json.dump(data_content, data)
            data.close()


        # https://www.blog.pythonlibrary.org/2010/01/23/using-python-to-create-shortcuts/ -> example 3
        def createShortcut(self, path, target='', wDir='', icon=''):  
            from win32com.client import Dispatch
            ext = path[-3:]
            if ext == 'url':
                #shortcut = file(path, 'w')
                shortcut = open(path, 'w')
                shortcut.write('[InternetShortcut]\n')
                shortcut.write('URL=%s' % target)
                shortcut.close()
            else:
                shell = Dispatch('WScript.Shell')
                shortcut = shell.CreateShortCut(path)
                shortcut.Targetpath = target
                shortcut.WorkingDirectory = wDir
                if icon == '':
                    pass
                else:
                    shortcut.IconLocation = icon
                shortcut.save()


    # function to download incorporating class: https://github.com/fbunaren/GitHubFolderDownloader
        def download(self):
            try:
                
                ## DOWNLOADING SETUP GOES HERE
                # imports
                import update.tools.download as d
                import update.tools.extract as e
                import update.tools.copy as c

                # downloading
                try:
                    self.start = timeit.default_timer()
                    












                    
                    # creating directory
                    print('---------------')
                    print('Update: Cleaning tmp...')
                    try:
                        shutil.rmtree(f'{self.install_path}/tmp')
                    except:
                        print('Update: No prior tmp')
                    print('Update: Making tmp...')
                    os.mkdir(f'{self.install_path}/tmp')

                    # downloading .zip
                    repo_url = "https://api.github.com/repos/SketchedDoughnut/development/releases/latest"
                    #repo_url = "https://api.github.com/repos/SketchedDoughnut/SDA-src/releases/latest"
                    # TRANSITION TO NEW REPO! LETS SEE HOW THIS GOES WOOOOOOOOOOOOOOOOOOOOOOO
                    
                    print('Update: Downloading .zip...')
                    zip_download_path = f"{self.install_path}/tmp/latest_release.zip"  # Change the path if needed
                    d.download_latest_release(repo_url, zip_download_path)

                    print('Update: Extracting files...')
                    ext_download_path = f"{self.install_path}/tmp"
                    e.extract(zip_download_path, ext_download_path)

                    print('Update: Getting commit label...')
                    release_version = requests.get(repo_url)
                    release_version = release_version.json()
                    release_version = str(release_version['body'])
                    release_version = release_version.split()
                    self.release_version = release_version[0]

                    copy_location = f'{(self.install_path)}/everything'
                    back_extract = f'{self.install_path}'
                    other_paths = [ 
                        # all MD
                        [f"{ext_download_path}/SketchedDoughnut-development-{self.release_version}/changelog.md", 'changelog.md'],
                        [f"{ext_download_path}/SketchedDoughnut-development-{self.release_version}/README.md", 'README.md'],
                        # all extensionless,
                        [f"{ext_download_path}/SketchedDoughnut-development-{self.release_version}/.gitattributes", '.gitattributes'],
                        [f"{ext_download_path}/SketchedDoughnut-development-{self.release_version}/LICENSE", 'LICENSE'],
                        [f"{ext_download_path}/SketchedDoughnut-development-{self.release_version}/Pipfile", 'Pipfile'],
                        # all other types (.lock, other .txt),
                        [f"{ext_download_path}/SketchedDoughnut-development-{self.release_version}/requirements.txt", 'requirements.txt'],
                        [f"{ext_download_path}/SketchedDoughnut-development-{self.release_version}/Pipfile.lock", 'Pipfile.lock']
                    ]
                    folder_create = [
                        'universe',
                        'universe/index'
                    ]

                    print(f'Update: Copying files to {copy_location}...')
                    copy_source = f"{ext_download_path}/SketchedDoughnut-development-{self.release_version}/everything/"
                    c.copy(copy_source, copy_location)

                    # new experimental copying system for extra files
                    print(f'Update: Copying IMPORTANT files to {back_extract}...')
                    for file in other_paths:
                        print('- copying:', file[1])
                        c.copy(file[0], f'{back_extract}/{file[1]}', mode='file')
                    
                    # new new system for creating universe/ if it doesn't exist
                    print('Update: Creating universe if non-existent...')
                    for folder in folder_create:
                        try:
                            os.mkdir(f'{back_extract}/{folder}')
                            print('- created:', folder)
                        except Exception as ee:
                            print('- error creating universe folder:', ee)

                    print('Update: Cleaning up tmp...')
                    try:
                        shutil.rmtree(f'{self.install_path}/tmp')
                    except:
                        print('Update: No tmp')

                    print('Update: Checking install path...')
                    if os.path.exists(f'{self.install_path}/everything'):
                        pass
                    else:
                        print('!!! UPDATE ERROR: The installed directory does not exist. Cancelling.')
                        input('Enter anything to exit: ')
                        sys.exit()






















                    # writing run path to text file (not used, not up to date)
                    try:
                        print('Update: Assembling text file...')
                        url_path = f'{self.install_path}/everything/main/top/content_url.txt'
                        f = open(url_path, 'w')
                        f.write(f'{self.install_path}/everything/main/top/game_data/main.py')
                        f.close()

                    except Exception as e:
                        print(f'!!! Error with text file: {e}')

                    # formats info and runs shortcut making function
                    try:
                        if self.desktop_shortcut == True:
                            #print('---------------')
                            print('Update: Deleting previous shortcut...')
                            try:
                                os.remove(path)
                            except:
                                print('Update: No prior shortcut.')
                            
                            time.sleep(0.25)
                                
                            import winshell
                            print('Update: Creating shortcut...')
                            desktop = winshell.desktop()
                            
                            path = os.path.join(desktop, "SDA_game_name.lnk") # CHANGE game_name TO NAME
                            self.abs_shortcut = path
                            #target = f"{self.install_path}/main/top/starter.exe" # CHANGE TO EXE
                            target = f"{self.install_path}/everything/main/setup/fiesta.exe" # CHANGE TO EXE
                            wDir = f"{self.install_path}/everything/main/setup"
                            #icon = f"{self.install_path}/main/top/starter.exe" # CHANGE TO EXE
                            icon = f"{self.install_path}/everything/main/setup/fiesta.exe" # CHANGE TO EXE

                            # calls on function here with data from above
                            self.createShortcut(target=target, path=path, wDir=wDir, icon=icon)
                            print('Update: Dumping shortcut path...')

                            # run
                            if self.rules['env'] == 'run':
                                f = open(f'{self.setup_wDir}/data.json', 'r')

                            # - for codespace
                            else:
                                f = open('main/setup/data.json', 'r')

                            temp = json.load(f)
                            temp['abs_shortcut'] = self.abs_shortcut
                            f.close()

                            # run
                            if self.rules['env'] == 'run':
                                f = open(f'{self.setup_wDir}/data.json', 'w')

                            # - for codespace
                            else:
                                f = open('main/setup/data.json', 'w')
                                
                            json.dump(temp, f)
                            f.close()
                                
                        else:
                            pass

                    except Exception as e:
                        print(f'!!! Error creating shortcut: {e}')

                except Exception as e:
                    print(f'!!! Error while downloading: {e}')
                    #print('Cleaning up then exiting...')
                    #self.pre_clean('error')
                    #sys.exit()

            except Exception as e:
                print(f'!!! Error while creating object: {e}')
                #print('Consider re-entering branch name / github url')
                #print('Cleaning up then exiting...')
                #self.pre_clean('error')
                #sys.exit()    
            self.end = timeit.default_timer()     


        # doing file cleanup
        def post_clean(self):
            print('---------------')
            print('Post: Cleaning up')
            print('Post: Deleting extra files...')

            # remove setup folder
            if self.rules['env'] == 'run':
                shutil.rtmree(f'{self.install_path}/setup')
                os.remove(f'{self.install_path}/top/content_url.txt')

            else:
                print('Individual cleanup is not offered for this mode. Use mode run instead')

            print('Post: Extra files deleted.')

            ## to delete setup folder if needed (not used)
            #shutil.rmtree(f'{self.install_path}/main/setup')

            #shutil.rmtree('./temp/')
            print('Post: Note: If directory is not present, or is empty, check your inputs and run again.')
            print('Post: Done cleaning; continuing...')


        # quits install file (to make sure it goes right)
        def quit_install(self):
            print('---------------')
            if not self.desktop_shortcut:
                print(f'Since you did not choose to have a shortcut, the file to run is located in: ')
                print(f'- {self.install_path}/everything/main/setup/fiesta.exe')
                print('---------------')
            input(f'Install complete! Time: {round(self.end - self.start, 2)}s \nEnter anything to exit: ')
            #print('Install complete. Exit in:')
            #for i in range(3, 0, -1):
            #    print(f'{i}')
            #    time.sleep(1)

            # ensure an exit happens
            sys.exit()

        # more of an assurance honestly, but eh
        def edit_data(self):
            print('---------------')
            print('Update: Updating installed data.json...')
            f = open(f'{self.install_path}/everything/main/setup/data.json', 'r')
            content = json.load(f)
            f.close()
            content['shortcut'] = True
            content['update'] =  False
            content['bounds'] = 'x'
            f = open(f'{self.install_path}/everything/main/setup/data.json', 'w')
            json.dump(content, f)
            f.close()
            print('Update: Installed data.json updated.')

            print('Update: Updating installed state.json...')
            f = open(f'{self.install_path}/everything/main/setup/state.json', 'w')
            json.dump(False, f)
            f.close()
            print('Update: Installed state.json updated.')

            print('Update: Updating installed version.json...')
            f = open(f'{self.install_path}/everything/main/top/container/version.json', 'w')
            json.dump(self.release_version, f)
            f.close()
            print('Update: Installed version.json updated.')





        # runs all the functions in order, by config rules (can be changed in config.json)
        def run(self):

            if self.rules['safety_check']: self.safety_check()
            if self.rules['pre_clean']: self.pre_clean()
            if self.rules['setup']: self.setup()
            if self.rules['create']: self.create()
            if self.rules['download']: self.download()
            if self.rules['post_clean']: self.post_clean()
            if self.rules['edit_data']: self.edit_data()
            if self.rules['quit_install']: self.quit_install()


    ## ONLY TWO ACTING LINES OF CODE
    # initializes Install class
    # and also runs all of the code
    install = Install()
    install.run()

# in the event of an error, this logs that error
# in a file and crashes gracefully
except Exception as e:
    import os
    import traceback
    import setup_crash_handler
    setup_crash_handler.Crash_handler(
        error = traceback.format_exc()
    )