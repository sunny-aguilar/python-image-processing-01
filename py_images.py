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
#print('PIL', Image.__version__)

# directory to iterate over
directory = './images'

# iterate over files in directory
for file in os.listdir(directory):
    if file.endswith('ic_add_location_black_48dp'):
        # print(file)
        # img = Image.open(file)
        # img.rotate(45).show()
        img = Image.open(file)
        print(img.format, img.size, img.mode)



