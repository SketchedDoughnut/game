import requests
import os

wDir = os.path.dirname(os.path.abspath(__file__))

installer_data = requests.get('https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe')
if installer_data.status_code == '200':
    tmp_path = wDir + '/tmp'
    try:
        os.mkdir(tmp_path)
    except:
        pass
    exec_path = tmp_path + 'python-3.11.9-amd64.exe'
    f = open(exec_path, 'wb')
    f.write(installer_data.content)
    f.close()
    os.system(exec_path)