
import shutil

import os

source = '/Users/Lyci/Desktop/FolderA/'
destination = '/Users/Lyci/Desktop/FolderB/'
listfile= os.listdir(source)
print listfile
##shutil.move(source,destination)

for files in listfile:
    if files.endswith(".txt"):
        shutil.move(source+files,destination)
        print destination+files
    
