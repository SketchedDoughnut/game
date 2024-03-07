# importing builtin
import os
import time
import shutil

# downloader imports
import json
import requests
import urllib.request


########################################################################


class Install:
    # init
    def __init__(self, mode=0):

        # default
        if mode == 0: 

            # assigning vars (local)
            new_string = ''
            rules_list = []

            # check if .json is all false
            ## for codespace
            try:
                f = open('config.json', 'r')
            except:
                try:
                    f = open('main/setup/config.json', 'r')
                except Exception as e:
                    print(f'error: {e}')
                    print('vsc handling: exiting')
                    time.sleep(5)
                    exit()

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
            
            # printing start statement, format, prompting
            print("""
            Welcome to the open-source file installer created by (placeholder)! 
                Code is written by (placeholder) with snippets from others.
                Sources are in: (install location)/gitignore/sources.txt.   
    To change config, change values in "config.json", then restart this installer.
            """)
            print('---------------')
            print('Input file directory for install below (or type "un-install" to uninstall").')
            print('Note: Must be absolute path. Ex: C:\\install_location')
            self.install_path = input('--> ')

            # checking for uninstall, doing uninstall if so
            if self.install_path == "un-install":
                print('---------------')
                if input('Are you sure? (y/n): ') == 'y':

                    # opening delete.json and getting path
                    temp = open('main/setup/delete.json', 'r')
                    delete_path = json.load(temp)
                    delete_path = delete_path["remove_path"]
                    temp.close()
                    print('---------------')
                    print(f'Un-installing game from the following directory: {delete_path}')

                    # runs delete file
                    ## for codespace
                    try:
                        os.system(f'python delete.py')
                    except:
                        try:
                            os.system(f'python main/setup/delete.py')
                        except Exception as e:
                            print(f'error: {e}')
                            print('vsc handling: exiting')
                            time.sleep(5)
                            exit()

                    # final, then finishes
                    print('---------------')
                    print('NOTE: Shortcut will note be deleted.')
                    print('Delete done. This installer will exit in 20 seconds; afterwards, delete the folder it is in. Thank you for using this installer! :3')
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
                self.install_path += '/game_name'
                print('---------------')
                print(self.install_path)
                #else:
                    #print('---------------')
                    #self.install_path += '/game_name'
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
        print("""
                     Before we proceed, you need to have an installation of python installed.
              If you already have one, type "y" to proceed. If you don't, do the following instructions:
              - go to Microsoft Store
              - search "Python 3.9"
              - Install
              - You're done!
                        Once done doing these instructions, type 'y' (anything else to cancel).
              """)
        if input('--> ').lower() != 'y':
            exit()
        else:
            print('---------------')


    # create temp dir and establish code file
    def create(self):

        # creating directories
        print(f'Creating directory: {self.install_path}')
        os.mkdir(self.install_path)

        # opening delete file and writing path
        ## for codespace
        try:
            rules = open('delete.json', 'r')
        except:
            try:
                rules = open('main/setup/delete.json', 'r')
            except Exception as e:
                print(f'error: {e}')
                print('vsc handling: exiting')
                time.sleep(5)
                exit()
                
        rules_content = json.load(rules)
        rules.close()
        rules_content["remove_path"] = self.install_path
        rules = open('main/setup/delete.json', 'w')
        #rules = open('delete.json', 'w')
        json.dump(rules_content, rules)
        rules.close()


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

        # initializing the downloader class
        # NOTE: Alternatively, initialize .Downloader empty and instead do load repository with url
        # NOTE: Do this because you can link branch in that url and it will identify it
        # NOTE: .download still runs the same
        try:
            downloader = Downloader("https://github.com/SketchedDoughnut/development")

            # downloading
            try:
                downloader.download(self.install_path)

                # writing run path to text file (not used, not up to date)
                try:
                    print('Assembling text file')
                    url_path = f'{self.install_path}/main/top-level/content_url.txt'
                    f = open(url_path, 'w')
                    f.write(f'{self.install_path}/main/top-level/game_data/main.py')
                    f.close()

                except Exception as e:
                    print(f'!!! Error with text file: {e}')

                # formats info and runs shortcut making function
                try:
                    if self.desktop_shortcut == True:
                        #print('---------------')
                        import winshell
                        print('Creating shortcut')
                        desktop = winshell.desktop()
                        path = os.path.join(desktop, "game_name.lnk") # CHANGE game_name TO NAME
                        target = f"{self.install_path}/main/top-level/starter.exe" # CHANGE TO EXE
                        wDir = f"{self.install_path}/main/top-level"
                        icon = f"{self.install_path}/main/top-level/starter.exe" # CHANGE TO EXE

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
        try:
            f = open('config.json', 'r')
        except:
            try:
                f = open('main/setup/config.json', 'r')
            except Exception as e:
                print(f'error: {e}')
                print('vsc handling: exiting')
                time.sleep(5)
                exit()

        rules = json.load(f)
        f.close()

        if rules['safety_check'] == True: self.safety_check()
        if rules['pre_clean'] == True: self.pre_clean()
        if rules['setup'] == True: self.setup()
        if rules['create'] == True: self.create()
        if rules['download'] == True: self.download()
        if rules['post_clean'] == True: self.post_clean()
        if rules['quit_install'] == True: self.quit_install()


########################################################################
########################################################################
########################################################################
    
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


########################################################################
########################################################################
########################################################################

########################################################################


## ONLY TWO ACTING LINES OF CODE
# initializes Install class
install = Install()

# calls on run function
install.run()