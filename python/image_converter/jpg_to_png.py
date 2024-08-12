# This example shows how to handle command line arguments, list files, create dirs and do some image manipulation.
# Requires Pillow (https://pillow.readthedocs.io/).
#
# Simple CLI utility which receives two arguments:
# The first arg is a source folder containing jpg images.
# The second argument is a destination folder where all jpg images found in the soource folder will be saved as png.
# Origin and destination folders are considered relative to the current location.

import os
import sys
from PIL import Image

# Get the command line argumes used to run this script.
args = sys.argv

# First arg is always this script file, so we verify there are 3 arguments present.
if len(args) < 3:
    print('Invalid arguments, please specify a source and destination folders')
else:
    # args[0] -> script file name.
    source_folder = args[1]
    destination_folder = args[2]

    if not source_folder.endswith('/'):
        source_folder = f'{source_folder}/'
        
    if not destination_folder.endswith('/'):
        destination_folder = destination_folder + '/'

    jpgs = []
    try:
        print(f'Will read from "{source_folder}" and save the converted files to "{destination_folder}"')
        
        # os module allows us to perform file/folder operations.
        files = os.listdir(source_folder)
        # print(f'Files found {files}')
        
        # Filter only jpg files. Would love this (comprehensions) in Java.
        jpgs = [jpg for jpg in files if jpg.endswith('.jpg')]
        # print (f'JPGs found {jpgs}')
    except FileNotFoundError:
        print(f'Origin folder "{source_folder}" does not exist. \nPlease check and try again...')
        
    if len(jpgs) > 0:
        # If destination_folder does not exist, create it.
        if not os.path.exists(destination_folder):
            os.mkdir(destination_folder)
            print(f'Folder "{destination_folder}" created...')
        # Can also be done by catching the exeption when trying to list files in dir.
        # try:
        #     os.listdir(destination_folder)
        # except FileNotFoundError:
        #     os.mkdir(destination_folder)
        #     print(f'Folder "{destination_folder}" created...')
        
        # Process every jpg image found under source_folder folder by saving it as png into destination_folder folder.
        for jpg_file_name in jpgs:
            # Two ways to concatenate strings
            src_path = f'{source_folder}{jpg_file_name}'
            # os.path.splitext returns a tuple containing the file name and extension separate.
            dest_path = destination_folder + os.path.splitext(jpg_file_name)[0] + '.png'
            
            print(f'File "{src_path}" will de saved as {dest_path}')
            
            image = Image.open(src_path)
            # Image allows us to change the original format of the current image while saving it.
            image.save(dest_path, format='png')
            image.close()
        
        print(f'Done. {len(jpgs)} images saved to {destination_folder}...')
    