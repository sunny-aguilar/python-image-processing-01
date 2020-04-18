#!/usr/bin/env python3
#
#   A script that iterates over image files in a directory and makes changes
#   to them using the Pillow library.
#
#   Author:     Sandro Aguilar
#   Date:       April 15, 2020
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import os, sys
from PIL import Image

# directory to iterate over
directory = './images'

# iterate over files in directory
for filename in os.listdir(directory):
    if filename.endswith('.png'):
        # do stuff here to file
        im = Image.open('img1.jpg')
        im.rotate(45).show()



