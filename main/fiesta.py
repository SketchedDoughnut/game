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
# change setup to start to run as normal
# in case .json contents are lost

{
    "mode": "setup", 
    
    "py_version": "",
    "repo_url": "",
    "repo_branch": "",

    "shortcut_path": "",
    "shortcut_target": "",
    "shortcut_wDir": "",
    "shortcut_icon": ""
}

'''
########################################################################

# main install class
class Install:

    # init
    def __init__(self):

        # read setup.json for setup and get info
        
        # - for codespace
        #self.read_setup = open('main/setup.json', 'r')

        # for run
        self.read_setup = open('setup.json', 'r')

        self.read_setup_value = json.load(self.read_setup)

        # establish all variables 
        if self.read_setup_value['mode'] == 'setup':
            
            # print start message
            print("""--------------------------------------------------------------------------
Welcome to the installation agent designed by (placeholder)!
This installer will run you through the steps required to set up, and then use the installer. 
It is coded in python and compiled with pyinstaller. This enables you to install and run python files.
For this program, y/n will be the responses the program will take from you. 
--------------------------------------------------------------------------
Here is the rundown on the files included with this installer:
    ALL .JSON
        - config.json: 
            - Allows you to change which functions from the file will run (true/false values)
        
        - delete.json: 
            - A file used by delete.py 
                  
        - setup.json:
            - A file used by the installer when setting up; necessary for info.
    
    FOLDERS
        - _internal:
            - Files necessary for this installer to run. Do not interfere with those files.
                  
        - _example:
            - An example of how things should generally look when done.
                  
    OTHER FILES
        - delete.py:
            - is used when user wishes to un-install installed files.
                  
        - help.txt:
            - helps with installation; will be removed at the end.


Here is the rundown on how the installer will work, user-side:
                  
    - Gets file directory for installation, and formats. (__init__)
    - After confirmation, deletes everything previously installed by the installer to then re-install. (safety_check, pre_clean)
    - Asks if you want a shortcut created, and makes sure you have python installed. (setup)
    - Creates directory for game folder within inputted file directory done at step 1, and writes that path into delete.json. (create)
    - Downloads files from an inputted github link, and optionally a branch of said repository (download)
        - NOTE: Some respositories have had issues with getting code grabbed from them; cause: unknown.
    - Cleans up any temporary files afterwards. (post_clean)
    - Finishes up then quits install after a set time. (quit_install)
                  
You can configure which of the above run in config.json.
                  
There a variety of other safety checks and functions within, such as "time.sleep()" being used multiple times. 
These values unfortunately can not be changed. They have been optimized for a smooth experience, however.
--------------------------------------------------------------------------""")
            if input('When ready, type "y": ').lower() == 'y':
                input_loop = True
                while input_loop == True:
                    print('--------------------------------------------------------------------------')
                    print("""We will now proceed into setup.
    in order to run, extensive data must be inputted by you for this to work.
    To follow along with, check "example.txt" for further elaboration on each step.
    Also, an example has been installed to compare against.""")
                    print('--------------------------------------------------------------------------')

                    print('DOWNLOADING: ')
                    self.py_version = input('- What is Python version you want them to install? (Ex: 3.9) \n--> ')
                    self.repo_url = input('- Input a link to the PUBLIC github repository for install \n--> ')
                    #self.repo_branch = input('- Input the name of the repository branch for install \n--> ')

                    print("\nSHORTCUT: ")
                    self.shortcut_path = input('- Input the name you want for your shortcut \n--> ')
                    self.shortcut_target = input('- Input the path to your intended file to execute \n--> ')
                    self.shortcut_wDir = input('- Input the folder that your intended file to execute is in \n--> ')
                    self.shortcut_icon = self.shortcut_target
                    print('--------------------------------------------------------------------------')
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
                    
                    if input('If everything is right, type "y". Otherwise, type "n" to re-enter info: \n--> ').lower() == 'y':
                        input_loop = False
                
                # loop over, format dict and dump
                print('Setting up dictionary...')

                # - for codespace
                #self.read_setup = open('main/setup.json', 'w')

                # for run
                self.read_setup = open('setup.json', 'r')

                # dumping data
                # downloading
                self.read_setup_value['py_version'] = self.py_version
                self.read_setup_value['repo_url'] = self.repo_url
                #self.read_setup_value['repo_branch'] = self.repo_branch
                self.read_setup_value['repo_branch'] = 'x'

                # shortcut
                self.read_setup_value['shortcut_path'] = self.shortcut_path
                self.read_setup_value['shortcut_target'] = self.shortcut_target
                self.read_setup_value['shortcut_wDir'] = self.shortcut_wDir
                self.read_setup_value['shortcut_icon'] = self.shortcut_icon 
                
                # finished dict
                print('Dictionary done: ')
                print(self.read_setup_value)

                # dumping into .json
                print('Dumping into setup.json')
                self.temp = json.dump(self.read_setup_value, self.read_setup)
                print('Dump done.')


                print("""-------------------------------------------------------------------------
This file will now attempt a test installation using the information given. However, if you are confident in this then type "skip" to skip.
Enter "y" to start test installation.""")

                run_test_install = input('--> ').lower()
                if run_test_install == 'y':
                    print('Running test installation. A temporary directory will be created named "temp-inst".')
                    print('-------------------------------------------------------------------------')
                    
                    # - for codespace
                    #main_path = 'main/temp-inst'
                    #os.mkdir(main_path)

                    # for run
                    main_path = '/temp-inst'
                    os.mkdir(main_path)

                    downloader = Downloader()
                    downloader.load_repository(url=self.repo_url)
                    downloader.download(main_path, "*", True)
                    print('-------------------------------------------------------------------------')
                    print('Installation is done. Creating shortcut.')
                    print('-------------------------------------------------------------------------')
                    try:
                        import winshell
                        desktop = winshell.desktop()
                        path = os.path.join(desktop, self.shortcut_path) # CHANGE game_name TO NAME
                        target = self.shortcut_target
                        wDir = self.shortcut_wDir
                        icon = self.shortcut_icon

                        # calls on function here with data from above
                        self.createShortcut(target=target, path=path, wDir=wDir, icon=icon)

                    except:
                        print('Shortcut error; run file individually not through an interpreter')
                    print('-------------------------------------------------------------------------')
                    print('Shortcut created. The following should be installed: ')
                    print('installation at: /temp-inst')
                    print(f'shortcut on desktop named: {self.shortcut_path}')
                    print('-------------------------------------------------------------------------')
                    input('Enter anything to proceed to cleanup: ')
                    print('Cleaning up installating at /temp-inst...')
                    shutil.rmtree(main_path)
                    print('Cleanup done; continuing')


                elif run_test_install == 'skip':
                    print('Skipping test installation.')
            
            print('--------------------------------------------------------------------------')
            print('Your installer should now be configured to install your programs,')
            print('and also create a shortcut to run your program.')
            print('-------------------------------------------------------------------------')
            #print('File cleanup is next: files in question being (_example/) and (help.txt).')
            #input('Enter anything to authorize cleanup: ')
            print('Installer complete! To finish up, this installer will change "mode" in setup.json to install and quit. Change  it to "setup" to redo this after this point.')
            print("""NOTE: You only need the following files:
    - setup.json
    - config.json
    - delete.json
    - delete.py
    - this installer
    - _internal""")
            self.read_setup_value['mode'] == 'install'
            print('-------------------------------------------------------------------------')
            print('Changed mode to install.')
            print('-------------------------------------------------------------------------')
            print('Exiting in 30s...')
            for i in range(30, 0, -1):
                print(i)
                time.sleep(1)
            exit()

                

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









Install = Install()