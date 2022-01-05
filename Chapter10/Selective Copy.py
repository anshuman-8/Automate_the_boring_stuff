
import os
from pathlib import Path

print("It prints all the .txt files")

for folderName, subfolders, filenames in os.walk(Path.home()):
    for files in folderName:
        if not files.endswith('.txt'):
            continue
        else:
            print(files)
    for files in filenames:
        if not files.endswith('.txt'):
            continue
        else:
            print(files)
    for files in subfolders:
        if not files.endswith('.txt'):
            continue
        else:
            print(files)

