#! /usr/bin/env python3

import requests
import os

# Read API key from keys file
keyFile = open('keys', 'r')
key = keyFile.readline().rstrip()

# Add your key from keys file to the API url
url = 'https://api.nasa.gov/planetary/apod?api_key='+key

# Set wallpaper directory to store image
global directory
directory = '/Users/'+username+'/Pictures/Wallpapers/'

# Request APOD and write image to Wallpapers directory
req = requests.get(url)
if req:
    APOD = r.json()['url']
    pic = requests.get(APOD, allow_redirects=True)
    if 'jpg' not in APOD:
        print('No image')
    else:
        open(directory, 'wb').write(pic.content)
else:
    print('Error getting Image')
