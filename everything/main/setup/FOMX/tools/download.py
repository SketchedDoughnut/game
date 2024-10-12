'''
This is a downloader for the FOMX system.
It's job is to download releases form github and store them properly.
....I think I got this code from ChatGPT.
--------------------------------------------------------------------------------------------------------------------------------
This files adheres to the commenting guidelines (kinda) :D
'''

# builtin modules
import requests
import sys
import time

# downloads the latest release from github
# and stores it in a file
# this was not written by me so I am not sure what is going on here
# but I still tried to comment it the best I could!
def download_latest_release(url, download_path):
    try:

        # get data from the url, and json it
        # this makes it into dictionary form
        response = requests.get(url)
        data = response.json()

        # if the repository / release does not exist, exit
        # this will make FOMX skip and continue on
        if 'message' in data and data['message'] == 'Not Found':
            print("Repository or release not found.")
            time.sleep(2)
            sys.exit()
            # return
        
        # I am not really sure...
        # what any of this does...
        if 'assets' not in data or len(data['assets']) == 0:
            download_url = data['zipball_url']  # Download the source code as a zipball
            _download_file(download_url, download_path)
        else:
            assets = data['assets']
            download_url = assets[0]['browser_download_url']
            _download_file(download_url, download_path)

    except Exception as e:
        print(f"Error: {e}")

# I also have no idea what this does, but basically it just downloads a file?
# yeah sure-
def _download_file(url, download_path):
    response = requests.get(url)
    with open(download_path, 'wb') as f:
        f.write(response.content)
    #print(f"Downloaded the latest release to {download_path}")
    print(f"FOMX: Downloaded the latest release to {download_path}")
    #print(f'Update: Downloaded the latest release')

# ???????????????????
# if __name__ == "__main__":
    # repo_url = "https://api.github.com/repos/SketchedDoughnut/development/releases/latest"
    # download_path = "latest_release.zip"  # Change the path if needed
    # download_latest_release(repo_url, download_path)