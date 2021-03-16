#! /usr/bin/env python3

import os
import requests

# Get the list of all files and directories 
# in the /data/feedback directory 
path = "/data/feedback/"
# 
dir_list = os.listdir(path) 

for file in dir_list:
    #print(file)
    with open(os.path.join(path, file)) as filename:
        data = filename.read().split('\n')
        d = {}
        d['title'] = data[0]
        d['name'] = data[1]
        d['date'] = data[2]
        d['feedback'] = data[3]
        response = requests.post("34.66.239.236/feedback/", data = d)
        print(response.status_code)
