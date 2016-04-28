
import shutil, os, time, sys
import datetime as dt
from datetime import  timedelta

source = '/Users/Lyci/Desktop/Folder1/'
destination = '/Users/Lyci/Desktop/Folder2/'

listfile= os.listdir(source)
print listfile

today=dt.datetime.now()
modtime=today-dt.timedelta(hours=24)

for files in listfile:
    if files.endswith(".txt"):
        mtime=dt.datetime.fromtimestamp(os.stat(source+files).st_mtime)
##        print mtime      
        if mtime > modtime:
            shutil.copy2(source+files,destination)
            print destination+files
        else:
            print "File is not new to copy"
