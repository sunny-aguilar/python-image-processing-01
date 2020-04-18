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
    # if file.endswith('ic_add_location_black_48dp'):
    # img = Image.open('./images/ic_add_location_black_48dp')
    if not file.endswith('.DS_Store'):
        file_loc = './images/' + file
        img = Image.open(file_loc)

        # rotate image 90 degrees
        img.rotate(90).show()

        # # new size
        newsize = (128, 128)

        img = Image.resize(newsize).show()
        # print(img.format, img.size, img.mode)
        # print(file)



