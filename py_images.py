#!/usr/bin/env python3
#
#   A script that iterates over image files in a directory and makes changes
#   to them using the Pillow library.
#
#   Author:     Sandro Aguilar
#   Date:       April 15, 2020
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import os, sys, PIL
from PIL import Image
#print('PIL', Image.__version__)

# directory to iterate over
directory = './images'

# iterate over files in directory
for file in os.listdir(directory):

    if not file.endswith('.DS_Store'):
        # file location and name
        file_loc = './images/'

        # open the file
        img = Image.open(file_loc + file)

        # rotate image 90 degrees
        img = img.rotate(90)
        
        # resize image
        newsize = (128, 128)
        img = img.resize(newsize)

        # all of this can be done with a one-liner since each method returs an object
        # img = Image.rotate(90).resize(newsize).convert('RGB').save(save_location)

        # save file
        save_location = './new_images/' + file + '.jpeg'
        img.convert('RGB').save(save_location)
