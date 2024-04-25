import shutil
import os
import json

def decide(
    if_full_redo
    ):
    if not if_full_redo:
        print('------------------------------------')
        print("""It appears files are missing from your installation. This can be detrimental to 
    the functionality of your game. Alternatively, there can be an issue 
    with the file named "File_list.json" in "everything/main/setup/file_list.json".
    Because of this, you can do three things:
        - Ignore this warning, and cancel the update. This will restore a backup made before beginning
        installation.
        - Re-install everything. The program can do this automatically, and it will likely fix your issue.
        - Update your file_list.json. This might not fix the issue if the release file is wrong.
    ------------------------------------""")
        print('To choose to re-install, type "full".')
        print('To choose to re-download file_list.json, type "re-download".')
        print('To choose to ignore, type "ignore".')
        choice = input('-> ')

        data_json_path = os.path.dirname(os.path.dirname(__file__))

        # for vscode
        data_json_path = os.path.dirname(data_json_path)
        
        data_json_path = os.path.join(data_json_path, 'data.json')

        if choice == 'full':
            print('------------------------------------')
            print('Update: Changing data.json...')
            f = open(data_json_path, 'r')
            dict = json.load(f)
            f.close()
            dict['shortcut'] = True
            dict['update'] = True
            dict['bounds'] = 'full'
            f = open(data_json_path, 'w')
            json.dump(dict, f)
            f.close()
            print('Update: data.json has been updated')
            print('------------------------------------')
            print('A full re-installation will now happen. Please re-launch.')
            print('------------------------------------')
            input('Enter anything to exit: ')
            exit()


        elif choice == 're-download':
            print('------------------------------------')
            print("""Please go to where you installed the game from and 
re-download the file 'file_list.json' located in 'everything/main/setup/file_list.json'""")
            print('------------------------------------')
            input('Enter anything to exit: ')
            exit()

        
        elif choice == 'ignore':
            print('------------------------------------')
            print("""This issue will be ignored. However, functionality can no longer be
guaranteed until action is taken to fix this issue.""")
            print('------------------------------------')
            print('Update: Changing data.json...')
            f = open(data_json_path, 'r')
            dict = json.load(f)
            f.close()
            dict['shortcut'] = True
            dict['update'] = False
            dict['bounds'] = 'x'
            f = open(data_json_path, 'w')
            json.dump(dict, f)
            f.close()
            print('Update: data.json has been updated')
            print('------------------------------------')
            input('Enter anything to exit: ')
            exit()