# imports
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
    def __init__(self):
        #self.install_path = './game_name/'
        new_string = ''
        #self.install_path = (input('Input wanted file directory for install below: \n--> ') + '/game_name/')
        self.install_path = (input('Input wanted file directory for install below: \n--> '))
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


    # making sure they are sure of their choice
    def safety_check(self):
        print("""
              You are running the installer; this will overwrite pre-existing files created by the installer previously.
              To confirm, type "confirm" below. Otherwise, type anything else.
              """)
        
        # checking if input confirms proceeding, cancelling if not
        if input('--> ') == "confirm":
            #try:
            #    os.system('clear')
            #except:
            #    pass
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
                print('! install cleaned')
            except:
                print('! no install')

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
                print('! install cleaned')
            except:
                print('! no install')

            print('Pre: Done cleaning; continuing...')
            time.sleep(1)
            print('---------------')

    
    ## getting info
    def setup(self):
        # getting inputs
    #    ## https://github.com/BirdLogics/sb3topy
    #    ## master
    #    self.url = input('Input repository URL: ')
    #    self.branch = input('Input respository branch: ')
    #    print('---------------')
        self.desktop_shortcut = (input('Do you want to add a desktop shortcut? (y/n) \n--> ').lower()) == 'y'


    # create temp dir and establish code file
    def create(self):
        # creating directories
        #print(f'Creating directory: {self.temp_path}')
        #os.mkdir(self.temp_path)
        print(f'Creating directory: {self.install_path}')
        os.mkdir(self.install_path)

        ## writing code to file
        #print('Writing code to file')
        #f = open(f'{self.temp_path}/gh_downloader.py', 'w')


   # function for running code written into the file (above)
    def download(self):
        # importing downloader, assigning vars
        # https://github.com/fbunaren/GitHubFolderDownloader
        #url = 'https://github.com/SketchedDoughnut/game'
        #branch = 'master'

        try:
            # initializing the downloader class with url and what branch
            downloader = self.Downloader('https://github.com/SketchedDoughnut/game')
            
            # try:
            #     # creating second download object
            #     downloader2 = self.Downloader()
            #     downloader2.load_repository('https://github.com/python/cpython/tree/3.9')
            # except Exception as e:
            #     print(f'!!! Second initial failed: {e}')

            try:
                # downloading
                #downloader.download(self.install_path, 'game_name', True)
                downloader.download(self.install_path)

                try:
                    # writing run path to text file (not used, not up to date)
                    url_path = f'{self.install_path}/main/top-level/content_url.txt'
                    print(url_path)
                    f = open(url_path, 'w')
                    f.write(f'{self.install_path}/main/top-level/game_data/main.py')
                    f.close()
                except Exception as e:
                    print(f'!!! Error with text file: {e}')

                # # running second installer to install python
                # try:
                #     downloader2.download(f'{self.install_path}/python')
                #     print('! Python 3.9 installed')
                # except Exception as e:
                #     print(f'!!! Python install failed: {e}')

                # from win32com.client import Dispatch

                # path = r"C:\Users\user\Desktop\game_name.lnk"  #This is where the shortcut will be created
                # target = rf"{self.install_path}/main/setup/inst-ver-win.py" # directory to which the shortcut is created

                # shell = Dispatch('WScript.Shell')
                # shortcut = shell.CreateShortCut(path)
                # shortcut.Targetpath = target
                # shortcut.save()
            
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


    # deletes temp tree
    def post_clean(self):
    #    try:
    #        os.system('clear')
    #    except:
    #        pass
        print('---------------')
        print('Post: Cleaning up')
        #shutil.rmtree('../')
        #print('---------------')
        #shutil.rmtree('./temp/')
        print('Note: If directory is not present, or is empty, check your inputs and run again.')
        print('Post: Done')


    def quit_install(self):
        # print(f'Downloading complete. Run executable at {install.install_path}/essentials/run_game/run_game.exe')
        print('---------------')
        print('Install complete. Exit in:')
        for i in range(3, 0, -1):
            print(f'{i}')
            time.sleep(1)

        # ensure an exit happens
        exit()


    def run(self):
        self.safety_check()
        self.pre_clean()
        self.setup()
        self.create()
        self.download()
        self.post_clean()
        self.quit_install()

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

                    # modified segment
                    # try:
                    #     os.system('clear')
                    # except:
                    #     print('x')
                    print(f'Installing file: {i}')


########################################################################
########################################################################
########################################################################
########################################################################

install = Install()
install.run()