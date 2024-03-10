### imports
# builtin
import os
import time
import shutil

# external(?)
import json
import requests
import urllib.request
########################################################################
'''
# change setup to install to run as normal
# in case .json contents are lost

{
    "mode": "setup", 

    "py_use": false, 
    "py_version": 0, 

    "repo_url": "", 
    "repo_branch": "", 

    "shortcut_path": "", 
    "shortcut_target": "", 
    "shortcut_wDir": "", 
    "shortcut_icon": "",
    
    "remove_path": ""
}

'''
########################################################################

# main install class
class Install:

    # init
    def __init__(self, mode=0):

        # read setup.json for setup and get info
        
        # - for codespace
        #self.read_setup = open('main/setup.json', 'r')

        # for run
        self.read_setup = open('setup.json', 'r')

        self.read_setup_value = json.load(self.read_setup)

        self.read_setup.close()

        # establish all variables 
        if self.read_setup_value['mode'] == 'setup':
            
            # print start message
            print("""--------------------------------------------------------------------------
Welcome to the installation agent designed by Sketched Doughnut!
This installer will run you through the steps required to set up, and then your installer is ready to go! 
It is coded in python and compiled with pyinstaller. This enables you to install and run python files. 

Information about the files and steps to follow along can be found in "help.txt", and it is heavily encouraged you
have that open while using this installer for reference.""")
            print('--------------------------------------------------------------------------')
            input('Enter anything to continue: ')
            print("""--------------------------------------------------------------------------
GENERAL INFO

                  
Here is the rundown on how the installer will work, user-side:
                  
    - Gets file directory for installation, and formats. 
        - (__init__)
                  
    - After confirmation, deletes everything previously installed by the installer to then re-install. 
        - (safety_check)
        - (pre_clean)
                  
    - Asks if you want a shortcut created, and makes sure you have python installed. 
        - (setup)
                  
    - Creates directory for main folder within inputted file directory done at step 1, and writes that path into setup.json. 
        - (create)
                  
    - Downloads files from an inputted github link, and optionally a branch of said repository 
        - (download)
                  
        - NOTE: Some respositories have had issues with getting code downloaded from them. Cause: unknown.
    - Cleans up any temporary files afterwards. 
        - (post_clean)
                  
    - Finishes up then quits install after a set time. 
        - (quit_install)

                  
Refer to "help.txt" for configuring these functions.
                  
There a variety of other safety checks and functions within, such as "time.sleep()" being used multiple times. 
These values unfortunately can not be changed. They have been optimized for a smooth experience, however.
--------------------------------------------------------------------------""")
            input('Enter anything to continue: ')
            input_loop = True
            while input_loop == True:
                print('--------------------------------------------------------------------------')
                print("""SETUP
                      
We will now proceed into setup.
in order to run, info must be inputted by you for this to work.
To follow along, please check "help.txt" for further elaboration on each step.
Also, an example folder has been installed to refer to, named "_example/" (check "help.txt" to know more about "_example/").""")
                print('--------------------------------------------------------------------------')

                print('DOWNLOADING: ')
                self.py_use = input('- Does this file involve any python files? (y/n): \n--> ').lower() == 'y'
                if self.py_use == True:
                    self.py_version = input('   - What is Python version you want them to install? (Ex: 3.9) \n     --> ')
                else:
                    self.py_version = 0
                self.repo_url = input('\n- Input a link to the PUBLIC github repository for install \n--> ')
                #self.repo_branch = input('- Input the name of the repository branch for install \n--> ')

                print("\nSHORTCUT: ")
                self.shortcut_path = input('- Input the name you want for your shortcut \n--> ')
                self.shortcut_target = input('\n- Input the path to your intended file to execute \n- Note: Path from "main/" to where your installed files will be located (refer to "help.txt") \n--> ')
                self.shortcut_wDir = input('\n- Input the folder that your intended file to execute is in \n- Note: if file is in root, enter nothing here \n--> ')
                self.shortcut_icon = self.shortcut_target
                print('--------------------------------------------------------------------------')
                #if self.shortcut_wDir == " ":
                #    self.shortcut_wDir = 
                print('Here is a current data sheet of what has been inputted: ')
                print(f"""--------------------------------------------------------------------------
DOWNLOADING
    - python version: {self.py_version}
    - repository url: {self.repo_url}

SHORTCUT
    - shortcut name: {self.shortcut_path}
    - shortcut target file: {self.shortcut_target}
    - shortcut directory of target: {self.shortcut_wDir}
    - shortcut icon: {self.shortcut_icon}
-------------------------------------------------------------------------""")
# - repository branch: {self.repo_branch}
                print('Compare these results with the example in "help.txt".')
                if input('If everything is right, type "y". Otherwise, type "n" to re-enter info: \n--> ').lower() == 'y':
                    input_loop = False
            
            # loop over, format dict and dump
            print('Setting up dictionary...')

            # - for codespace
            #self.read_setup = open('main/setup.json', 'w')

            # for run
            self.read_setup = open('setup.json', 'w')

            # dumping data
            # downloading
            self.read_setup_value['py_version'] = self.py_version
            self.read_setup_value['repo_url'] = self.repo_url
            #self.read_setup_value['repo_branch'] = self.repo_branch
            #self.read_setup_value['repo_branch'] = 'x'

            # shortcut
            self.read_setup_value['shortcut_path'] = self.shortcut_path
            self.read_setup_value['shortcut_target'] = self.shortcut_target
            self.read_setup_value['shortcut_wDir'] = self.shortcut_wDir
            self.read_setup_value['shortcut_icon'] = self.shortcut_icon 
            self.read_setup_value['py_use'] = self.py_use
            
            # finished dict
            print('Dictionary done.')
            #print(self.read_setup_value)

            # dumping into .json
            print('Dumping into setup.json...')
            self.temp = json.dump(self.read_setup_value, self.read_setup)
            self.read_setup.close()
            print('Dump done.')

            input('Enter anything to continue: ')
            print("""-------------------------------------------------------------------------
This file will now attempt a test installation using the information given. However, if you are confident in this then type "skip" to skip.
Enter "y" to start test installation.""")

            run_test_install = input('--> ').lower()
            if run_test_install == 'y':
                print('Running test installation. A temporary directory will be created named "_temp-inst/".')
                print('In actual installation, this will be "main".')
                print('-------------------------------------------------------------------------')
                
                # - for codespace
                # self.main_path = 'main/main'
                # os.mkdir(self.main_path)

                # for run
                self.main_path = 'main'
                os.mkdir(self.main_path)

                try:
                    downloader = Downloader()
                    downloader.load_repository(url=self.repo_url)
                    downloader.download(self.main_path)
                    print('-------------------------------------------------------------------------')
                    print('Installation is done. Creating shortcut.')

                except Exception as e:
                    print(f'Download error: {e}')
                    print('Cleaning up failed install...')
                    try:
                        shutil.rmtree(self.main_path)
                    except:
                        print('Directory deletion fail...')
                    print('The file will now quit. Restart it and input a new github url, or fix the current one.')
                    print('Repository must be PUBLIC. Due to an currently unknown error some PUBLIC URLs do not allow downloads from them.')
                    for i in range(30, 0, -1):
                        print(i)
                        time.sleep(1)
                    exit()
    
                try:
                    import winshell
                    desktop = winshell.desktop()
                    
                    # make shortcut adapt for installation

                    path = os.path.join(desktop, f'{self.shortcut_path}.lnk') # name
                    target = f'{self.main_path}/{self.shortcut_target}' # file to execute
                    wDir = self.shortcut_wDir # directory of file to execute 
                    icon = self.shortcut_icon # same as target

                    # calls on function here with data from above
                    self.createShortcut(target=target, path=path, wDir=wDir, icon=icon)
                    print('-------------------------------------------------------------------------')
                    print('Shortcut created.')

                except Exception as e:
                    print(f'Shortcut error: {e}')

                print('-------------------------------------------------------------------------')
                print('The following should be installed (unless error occured): ')
                print('installation at: main/')
                print(f'shortcut on desktop at: {self.shortcut_path}')
                print('-------------------------------------------------------------------------')
                input('Enter anything to proceed to cleanup: ')
                print('Cleaning up installation at main/...')
                shutil.rmtree(self.main_path)
                print('Cleanup done; continuing')


            elif run_test_install == 'skip':
                print('Skipping test installation.')
        
            input('Enter anything to continue: ')
            print('--------------------------------------------------------------------------')
            print('Your installer should now be configured to install your programs,')
            print('and also create a shortcut to run your program.')
            print('-------------------------------------------------------------------------')
            print(f"""Total information gathered throughout this process (all self):

PATH(S)
- {self.main_path}

PY
- {self.py_version}
- {self.py_use}

SETUP DICT
- {self.read_setup_value}

REPO URL
- {self.repo_url}

SHORTCUT INFO: name, icon, wDir, target
- {self.shortcut_path}
- {self.shortcut_icon}
- {self.shortcut_wDir}
- {self.shortcut_target}

OTHER: 
- {self.read_setup}
- {self.temp}

""")
            input('Enter anything to continue: ')
            print('-------------------------------------------------------------------------')
            #print('File cleanup is next: files in question being (_example/) and (help.txt).')
            #input('Enter anything to authorize cleanup: ')
            print('Installer complete! To finish up, this installer will change "mode" in "setup.json" to "install" and quit.')
            print('Change it to "setup" to redo this after this point.')
            print("""NOTE: You only need the following files:
    - setup.json
    - config.json
    - delete.py
    - this installer
    - _internal""")
            print('-------------------------------------------------------------------------')
            self.read_setup_value['mode'] = 'install'

            # - for codespace
            #self.read_setup = open('main/setup.json', 'w')

            # for run
            self.read_setup = open('setup.json', 'w')
            
            json.dump(self.read_setup_value, self.read_setup)
            self.read_setup.close()
            print('Changed mode to install.')
            print('-------------------------------------------------------------------------')
            print('Exiting in 30s...')
            for i in range(30, 0, -1):
                print(i)
                time.sleep(1)
            exit()























        if self.read_setup_value['mode'] == 'install':
            # assigning vars (local)
            new_string = ''
            rules_list = []

            # check if .json is all false
            ## for codespace
            # try:
            #     f = open('config.json', 'r')

            # except:
            #     try:
            #         f = open('main/config.json', 'r')

            #     except Exception as e:
            #         print(f'error: {e}')
            #         print('vsc handling: exiting')
            #         time.sleep(5)
            #         exit()

            # - for codespace
            #f = open('main/config.json', 'r')

            # for run
            f = open('config.json', 'r')

            rules = json.load(f)
            f.close()

            # iterate through rules dictionary and check for and True
            for key in rules:
                if rules[key] == False:
                    rules_list.append(False)

                else:
                    rules_list.append(True)

                if rules_list.count(True) > 0:
                    pass

                # exit if no True
                else:
                    print('---------------')
                    print('Running no files; cancelling in 5s')
                    print('---------------')
                    time.sleep(5)
                    exit()


            # establishing all contents from setup.json

            # - for codespace
            #self.read_setup = open('main/setup.json', 'r')

            # for run
            self.read_setup = open('setup.json', 'r')

            self.read_setup_value = json.load(self.read_setup)
            self.read_setup.close()

            self.py_version = self.read_setup_value['py_version']
            self.repo_url = self.read_setup_value['repo_url']
            self.shortcut_path = self.read_setup_value['shortcut_path']
            self.shortcut_target = self.read_setup_value['shortcut_target']
            self.shortcut_wDir = self.read_setup_value['shortcut_wDir']
            self.py_use = self.read_setup_value['py_use']
            self.shortcut_icon = self.shortcut_target
            
            # printing start statement, format, prompting
            print("""
            Welcome to the open-source file installer created by Sketched Doughnut! 
                Code is written by Sketched Doughnut with snippets from others.
                Sources are in: (install location)/gitignore/sources.txt.   
        To change config, change values in "config.json", then restart this installer.
                    To configure your own installer, install it at: (url)
            """)
            print('---------------')
            print('Input file directory for install below (or type "delete" to delete").')
            print('Note: Must be absolute path. Ex: C:\\install_location')
            self.install_path = input('--> ')

            # checking for uninstall, doing uninstall if so
            if self.install_path == "delete":
                print('---------------')
                if input('Are you sure you want to delete?  \nType: "confirm-delete", anything else to cancel \n--> ') == 'confirm-delete':

                    # opening delete.json and getting path

                    # - for codespace
                    #temp = open('main/setup.json', 'r')

                    # for run
                    temp = open('setup.json', 'r')

                    delete_path = json.load(temp)
                    delete_path = delete_path["remove_path"]
                    temp.close()
                    print('---------------')
                    print(f'Un-installing main from the following directory: {delete_path}')

                    # runs delete file
                    ## for codespace
                    # try:
                    #     os.system(f'python delete.py')
                    # except:
                    #     try:
                    #         os.system(f'python main/delete.py')
                    #     except Exception as e:
                    #         print(f'error: {e}')
                    #         print('vsc handling: exiting')
                    #         time.sleep(5)
                    #         exit()

                    # - for codespace
                    #os.system(f'python main/setup.py')
                            
                    ## for run
                    os.system(f'python delete.py')
                            

                    # final, then finishes
                    print('---------------')
                    print('NOTE: Shortcut will not be deleted.')
                    print('Delete done. This installer will exit in 20 seconds; afterwards, delete the folder it is in.')
                    print('Thank you for using this installer! :3')
                    for i in range(20, 0, -1):
                        print(i)
                        time.sleep(1)
                    exit()
                
                else:
                    print('Cancelling deletion, cancelling file in 5s...')
                    for i in range(5, 0, -1):
                        print(i)
                        time.sleep(1)
                    exit()

            else:

                # getting path, formatting
                #if self.install_path != "":
                list = [str(i) for i in self.install_path]
                for i in list:
                    if i == '\\':
                        new_string += '/'
                    else:
                        new_string += i
                self.install_path = new_string
                self.install_path = [str(i) for i in self.install_path]
                if self.install_path[len(self.install_path) - 1] == '/':
                    #self.install_path += '/'
                    self.install_path.pop(len(self.install_path) - 1)
                else:
                    pass
                new_string = ''
                for i in self.install_path:
                    new_string += i
                self.install_path = new_string
                self.install_path += '/main'
                print('---------------')
                print(self.install_path)
                #else:
                    #print('---------------')
                    #self.install_path += '/main'
                    #print(self.install_path)

        # return self.install_path
        elif mode == 1:
            #self.install_path = self.install_path
            return self.install_path


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
        else:
            print('Cancelling...')
            time.sleep(2)
            exit()


    # cleaning before any running
    def pre_clean(self, run_error=''):
        if run_error == 'error':
        #    try:
        #        shutil.rmtree(self.temp_path)
        #    except:
        #        print('no temp')
        
            # removing install tree
            try:
                shutil.rmtree(self.install_path)
                print(f'! install cleaned')
            except:
                print(f'! no install')

        else:
            print('Pre: Cleaning up directories before install')

            ## removing temp tree
            #try:
            #    shutil.rmtree(self.temp_path)
            #except:
            #    print('no temp')
            
            # removing install tree
            try:
                shutil.rmtree(self.install_path)
                print(f'! install cleaned')
            except:
                print(f'! no install')

            print('Pre: Done cleaning; continuing...')
            time.sleep(1)
            print('---------------')

    
    ## getting info
    def setup(self):
        # getting inputs
    #    ## https://github.com/BirdLogics/sb3topy
    #    self.url = input('Input repository URL: ')
    #    self.branch = input('Input respository branch: ')
        self.desktop_shortcut = (input('Do you want to add a desktop shortcut? (y/n) \n--> ').lower()) == 'y'
        
        # make sure they have python installed
        print('---------------')
        if self.py_use == True:
            print(f"""
                     Before we proceed, you need to have an installation of python installed.
              If you already have one, type "y" to proceed. If you don't, do the following instructions:
              - go to Microsoft Store
              - search "Python {self.py_version}"
              - Install
              - You're done!
                        Once done doing these instructions, type 'y' (anything else to cancel).
              """)
            if input('--> ').lower() != 'y':
                exit()
            else:
                print('---------------')
        
        else:
            print('---------------')


    # create temp dir and establish code file
    def create(self):

        # creating directories
        print(f'Creating directory: {self.install_path}')
        os.mkdir(self.install_path)

        # opening delete file and writing path
        ## for codespace
        #try:
            #rules = open('delete.json', 'r')

        #except:
        #    try:
        #    rules = open('main/delete.json', 'r')
        
        #    except Exception as e:
        #        print(f'error: {e}')
        #        print('vsc handling: exiting')
        #        time.sleep(5)
        #        exit()
        
        # - for codespace
        #rules = open('main/setup.json', 'r')

        # for run
        rules = open('setup.json', 'r')

        rules_content = json.load(rules)
        rules.close()
        rules_content["remove_path"] = self.install_path

        # - for codespace
        #rules = open('main/setup.json', 'w')

        # for run
        rules = open('setup.json', 'w')

        json.dump(rules_content, rules)
        rules.close()


        # function to download incorporating class: https://github.com/fbunaren/GitHubFolderDownloader
    def download(self):

        # initializing the downloader class
        # NOTE: Alternatively, initialize .Downloader empty and instead do load repository with url
        # NOTE: Do this because you can link branch in that url and it will identify it
        # NOTE: .download still runs the same
        try:
            downloader = Downloader(self.repo_url)

            # downloading
            try:
                downloader.download(self.install_path)

                # writing run path to text file (not used, not up to date)
                # try:
                #     print('Assembling text file')
                #     url_path = f'{self.install_path}/main/top-level/content_url.txt'
                #     f = open(url_path, 'w')
                #     f.write(f'{self.install_path}/main/top-level/game_data/main.py')
                #     f.close()

                # except Exception as e:
                #     print(f'!!! Error with text file: {e}')

                # formats info and runs shortcut making function
                try:
                    if self.desktop_shortcut == True:
                        #print('---------------')
                        import winshell
                        print('Creating shortcut')
                        desktop = winshell.desktop()
                        path = os.path.join(desktop, f'{self.shortcut_path}.lnk')
                        target = f'{self.install_path}/{self.shortcut_target}'
                        wDir = self.shortcut_wDir
                        icon = self.shortcut_icon

                        # calls on function here with data from above
                        self.createShortcut(target=target, path=path, wDir=wDir, icon=icon)

                    else:
                        pass

                except Exception as e:
                    print(f'Error creating shortcut: {e}')

            except Exception as e:
                print(f'!!! Error while downloading: {e}')
                #print('Cleaning up then exiting...')
                #self.pre_clean('error')
                #exit()

        except Exception as e:
            print(f'!!! Error while creating object: {e}')
            #print('Consider re-entering branch name / github url')
            #print('Cleaning up then exiting...')
            #self.pre_clean('error')
            #exit()         


    # doing file cleanup
    def post_clean(self):
        print('---------------')
        print('Post: Cleaning up')

        ## to delete setup folder if needed (not used)
        #shutil.rmtree(f'{self.install_path}/main/setup')

        #shutil.rmtree('./temp/')
        print('Note: If directory is not present, or is empty, check your inputs and run again.')
        print('Post: Done cleaning; continuing...')


    # quits install file (to make sure it goes right)
    def quit_install(self):
        print('---------------')
        print('Install complete. Exit in:')
        for i in range(3, 0, -1):
            print(f'{i}')
            time.sleep(1)

        # ensure an exit happens
        exit()


    # runs all the functions in order, by config rules (can be changed in config.json)
    def run(self):
        rules = {}

        ## for codespace
        # try:
            # f = open('config.json', 'r')
        # except:
            # try:
                # f = open('main/config.json', 'r')
            # except Exception as e:
                # print(f'error: {e}')
                # print('vsc handling: exiting')
                # time.sleep(5)
                # exit()

        # - for codespace
        #f = open('main/config.json', 'r')

        # for run
        f = open('config.json', 'r')

        rules = json.load(f)
        f.close()

        if rules['safety_check'] == True: self.safety_check()
        if rules['pre_clean'] == True: self.pre_clean()
        if rules['setup'] == True: self.setup()
        if rules['create'] == True: self.create()
        if rules['download'] == True: self.download()
        if rules['post_clean'] == True: self.post_clean()
        if rules['quit_install'] == True: self.quit_install()



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


#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
GitHub Folder Downloader
Created by Fransiscus Emmanuel Bunaren
https://bunaren.com
'''

class Downloader:

    def __init__(self, repository_url='', branch=''):
        if not repository_url:
            self.repo_url = ''
            self.files = []
            self.location = dict()
        else:
            self.load_repository(repository_url, branch)

    @classmethod
    def __get_branch_from_url(self, url, branch=''):
        if '/tree/' in url and not branch:
            branch = url.split('/tree/')[1]
            branch = branch.split('/')[0]
        else:
            branch = 'master'
        return branch

    @classmethod
    def __get_raw_url(self, file_path, url, branch=''):
        tmp_url = url.replace(
            'https://api.github.com/repos/',
            'https://raw.githubusercontent.com/')
        tmp_url = tmp_url.split('/git/blobs/')[0]
        tmp_url = tmp_url + '/' + branch + '/' + file_path
        return tmp_url

    def load_repository(self, url, branch=''):

        # Check if URL contains branch name

        branch = self.__get_branch_from_url(url, branch)

        # Convert URL to match GitHub API URI

        tmp_url = url.replace('https://github.com/',
                            'https://api.github.com/repos/')
        tmp_url += '/git/trees/{}?recursive=1'.format(branch)

        # Make GET Request

        api = requests.get(tmp_url).text
        files = json.loads(api)

        # Turn the API Data into List

        output = []
        location = dict()
        for (k, i) in enumerate(files['tree']):
            if i['type'] == 'blob':
                tmp = [i['path']]

                # Get RAW URL

                tmp += [self.__get_raw_url(tmp[0], i['url'], branch)]
                output.append(tmp)
            else:
                location[i['path']] = k
        self.files = output
        self.location = location

        # Set Repo URL for memoization

        self.repo_url = url

    def __mkdirs(self, path):

        # Make directory if not exist

        if not os.path.isdir(path):
            os.makedirs(path)

    def download(
        self,
        destination,
        target_folder='*',
        recursive=True,
    ):

        # Make directory if not exist

        self.__mkdirs(destination)

        # Find Folder Position

        if target_folder == '*':
            start = 0
        else:

            # Remove Relative Path Symbol from string

            tmp_target = target_folder.replace('./', '')
            tmp_target = tmp_target.replace('../', '')

            # Remove "/"

            tmp_target = (tmp_target if tmp_target[-1] != '/'
                        else tmp_target[:-1])
            start = self.location[target_folder]

        # Start Downloading

        for i in self.files[start:]:
            if recursive or i[0].split(target_folder)[1].count('/') \
                    <= 1:
                self.__mkdirs(destination + '/' + os.path.dirname(i[0]))
                urllib.request.urlretrieve(i[1], destination + '/' + i[0])

                # modified segment by me
                print(f'Installing file: /{i}')









install = Install()
install.run()