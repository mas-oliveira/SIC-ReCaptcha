import requests
import shutil
import os
from os import path
from payload import get_payload_and_keyword
from datetime import datetime

payl_and_keyw = get_payload_and_keyword() #tuple [0] = url + tuple[1] = keyword
url = payl_and_keyw[0]

r = requests.get(url, stream=True)

while(True):
    payl_and_keyw = get_payload_and_keyword() #tuple [0] = url + tuple[1] = keyword
    url = payl_and_keyw[0]

    r = requests.get(url, stream=True)
    print(payl_and_keyw[1])
    if os.path.exists(payl_and_keyw[1]):
        current_path = os.getcwd()
        os.chdir(current_path + '/' + payl_and_keyw[1])
        with open(payl_and_keyw[1] + str(datetime.now()) + '.png', 'wb') as out_file:
            shutil.copyfileobj(r.raw, out_file)
        os.chdir(current_path)
    else:
        os.mkdir(payl_and_keyw[1])
        current_path = os.getcwd()
        os.chdir(current_path + '/' + payl_and_keyw[1])
        with open(payl_and_keyw[1] + str(datetime.now()) + '.png', 'wb') as out_file:
            shutil.copyfileobj(r.raw, out_file)
        os.chdir(current_path)

        