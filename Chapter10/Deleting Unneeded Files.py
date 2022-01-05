
import os
from pathlib import Path

# print("It prints all the .txt files")
# print(Path.home())

for folderName, subfolders, filenames in os.walk(Path.home()):
    for files in folderName:
        if os.path.getsize(folderName+files)>100000:
            print(files)
    for files in filenames:
        if os.path.getsize(filenames+files)>100000:
            print(files)
    for files in subfolders:
        if os.path.getsize(subfolders+files)>100000:
            print(files)
        


#Error that I am getting

# Traceback (most recent call last):
#   File "/home/anshuman/Desktop/Anshuman/Automate_the_boring_stuff/Chapter10/Deleting Unneeded Files.py", line 10, in <module>
#     if os.path.getsize(folderName+files)>100000:
#   File "/usr/lib/python3.8/genericpath.py", line 50, in getsize
#     return os.stat(filename).st_size
# FileNotFoundError: [Errno 2] No such file or directory: '/home/anshumanh'