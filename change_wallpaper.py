#! /usr/bin/env python3

import requests
import os
import pwd

# Read API key from keys file
keyFile = open('keys.txt', 'r')
key = keyFile.readline().rstrip()

# Add your key from keys file to the API url
url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

# Set wallpaper directory to store image
global directory
username = pwd.getpwuid(os.getuid()).pw_name
directory = '/Users/'+username+'/Pictures/Wallpapers/'

# Request APOD and write image to Wallpapers directory
req = requests.get(url)
print(url)
if req:
    APOD = req.json()['url']
    pic = requests.get(APOD, allow_redirects=True)
    if 'jpg' not in APOD:
        print('No image')
    else:
        open(directory+'pod.jpg', 'wb').write(pic.content)
else:
    print('Error getting Image')
