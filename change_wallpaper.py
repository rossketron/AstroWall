#! /usr/bin/env python3

import requests
import os
import pwd
import fnmatch

# Read API key from keys file
keyFile = open('keys.txt', 'r')
key = keyFile.readline().rstrip()

# Add your key from keys file to the API url
url = "https://api.nasa.gov/planetary/apod?api_key="+key

# Set wallpaper directory to store image
global directory
username = pwd.getpwuid(os.getuid()).pw_name
directory = '/Users/'+username+'/Pictures/Wallpapers/'

# Request APOD and write image to Wallpapers directory
req = requests.get(url)
if req:
    APOD = req.json()['url']
    pic = requests.get(APOD, allow_redirects=True)
    if 'jpg' not in APOD:
        print('Connected to API -- No image today')
    else:
        count = len(fnmatch.filter(os.listdir(directory), 'apod*'))
        file_name = "apod" + str(count+1) + ".jpg"
        open(directory+file_name, 'wb').write(pic.content)
        print('Image in Wallpapers 🤟')
else:
    print('Error Connecting to API 👎')
