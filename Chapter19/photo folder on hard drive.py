#! python3
# Import modules and write comments to describe this program.
import os
from pathlib import Path
from PIL import Image

for foldername, subfolders, filenames in os.walk(Path.home()):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        # Check if file extension isn't .png or .jpg.
        if not filename.endswith('.png'):
            numNonPhotoFiles += 1
            continue    # skip to next filename

        # Open image file using Pillow.
        a=str(os.path.join(foldername, filename))
        img=Image.open(a)

        # Check if width & height are larger than 500.
        width, height = img.size
        if width>500 and height>500:
            # Image is large enough to be considered a photo.
            numPhotoFiles += 1
        else:
            # Image is too small to be a photo.
            numNonPhotoFiles += 1

    # If more than half of files were photos,
    # print the absolute path of the folder.
    # print(numNonPhotoFiles)
        print(numPhotoFiles)

    if (numPhotoFiles+numNonPhotoFiles)//2<numPhotoFiles:
        print(str(os.path.join(foldername)))