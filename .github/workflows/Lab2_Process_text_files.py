#! /usr/bin/env python3

import os
import requests

# Get the list of all files and directories 
# in the /data/feedback directory 
path = "/data/feedback/"
# List all .txt files under /data/feedback directory that contains the actual feedback to be displayed on the company's website.
# Use the Python method listdir() to return a list containing all files and directories in the directory "path."
dir_list = os.listdir(path) 

#Traverse over each file and, from the contents of these text files, create a dictionary 
# by keeping title, name, date, and feedback as keys for the content value, respectively.
for file in dir_list:
    with open(os.path.join(path, file)) as filename:
        data = filename.read().split('\n')
        d = {}
        d['title'] = data[0]
        d['name'] = data[1]
        d['date'] = data[2]
        d['feedback'] = data[3]
        #Use the Python requests module to post the dictionary to the company's website. 
        #Use the request.post() method to make a POST request to http://<corpweb-external-IP>/feedback.
        response = requests.post("34.66.239.236/feedback/", data = d)
        print(response.status_code)
