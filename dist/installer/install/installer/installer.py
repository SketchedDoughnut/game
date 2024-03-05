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
        # files paths
        #self.temp_path = './temp'
        self.install_path = './install/'
        self.url = 'https://github.com/SketchedDoughnut/game'
        self.branch = 'game_files'
        self.run()


    # making sure they are sure of their choice
    def safety_check(self):
        print("""
              You are running the installer again; this will overwrite pre-existing files.
              To confirm, type "i confirm" below.
              """)
        
        # checking if input confirms proceeding, cancelling if not
        if input('--> ') == "i confirm":
            try:
                os.system('clear')
            except:
                pass
            pass
        else:
            print('Cancelling...')
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
            except:
                print('no install')

        else:
            print('Cleaning up directories before install')

            ## removing temp tree
            #try:
            #    shutil.rmtree(self.temp_path)
            #except:
            #    print('no temp')
            
            # removing install tree
            try:
                shutil.rmtree(self.install_path)
            except:
                print('no install')

            print('Done cleaning; continuing...')
            print('---------------')

    
    # getting info
    def setup(self):
        # getting inputs
        ## https://github.com/BirdLogics/sb3topy
        ## master
        self.url = input('Input repository URL: ')
        self.branch = input('Input respository branch: ')
        print('---------------')


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
        # importing downloader 
        # https://github.com/fbunaren/GitHubFolderDownloader

        try:
            # initializing the downloader class with url and what branch
            downloader = self.Downloader(self.url, self.branch)

            try:
                # downloading
                downloader.download(self.install_path)
            
            except Exception as e:
                print(f'Error while downloading: {e}')
                print('Cleaning up then exiting...')
                self.pre_clean('error')
                exit()

        except Exception as e:
            print(f'Error while creating object: {e}')
            print('Consider re-entering branch name / github url')
            print('Cleaning up then exiting...')
            self.pre_clean('error')
            exit()         


    # deletes temp tree
    def post_clean(self):
    #    try:
    #        os.system('clear')
    #    except:
    #        pass
        print('---------------')
        print('Cleaning up')
        #print('---------------')
        #shutil.rmtree('./temp/')
        print('Note: If directory is not present, or is empty, check your inputs and run again.')
        print('--------------')
        print('Done')


    def run(self):
        self.safety_check()
        self.pre_clean()
        #self.setup()
        self.create()
        self.download()
        self.post_clean()
        #print('Run done')

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
print('Install done, waiting 5 seconds then running fractal. If nothing happens, click enter.')
for i in range(5,0, -1):
    print(f'in {i}...')
    time.sleep(1)
os.system(f'python ./main.py')